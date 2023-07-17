# Implementation of a content server application
# that can respond to requests for content.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 13-jul-2023
#

import sys
from threading import Thread
from threading import Lock
import random
sys.path.append('./lib')
import settings
import common


# setup app module & start the face handler thread
def setup(dispatch):
    
    # start app worker that generates interests
    w = Worker(dispatch)
    w.start()

    # create the handler
    handler = Handler(dispatch)
    
    # return the handler for main to call the 
    # handle_msg function
    return handler


# worker thread that listens to ports and gets 
# packets arriving over the ports
class Worker(Thread):
    
    # constructor to get all parameters
    def __init__(self, dispatch):
        self.dispatch = dispatch
        super().__init__()

    def run(self):
        
        # wait for the initial delay
        time.sleep(settings.IOTGWAPP_START_DELAY_SEC)
        
        # create face registration message
        facereg = FaceRegistration()
        facereg.face_id = settings.IOTGWAPP_FACE_ID
        facereg.face_type = common.FaceType.FACETYPE_APP
        facereg.face_module_name = settings.IOTGWAPP_MODULE_NAME
        facereg.prefix_served = ''
        for i in range(len(settings.IOTGWAPP_SERVED_PREFIXES)):
            if i == 0
                facereg.prefix_served = facereg.prefix_served + settings.IOTGWAPP_SERVED_PREFIXES[i]
            else:
                facereg.prefix_served = facereg.prefix_served + ':' + settings.IOTGWAPP_SERVED_PREFIXES[i]

        # encapsulate registration message
        encap = common.PacketEncap()
        encap.from_direction = common.DirectionType.FROM_APP
        encap.from_direction_module_name = settings.IOTGWAPP_MODULE_NAME
        encap.from_face_id = settings.IOTGWAPP_FACE_ID
        encap.to_direction = common.DirectionType.TO_CCN
        encap.packet_contents = facereg

        # lock and send message
        with common.system_lock:
            dispatch(encap)


# handler to recive app packet
class Handler:

    # constructor to get all parameters
    def __init__(self, dispatch):
        self.dispatch = dispatch
   
    # function handles when data received by this app
    def handle_msg(encap):
        
        # the app only expects Interest messages
        if type(encap.packet_contents) is Interest:

            # log
            logmsg = settings.IOTGWAPP_MODULE_NAME + ':Interest received '
            common.log_activity(logmsg)

            # check if it is for a served prefix
            found = False
            for prefix in settings.IOTGWAPP_SERVED_PREFIXES:
                if prefix == encap.packet_contents.prefix:
                    found = True
                    break
            
            # if a not served prefix, return
            if !found:
                
                # log
                logmsg = settings.IOTGWAPP_MODULE_NAME + ':Unserved prefix '
                common.log_activity(logmsg)
                
                return
            
            # generate random value to return
            valstr = 'no-val'
            for i in range(len(settings.IOTGWAPP_DATA_HOSTED)):
                if settings.IOTGWAPP_DATA_HOSTED[i] == encap.packet_contents.name:
                    upper, lower = settings.IOTGWAPP_DATA_RANGES[i].split(':')
                    upper = float(upper)
                    lower = float(lower)
                    valfloat = round(random.uniform(lower, upper),2)
                    valstr = '%.2f' % valfloat
                    break
            
            # build Content Obj to return
            contentobjmsg = ContentObject()
            contentobjmsg.prefix = encap.packet_contents.prefix
            contentobjmsg.name = encap.packet_contents.name
            contentobjmsg.payload = valstr
            
            # encapsulate created message
            encap = common.PacketEncap()
            encap.from_direction = common.DirectionType.FROM_APP
            encap.from_module_name = settings.IOTGWAPP_MODULE_NAME
            encap.from_face_id = settings.IOTGWAPP_FACE_ID
            encap.to_direction = common.DirectionType.TO_CCN
            encap.packet_contents = contentobjmsg
        
            # lock and call function to send to CCN
            with common.system_lock:
                dispatch(encap)    

        # unknown message
        else:
            # log
            logmsg = settings.TEMPREADER_MODULE_NAME + ':Unknown message received to sent '
            common.log_activity(logmsg)
            return
        

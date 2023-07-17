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
        time.sleep(settings.SERVER_START_DELAY_SEC)
        
        # create face registration message
        facereg = FaceRegistration()
        facereg.face_id = settings.SERVER_FACE_ID
        facereg.face_type = common.FaceType.FACETYPE_APP
        facereg.face_module_name = settings.SERVER_MODULE_NAME
        facereg.prefix_served = settings.SERVER_DATA_REQ_PREFIX

        # encapsulate registration message
        encap = common.PacketEncap()
        encap.from_direction = common.DirectionType.FROM_APP
        encap.from_direction_module_name = settings.SERVER_MODULE_NAME
        encap.from_face_id = settings.SERVER_FACE_ID
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
            logmsg = settings.SERVER_MODULE_NAME + ':Interest received '
            common.log_activity(logmsg)

            # check if it is for a served prefix
            if encap.packet_contents.prefix == settings.SERVER_DATA_REQ_PREFIX:
                
                # build Content Obj to return
                contentobjmsg = ContentObject()
                contentobjmsg.prefix = encap.packet_contents.prefix
                contentobjmsg.name = encap.packet_contents.name
                contentobjmsg.seg_num = encap.packet_contents.seg_num
                contentobjmsg.payload = 'payload contents ' + str(random.randint(1000, 10000))
                
                # encapsulate created message
                encap = common.PacketEncap()
                encap.from_direction = common.DirectionType.FROM_APP
                encap.from_module_name = settings.SERVER_MODULE_NAME
                encap.from_face_id = settings.SERVER_FACE_ID
                encap.to_direction = common.DirectionType.TO_CCN
                encap.packet_contents = contentobjmsg
        
                # lock and call function to send to CCN
                with common.system_lock:
                    dispatch(encap)    
            else:
                # log
                logmsg = settings.SERVER_MODULE_NAME + ':Unserved prefix '
                common.log_activity(logmsg)

        # unknown message
        else:
            # log
            logmsg = settings.SERVER_MODULE_NAME + ':Unknown message received to sent '
            common.log_activity(logmsg)
            return
        

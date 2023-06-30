# Implementation of a dummy temperature reading application
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 26-jun-2023
#

import sys
from threading import Thread
from threading import Lock
sys.path.append('./lib')
import settings
import common


# setup app module & start the face handler thread
def setup(dispatch):
    
    # start app worker that generates interests
    w = Worker(dispatch)
    w.start()

    # create the handler
    handler = Handler()
    
    # return the handler for main to call the 
    # handle_msg function
    return handler


# worker thread that listens to ports and gets 
# packets arriving over the ports
class Worker(Thread):
    
    # constructor to get all parameters
    def __init__(self, dispatch):
        self.dispatch = dispatch

    def run(self):
        
        # wait for the initial delay
        time.sleep(settings.TEMPREADER_START_DELAY_SEC)
        
        # create face registration message
        facereg = FaceRegistration()
        facereg.face_id = settings.TEMPREADER_FACE_ID
        facereg.face_module_name = settings.TEMPREADER_MODULE_NAME
        facereg.prefix_served = None
        
        # encapsulate registration message
        encap = common.PacketEncap()
        encap.from_direction = common.DirectionType.FROM_APP
        encap.from_direction_module_name = settings.TEMPREADER_MODULE_NAME
        encap.from_face_id = settings.TEMPREADER_FACE_ID
        encap.to_direction = common.DirectionType.TO_CCN
        encap.packet_contents = facereg

        # lock and send message
        with common.system_lock:
            dispatch(encap)
        
        while True:
            
            # create interest as if it was received from the socket
            interestmsg = Interest()
            interestmsg.prefix = settings.TEMPREADER_DATA_REQ_PREFIX
            interestmsg.name = settings.TEMPREADER_DATA_NAME
        
            # encapsulate created message
            encap = common.PacketEncap()
            encap.from_direction = common.DirectionType.FROM_APP
            encap.from_direction_module_name = settings.TEMPREADER_MODULE_NAME
            encap.from_face_id = settings.TEMPREADER_FACE_ID
            encap.to_direction = common.DirectionType.TO_CCN
            encap.packet_contents = interestmsg
        
            # lock and call function to process message
            with common.system_lock:
                dispatch(encap)    

            time.sleep(settings.TEMPREADER_DATA_REQ_INTERVAL_SEC)


# handler to recive app packet
class Handler:
    
    # function handles when data received by this app
    def handle_msg(encap):
        
        # the app only expects ContentObject messages
        if type(encap.packet_contents) is ContentObject:
            
            # process ContentObject
            pass

            # log
            logmsg = settings.TEMPREADER_MODULE_NAME + ':ContentObj received '
            common.log_activity(logmsg)

        # unknown message
        else:
            # log
            logmsg = settings.TEMPREADER_MODULE_NAME + ':Unknown message received to sent '
            common.log_activity(logmsg)
            return
        

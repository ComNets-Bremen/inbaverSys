# Implementation of a dummy temperature reading application
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 26-jun-2023
#

import sys
import time
from threading import Thread
from threading import Lock
import settings
import common


# setup app module & start the face handler thread
def setup(dispatch):

    # start app worker that generates interests
    w = Worker(dispatch)
    w.start()

    # create the handler
    handler = Handler(dispatch)

    # log
    logmsg = settings.TEMPREADER_MODULE_NAME + ' : Setup completed, operation started'        
    with common.system_lock:
        common.log_activity(logmsg)

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

        try:

            # wait for the initial delay
            time.sleep(settings.TEMPREADER_START_DELAY_SEC)
        
            # create face registration message
            facereg = common.FaceRegistration()
            facereg.face_id = settings.TEMPREADER_FACE_ID
            facereg.face_type = common.FaceType.FACETYPE_APP
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
                self.dispatch(encap)

            while True:
            
                # create interest as if it was received from the socket
                interestmsg = common.Interest()
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
                    self.dispatch(encap)    

                time.sleep(settings.TEMPREADER_DATA_REQ_INTERVAL_SEC)

        except Exception as e:
            print(e)


# handler to recive app packet
class Handler:
    
    # constructor 
    def __init__(self, dispatch):
        self.dispatch = dispatch

    # function handles when data received by this app
    def handle_msg(self, encap):
        
        # the app only expects ContentObject messages
        if type(encap.packet_contents) is common.ContentObject:
            
            # log
            logmsg = settings.TEMPREADER_MODULE_NAME + ' : ContentObj received '
            common.log_activity(logmsg)
            
            # log ContentObject values

            logmsg = settings.TEMPREADER_MODULE_NAME + ' : Content in message:Temperature ' + encap.packet_contents.payload
            common.log_activity(logmsg)
            
        # unknown message
        else:
            # log
            logmsg = settings.TEMPREADER_MODULE_NAME + ' : Unexpected message received '
            common.log_activity(logmsg)
            return
        

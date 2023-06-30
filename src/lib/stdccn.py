# Implementation of a dummy CCN forwarder
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


# setup the ccn module & start the handler thread
def setup(dispatch):
    
    # start worker that performs general maintenance work (cache entry expiration)
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
                
        while True:
            time.sleep(10)


# handler to recive app packet
class Handler:
    
    # function handles when data received by this app
    def handle_msg(encap):

        # process FaceRegistration message
        if type(encap.packet_contents) is FaceRegistration:
            # log
            logmsg = settings.CCN_LAYER + ':FaceRegistration message received '
            common.log_activity(logmsg)

        # process Interest message
        else if type(encap.packet_contents) is Interest:
            # log
            logmsg = settings.CCN_LAYER + ':Interest message received '
            common.log_activity(logmsg)

        # process ContentObject message
        else if type(encap.packet_contents) is ContentObject:
            # log
            logmsg = settings.CCN_LAYER + ':ContentObject message received '
            common.log_activity(logmsg)

        # unknown message
        else:
            # log
            logmsg = settings.CCN_LAYER + ':Unknown message received '
            common.log_activity(logmsg)
            return
        

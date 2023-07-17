# Implementation of a LoRa module handling a face.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 02-jul-2023
#

import sys
from threading import Thread
from threading import Lock
import socket
sys.path.append('./lib')
import settings
import common


# setup link module & start the face handler thread
def setup(dispatch):
    
    # start all face handling workers
    for faceindex in range(len(settings.LORA_FACE_IDS)):
        w = Worker(faceindex, dispatch)
        w.start()

    # create the handler
    handler = Handler(dispatch)
    
    # return the handler for main to call the 
    # handle_msg function
    return handler


# worker thread that listens incoming packets
class Worker(Thread):
    
    # constructor to get all parameters
    def __init__(self, faceindex, dispatch):
        self.faceindex = faceindex
        self.dispatch = dispatch
        super().__init__()

    def run(self):
        
        # wait for the initial delay
        time.sleep(10)
        
        # create face registration message
        facereg = FaceRegistration()
        facereg.face_id = settings.LORA_FACE_IDS[faceindex]
        facereg.face_type = common.FaceType.FACETYPE_LINK
        facereg.face_module_name = settings.LORA_MODULE_NAME
        facereg.prefix_served = None
        
        # encapsulate registration message
        encap = common.PacketEncap()
        encap.from_direction = common.DirectionType.FROM_LINK
        encap.from_direction_module_name = settings.LORA_MODULE_NAME
        encap.from_face_id = settings.LORA_FACE_IDS[faceindex]
        encap.to_direction = common.DirectionType.TO_CCN
        encap.packet_contents = facereg

        # lock and send message
        with common.system_lock:
            dispatch(encap)
        
        # TODO: implement reading incomming packets

# handler to send packets out
class Handler:

    # constructor 
    def __init__(self, dispatch):
        self.dispatch = dispatch
    
    # function used to send packets to the given face
    def handle_msg(encap):

        # TODO: implement sending out messages


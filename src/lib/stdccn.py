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


facelist = []

# setup the ccn module & start the handler thread
def setup(dispatch):
    
    # start worker that performs general maintenance work (cache entry expiration)
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

    def run(self):
                
        while True:
            time.sleep(10)


# handler to recive app packet
class Handler:
    
    # constructor 
    def __init__(self, dispatch):
        self.dispatch = dispatch
    
    # function handles when data received by this app
    def handle_msg(encap):

        # process FaceRegistration message
        if type(encap.packet_contents) is common.FaceRegistration:
            # log
            logmsg = settings.CCN_LAYER + ':FaceRegistration message received '
            common.log_activity(logmsg)
            
            # save face info
            faceinfo = common.FaceInfo()
            faceinfo.face_id = encap.packet_contents.face_id
            faceinfo.face_module_name = encap.packet_contents.face_module_name
            faceinfo.prefix_served = encap.packet_contents.prefix_served
            facelist.append(faceinfo)
            

        # process Interest message
        else if type(encap.packet_contents) is common.Interest:
            # log
            logmsg = settings.CCN_LAYER + ':Interest message received:From ' + encap.from_face_id
            common.log_activity(logmsg)
            
            # loop around the face list and send Interest to all (except the arrival face)
            for faceinfo in facelist:
                if encap.from_module_name == faceinfo.face_module_name
                   and encap.from_face_id == faceinfo.face_id:
                    continue
                
                # create an Interest to send
                newinterest = common.Interest()
                newinterest.prefix = encap.packet_contents.prefix
                newinterest.name = encap.packet_contents.name
                
                # create a new PacketEncap
                newencap = common.PacketEncap()
                newencap.from_direction = common.DirectionType.FROM_CCN
                newencap.from_module_name = common.CCN_LAYER
                newencap.to_direction = common.DirectionType.TO_LINK
                newencap.to_module_name = faceinfo.face_module_name
                newencap.to_face_id = faceinfo.face_id
                newencap.packet_contents = newinterest
                
                # send packet out
                dispatch(newencap)

        # process ContentObject message
        else if type(encap.packet_contents) is common.ContentObject:
            # log
            logmsg = settings.CCN_LAYER + ':ContentObject message received:From ' + encap.from_face_id
            common.log_activity(logmsg)

            # loop around the face list and send ContentObject to all (except the arrival face)
            for faceinfo in facelist:
                if encap.from_module_name == faceinfo.face_module_name
                   and encap.from_face_id == faceinfo.face_id:
                    continue
                
                # create an Interest to send
                newcontentobj = common.ContentObject()
                newcontentobj.prefix = encap.packet_contents.prefix
                newcontentobj.name = encap.packet_contents.name
                newcontentobj.payload = encap.packet_contents.payload
                
                # create a new PacketEncap
                newencap = common.PacketEncap()
                newencap.from_direction = common.DirectionType.FROM_CCN
                newencap.from_module_name = common.CCN_LAYER
                newencap.to_direction = common.DirectionType.TO_LINK
                newencap.to_module_name = faceinfo.face_module_name
                newencap.to_face_id = faceinfo.face_id
                newencap.packet_contents = newcontentobj

                # send packet out
                dispatch(newencap)
            

        # unknown message
        else:
            # log
            logmsg = settings.CCN_LAYER + ':Unknown message received:From ' + encap.from_face_id
            common.log_activity(logmsg)
            return
        

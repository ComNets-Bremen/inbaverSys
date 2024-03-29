# Implementation of a dummy CCN forwarder
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 26-jun-2023
#

import sys
import time
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

    # log
    logmsg = settings.STDCCN_MODULE_NAME + ' : Setup completed, operation started'        
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
            # log
            logmsg = settings.STDCCN_MODULE_NAME + ' : Worker thread started'        
            with common.system_lock:
                common.log_activity(logmsg)

            while True:
                
                    # just loop endlessly
                    time.sleep(5)
                
        except Exception as e:
            print(e)


# handler to recive app packet
class Handler:
    
    # constructor 
    def __init__(self, dispatch):
        self.dispatch = dispatch
    
    # function handles when data received by this app
    def handle_msg(self, encap):
        global facelist

        # process FaceRegistration message
        if type(encap.packet_contents) is common.FaceRegistration:

            # log
            logmsg = settings.STDCCN_MODULE_NAME + ' : FaceRegistration message received:From ' + encap.from_face_id
            common.log_activity(logmsg)
            
            # save face info
            faceinfo = common.FaceInfo()
            faceinfo.face_id = encap.packet_contents.face_id
            faceinfo.face_module_name = encap.packet_contents.face_module_name
            faceinfo.prefix_served = encap.packet_contents.prefix_served
            facelist.append(faceinfo)
            

        # process Interest message
        elif type(encap.packet_contents) is common.Interest:

            # log
            logmsg = settings.STDCCN_MODULE_NAME + ' : Interest message received:From ' + encap.from_face_id
            common.log_activity(logmsg)
            
            # loop around the face list and send Interest to all (except the arrival face)
            for faceinfo in facelist:
                if encap.from_module_name == faceinfo.face_module_name \
                   and encap.from_face_id == faceinfo.face_id:
                    continue
                
                # create an Interest to send
                newinterest = common.Interest()
                newinterest.prefix = encap.packet_contents.prefix
                newinterest.name = encap.packet_contents.name
                newinterest.seg_num = encap.packet_contents.seg_num
                
                # create a new PacketEncap
                newencap = common.PacketEncap()
                newencap.from_direction = common.DirectionType.FROM_CCN
                newencap.from_module_name = settings.CCN_LAYER
                newencap.to_direction = common.DirectionType.TO_LINK
                newencap.to_module_name = faceinfo.face_module_name
                newencap.to_face_id = faceinfo.face_id
                newencap.packet_contents = newinterest
                
                # send packet out
                self.dispatch(newencap)

        # process ContentObject message
        elif type(encap.packet_contents) is common.ContentObject:

            # log
            logmsg = settings.STDCCN_MODULE_NAME + ' : ContentObject message received:From ' + encap.from_face_id
            common.log_activity(logmsg)

            # loop around the face list and send ContentObject to all (except the arrival face)
            for faceinfo in facelist:
                if encap.from_module_name == faceinfo.face_module_name \
                   and encap.from_face_id == faceinfo.face_id:
                    continue
                
                # create an Interest to send
                newcontentobj = common.ContentObject()
                newcontentobj.prefix = encap.packet_contents.prefix
                newcontentobj.name = encap.packet_contents.name
                newcontentobj.seg_num = encap.packet_contents.seg_num
                newcontentobj.payload = encap.packet_contents.payload
                
                # create a new PacketEncap
                newencap = common.PacketEncap()
                newencap.from_direction = common.DirectionType.FROM_CCN
                newencap.from_module_name = settings.CCN_LAYER
                newencap.to_direction = common.DirectionType.TO_LINK
                newencap.to_module_name = faceinfo.face_module_name
                newencap.to_face_id = faceinfo.face_id
                newencap.packet_contents = newcontentobj

                # send packet out
                self.dispatch(newencap)
            

        # unknown message
        else:
            # log
            logmsg = settings.STDCCN_MODULE_NAME + ' : Unknown message received:From ' + encap.from_face_id
            common.log_activity(logmsg)
            return
        

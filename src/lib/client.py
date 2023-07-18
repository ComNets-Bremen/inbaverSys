# Implementation of a simple content downloading application
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 17-jul-2023
#

import sys
import time
import random
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
    logmsg = settings.CLIENT_MODULE_NAME + ' : Setup completed, operation started'        
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
            time.sleep(settings.CLIENT_START_DELAY_SEC)
        
            # create face registration message
            facereg = common.FaceRegistration()
            facereg.face_id = settings.CLIENT_FACE_ID
            facereg.face_type = common.FaceType.FACETYPE_APP
            facereg.face_module_name = settings.CLIENT_MODULE_NAME
            facereg.prefix_served = 'ddd'
        
            # encapsulate registration message
            encap = common.PacketEncap()
            encap.from_direction = common.DirectionType.FROM_APP
            encap.from_direction_module_name = settings.CLIENT_MODULE_NAME
            encap.from_face_id = settings.CLIENT_FACE_ID
            encap.to_direction = common.DirectionType.TO_CCN
            encap.packet_contents = facereg

            # lock and send message
            with common.system_lock:
                self.dispatch(encap)

            while True:
                
                # setup new content download details
                data_name_prefixes = settings.CLIENT_DATA_NAME_PREFIXES.split(':')
                data_name_suffix_range = settings.CLIENT_DATA_NAME_SUFFIX_RANGE.split(':')
                data_name_seg_range = settings.CLIENT_DATA_NAME_SEGMENT_RANGE.split(':')                
                rnd_data_name_prefix_index = random.randint(0, len(data_name_prefixes) - 1)
                rnd_data_name_suffix_val = random.randint(int(data_name_suffix_range[0]), int(data_name_suffix_range[1]))
                rnd_data_name_total_seg_nums = random.randint(int(data_name_seg_range[0]), int(data_name_seg_range[1]))
                filename = data_name_prefixes[rnd_data_name_prefix_index] + '-' + str(rnd_data_name_suffix_val)
                seg_num = 0

                # log
                with common.system_lock:
                    logmsg = settings.CLIENT_MODULE_NAME + ' : Downloading new content ' + settings.CLIENT_DATA_REQ_PREFIX + ' ' + filename \
                                + ' segments ' + str(rnd_data_name_total_seg_nums)
                    common.log_activity(logmsg)

                while seg_num < rnd_data_name_total_seg_nums:
                    
                    # create interest as if it was received from the socket
                    interestmsg = common.Interest()
                    interestmsg.prefix = settings.CLIENT_DATA_REQ_PREFIX
                    interestmsg.name = filename
                    interestmsg.seg_num = seg_num
        
                    # encapsulate created message
                    encap = common.PacketEncap()
                    encap.from_direction = common.DirectionType.FROM_APP
                    encap.from_direction_module_name = settings.CLIENT_MODULE_NAME
                    encap.from_face_id = settings.CLIENT_FACE_ID
                    encap.to_direction = common.DirectionType.TO_CCN
                    encap.packet_contents = interestmsg

                    # log
                    with common.system_lock:
                        logmsg = settings.CLIENT_MODULE_NAME + ' : Generating Interest  ' + settings.CLIENT_DATA_REQ_PREFIX + ' ' + filename \
                                + ' segment ' + str(seg_num)
                        common.log_activity(logmsg)

                    # lock and call function to process message
                    with common.system_lock:
                        self.dispatch(encap)

                    # increment the segment number
                    seg_num = seg_num + 1

                    # wait before requesting next segment
                    time.sleep(settings.CLIENT_SEGMENT_REQ_INTERVAL_SEC)

                # wait before next content download
                time.sleep(settings.CLIENT_SEGMENT_REQ_INTERVAL_SEC)

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
            logmsg = settings.CLIENT_MODULE_NAME + ' : ContentObj received '
            common.log_activity(logmsg)
            
            # log ContentObject values

            logmsg = settings.CLIENT_MODULE_NAME + ' : Content in message:Payload ' + encap.packet_contents.payload
            common.log_activity(logmsg)
            
        # unknown message
        else:
            # log
            logmsg = settings.CLIENT_MODULE_NAME + ' : Unexpected message received '
            common.log_activity(logmsg)
            return
        

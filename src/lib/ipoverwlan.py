# Implementation of a WLAN module handling multiple
# faces. Each face is uniquely identified by an ID and each 
# will have its corresponding IP next hop information.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 22-jun-2023
#

import sys
import time
from threading import Thread
from threading import Lock
import socket
sys.path.append('./lib')
import settings
import common


# setup link module & start the face handler thread
def setup(dispatch):

    # start all face handling workers
    for faceindex in range(len(settings.IPOVERWLAN_FACE_IDS)):
        w = Worker(faceindex, dispatch)
        w.start()

    # create the handler
    handler = Handler(dispatch)

    # log
    logmsg = settings.IPOVERWLAN_MODULE_NAME + ' : Setup completed, operation started'        
    with common.system_lock:
        common.log_activity(logmsg)

    # return the handler for main to call the 
    # handle_msg function
    return handler


# worker thread that listens to ports and gets 
# packets arriving over the ports send up the stack
class Worker(Thread):
    
    # constructor to get all parameters
    def __init__(self, faceindex, dispatch):
        self.faceindex = faceindex
        self.dispatch = dispatch
        super().__init__()

    def run(self):

        try:

            # log
            logmsg = settings.IPOVERWLAN_MODULE_NAME + ' : Worker thread started'        
            with common.system_lock:
                common.log_activity(logmsg)

            # wait for the initial delay
            time.sleep(10)
        
            # create face registration message
            facereg = common.FaceRegistration()
            facereg.face_id = settings.IPOVERWLAN_FACE_IDS[self.faceindex]
            facereg.face_type = common.FaceType.FACETYPE_LINK
            facereg.face_module_name = settings.IPOVERWLAN_MODULE_NAME
            facereg.prefix_served = None
        
            # encapsulate registration message
            encap = common.PacketEncap()
            encap.from_direction = common.DirectionType.FROM_LINK
            encap.from_direction_module_name = settings.IPOVERWLAN_MODULE_NAME
            encap.from_face_id = settings.IPOVERWLAN_FACE_IDS[self.faceindex]
            encap.to_direction = common.DirectionType.TO_CCN
            encap.packet_contents = facereg

            # lock and send message
            with common.system_lock:
                self.dispatch(encap)
        
            # create socket and bind to given port
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('', settings.IPOVERWLAN_LOCAL_PORTS[self.faceindex]))
        
            while True:

                # do blocking socket read
                byte_msg, addr = s.recvfrom(1024)
            
                # convert message to string
                msg_contents = byte_msg.decode('UTF-8')

                # log
                logmsg = settings.IPOVERWLAN_MODULE_NAME + ' : Received message : Contents - ' + msg_contents
                with common.system_lock:
                    common.log_activity(logmsg)

                # split message into components
                msg_parts = msg_contents.split('::')
            
                # create encap message
                encap.from_direction = common.DirectionType.FROM_LINK
                encap.from_direction_module_name = settings.IPOVERWLAN_MODULE_NAME
                encap.from_face_id = settings.IPOVERWLAN_FACE_IDS[self.faceindex]
                encap.to_direction = common.DirectionType.TO_CCN
            
                # create message from received string
                if msg_parts[0] == 'Interest':
                    interestmsg = common.Interest()
                    interestmsg.prefix = msg_parts[1]
                    interestmsg.name = msg_parts[2]
                    encap.packet_contents = interestmsg
                
                elif msg_parts[0] == 'ContentObject':
                    contentobjmsg = ContentObject()
                    contentobjmsg.prefix = msg_parts[1]
                    contentobjmsg.name = msg_parts[2]
                    contentobjmsg.payload = msg_parts[3]
                    encap.packet_contents = contentobjmsg

                else:
                    # log
                    logmsg = settings.IPOVERWLAN_MODULE_NAME + ' : Unknown message received'
                    with common.system_lock:
                        common.log_activity(logmsg)
                    continue
                    
                # lock and call function to process message
                with common.system_lock:
                    self.dispatch(encap)

        except Exception as e:
            print(e)


# handler to send packets out
class Handler:

    # constructor 
    def __init__(self, dispatch):
        self.dispatch = dispatch
    
    # function used to send packets to the given face
    def handle_msg(self, encap):

        # find the faceindex from face id
        found = False
        faceindex = None
        for i in range(len(settings.IPOVERWLAN_FACE_IDS)):
            if settings.IPOVERWLAN_FACE_IDS[i] == encap.to_face_id:
                found = True
                faceindex = i
                break
        
        # extract socket information
        if found:
            
            # get ipaddress and port
            ipaddress, port = settings.IPOVERWLAN_IP_CONNECTIONS[faceindex].split(':')
            
        else:
            
            # log
            logmsg = settings.IPOVERWLAN_MODULE_NAME + ' : Unknown face ID given'
            common.log_activity(logmsg)
            return
            
        # setup send socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # create address object with IP address and port
        addr = (ipaddress, int(port))

        # build packet to send out
        msg_contents = ''
        
        # build Interest message
        if type(encap.packet_contents) is common.Interest:
            
            # log
            logmsg = settings.IPOVERWLAN_MODULE_NAME + ' : Interest received to be sent over ' + encap.to_face_id
            common.log_activity(logmsg)
            
            # create Interest packet to send over IP
            msg_contents = 'Interest::' + encap.packet_contents.prefix + '::' + encap.packet_contents.name

        # build ContentObject message
        elif type(encap.packet_contents) is common.ContentObject:
            
            # log
            logmsg = settings.IPOVERWLAN_MODULE_NAME + ' : ContentObj received to be sent over ' + encap.to_face_id
            common.log_activity(logmsg)

            # create Content Object packet to send over IP
            msg_contents = 'Interest::' + encap.packet_contents.prefix + '::' + encap.packet_contents.name + '::' + encap.packet_contents.payload

        # unknown message
        else:
            
            # log
            logmsg = settings.IPOVERWLAN_MODULE_NAME + ' : Unknown message received to sent '
            common.log_activity(logmsg)

            # close socket
            s.close()
            return

        # convert string to bytes to send
        byte_msg = msg_contents.encode('UTF-8')
        
        # send the packet
        s.sendto(byte_msg, addr)
        
        # close socket
        s.close()

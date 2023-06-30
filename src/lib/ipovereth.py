# Implementation of a dummy Ethernet module handling multiple
# faces. Each face is uniquely identified by an ID and each 
# will have its corresponding IP next hop information.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 22-jun-2023
#

import sys
from threading import Thread
from threading import Lock
sys.path.append('./lib')
import settings
import common


# setup link module & start the face handler thread
def setup(dispatch):
    
    # start all face handling workers
    for faceindex in range(len(settings.ETH_FACE_IDS)):
        w = Worker(faceindex, dispatch)
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
    def __init__(self, faceindex, dispatch):
        self.faceindex = faceindex
        self.dispatch = dispatch

    def run(self):
        
        # wait for the initial delay
        time.sleep(10)
        
        # create face registration message
        facereg = FaceRegistration()
        facereg.face_id = settings.ETH_FACE_IDS[faceindex]
        facereg.face_module_name = settings.ETH_MODULE_NAME
        facereg.prefix_served = None
        
        # encapsulate registration message
        encap = common.PacketEncap()
        encap.from_direction = common.DirectionType.FROM_LINK
        encap.from_direction_module_name = settings.ETH_MODULE_NAME
        encap.from_face_id = settings.ETH_FACE_IDS[faceindex]
        encap.to_direction = common.DirectionType.TO_CCN
        encap.packet_contents = facereg

        # lock and send message
        with common.system_lock:
            dispatch(encap)
        
        # create socket listen
        pass
        
        while True:

            # do blocking socket read
            pass
            
            # create interest as if it was received from the socket
            interestmsg = Interest()
            interestmsg.prefix = 'ccn://comnets/s2120'
            interestmsg.name = 'temperature'
        
            # encapsulate created message
            encap = common.PacketEncap()
            encap.from_direction = common.DirectionType.FROM_LINK
            encap.from_direction_module_name = settings.ETH_MODULE_NAME
            encap.from_face_id = settings.ETH_FACE_IDS[faceindex]
            encap.to_direction = common.DirectionType.TO_CCN
            encap.packet_contents = interestmsg
        
            # lock and call function to process message
            with common.system_lock:
                dispatch(encap)    

            time.sleep(15)


# handler to send packets out
class Handler:
    
    # function used to send packets to the given face
    def handle_msg(encap):


        # build packet to send out
        msg_contents = ''
        
        # build Interest message
        if type(encap.packet_contents) is Interest:
            # create Interest packet
            msg_contents = ''
            
            # log
            logmsg = settings.ETH_MODULE_NAME + ':Interest received to be sent '
            common.log_activity(logmsg)

        # build ContentObject message
        else if type(encap.packet_contents) is ContentObject:
            # create Interest packet
            msg_contents = ''

            # log
            logmsg = settings.ETH_MODULE_NAME + ':ContentObj received to be sent '
            common.log_activity(logmsg)

        # unknown message
        else:
            # log
            logmsg = settings.ETH_MODULE_NAME + ':Unknown message received to sent '
            common.log_activity(logmsg)
            return

        # find socket details related to sending face
        found = False
        faceindex = None
        for i in range(len(settings.ETH_FACE_IDS)):

            # if face is valid (exists) save it and exit loop
            if settings.ETH_FACE_IDS[i] == encap.to_face_id:
                faceindex = i
                found = True
                break

        # if face found, send message
        if found:
                           
            # get destination address and port information to use
            ipaddress, port = settings.ETH_IP_CONNECTIONS[i].split(':')
            
            # open socket, send the created and close socket
            pass

            # log
            logmsg = settings.ETH_MODULE_NAME + ':Unknown face specified '
            common.log_activity(logmsg)


        # non-existent face given
        else:

            # log
            logmsg = settings.ETH_MODULE_NAME + ':Unknown face specified '
            common.log_activity(logmsg)


        
        # temporary: wait for some time
        time.sleep(5)

# Implementation of the application layer of CCN node
#
# @author: Sowmia Suresh Kumar(sowmia@uni-bremen.de)
# @date: 17-May-2023
#

import time
import settings
import common
from threading import Thread
from threading import Lock
from Internalmsg import InternalMessage
from CCNmsg import InterestMessage

# initialize application layer
def initialize():
    
    print("Initialization of App layer Started")
    
    # Creating Application Face Registration Msg and send to CCN layer
    AppRegistrationMsg = InternalMessage(None,"App Register its face","Fapp")  # this internal msg format: CCNPacket_DataDescription_faceID
    
    
    #lock common queue and insert App Face Registration message for CCN to pop
    with common.ccn_upper_in_lock:
        try:
            common.ccn_upper_in_q.append(AppRegistrationMsg)
            print("Send: App --> App_Registration_Msg --> CCN :", AppRegistrationMsg)
        except:
            pass
    
# start the application threads
def start():
    
    Thread(target=generate_CCN_Interest).start()
    Thread(target=receive_from_ccn).start()


# application thread generate interests (to ccn layer)
def generate_CCN_Interest():
    
    # operate in an endless loop
    while True:
        if "user" in settings.APP_TYPE:       # If chosen User application   
            print("CCN node acts a User")
            
            # Generate Interest packet             
            CCNpacket = InterestMessage(common.msg_type["Interest"],0,0,0,settings.MAX_HOPS_ALLOWED,settings.INTEREST_LIFETIME_sEC,
                                        settings.REQUESTED_SEN_NETW_PREFIX_NAME,
                                        settings.SENSOR_DATA_NAMES,1,00,"Requesting temperature of COMNETS building")
            print("Interest for Temperature data is generated")
            
            # Encapsulate CCN interest msg into Internal msg
            CCNInterestmsg = InternalMessage(CCNpacket,None,"Fapp")
            
            #lock common queue and insert message for CCN to pop
            with common.ccn_upper_in_lock:
                try:
                    common.ccn_upper_in_q.append(CCNInterestmsg)
                    print('Send: App --> User_Interest_msg --> CCN :', CCNInterestmsg)
                except:
                    pass
           
            time.sleep(1000)
        else:
            pass

def generate_CCN_Reflexive_Interest():
    
    while True:
        if "user" in settings.APP_TYPE:
            
            CCNpacket = InterestMessage(common.msg_type["Interest"],0,settings.MAX_HOPS_ALLOWED,
                                        settings.INTEREST_LIFETIME_sEC,settings.REQUESTED_SEN_NETW_PREFIX_NAME,
                                        settings.SENSOR_DATA_NAMES,"none",1,00)
            
            CCNpacket_str = str(CCNpacket)
            CCNInterestmsg = InternalMessage(CCNpacket_str,"Requesting for temperature","Fapp")
            #print(CCNInterestmsg)
            CCNInterest_STR = str(CCNInterestmsg)
            #print(CCNInterest_STR)
             #lock common queue and insert message for epidemic to pop
            with common.ccn_upper_in_lock:
                try:
                    common.ccn_upper_in_q.append(CCNInterest_STR)
                    print('Sending Interest to CCN layer:', CCNInterest_STR)
                except:
                    pass
            time.sleep(settings.INTEREST_LIFETIME_sEC)
        else:
            pass
# application thread to receive content comjects from cc layer
def receive_from_ccn():
#     with common.ccn_lower_in_lock:
#            try:
#                # get message from the queue
#                CO = common.app_lower_in_q.popleft()
                #with common.logging_lock:
                #    common.log_activity('RRS   < link  | ' + msg)
#            except:
    pass


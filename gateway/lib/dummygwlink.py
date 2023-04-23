# Implementation of a dummy link to be used as an 
# example when developing link implementations.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#

import sys
from threading import Thread
from threading import Lock
sys.path.append('./lib')
import settings
import common
from collections import deque

# initialize link layer
def initialize():
    pass

# start link layer activity threads
def start():

    Thread(target=send_msg).start()
    Thread(target=recv_msg).start()


# send queued messages out
def send_msg():
    pass

# receive messages sent by neighbours
def recv_msg():
    pass


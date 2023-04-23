# Implementation of a dummy ccn gateway to be used as an 
# example when developing real ccn forwarders.
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


# initialize RRS layer
def initialize():
    pass

# start the RRS activity threads
def start():

    Thread(target=receive_from_app).start()
    Thread(target=send_data_to_neighbours).start()
    Thread(target=receive_from_link).start()


# get data from application
def receive_from_app():
    pass


# send data periodically to neighbours
def send_data_to_neighbours():
    pass

# receive data from link layer
def receive_from_link():
    pass

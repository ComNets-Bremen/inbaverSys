# Implementation of a dummy ccn forwarder to be used as an 
# example when developing real ccn forwarders.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#

import ucollections
import _thread
import machine
import os
import time
import utime
import common
import settings


# initialize RRS layer
def initialize():
    pass

# start the RRS activity threads
def start():

    _thread.start_new_thread(receive_from_app, ())
    _thread.start_new_thread(send_data_to_neighbours, ())
    _thread.start_new_thread(receive_from_link, ())


# get data from application
def receive_from_app():
    pass


# send data periodically to neighbours
def send_data_to_neighbours():
    pass

# receive data from link layer
def receive_from_link():
    pass

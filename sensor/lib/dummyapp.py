# Implementation of a dummy application to be used as an 
# example when developing applications.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#
import _thread
import machine
import os
import common
import time
import settings

# initialize application layer
def initialize():
    pass


# start the application threads
def start():
    _thread.start_new_thread(generate_data, ())
    _thread.start_new_thread(receive_from_ccn, ())


# application thread generate interests (to ccn layer)
def generate_data():
    pass

# application thread to receive content comjects from cc layer
def receive_from_ccn():
    pass

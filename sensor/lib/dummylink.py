# Implementation of a dummy link to be used as an 
# example when developing link implementations.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#

import pycom
import ucollections
import _thread
import machine
import os
import common
import time
import socket
import utime
import network
import socket
import ubinascii
import settings

# initialize link layer
def initialize():
    pass

# start link layer activity threads
def start():

    _thread.start_new_thread(send_msg, ())
    _thread.start_new_thread(recv_msg, ())
    _thread.start_new_thread(send_neigh_list, ())
    _thread.start_new_thread(send_hello, ())


# send queued messages out
def send_msg():
    pass

# receive messages sent by neighbours
def recv_msg():
    pass

# send the current neighbour list to the fwd layer
def send_neigh_list():
    pass

# send HELLO messeages to inform about being in neighbourhood
def send_hello():
    pass

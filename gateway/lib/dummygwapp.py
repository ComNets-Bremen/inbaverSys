# Implementation of a dummy gateway application to be used as an 
# example when developing applications.
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

# initialize application layer
def initialize():
    pass


# start the application threads
def start():
    Thread(target=generate_data).start()
    Thread(target=receive_from_ccn).start()


# application thread generate interests (to ccn layer)
def generate_data():
    pass

# application thread to receive content comjects from cc layer
def receive_from_ccn():
    pass

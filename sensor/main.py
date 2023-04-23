# A sensor network program that implements the functionality of a content
# centric networking (CCN) sensor node. It has a protocol 3-layer 
# architecture that can be configured to use diffeent protocols. The 3 
# layer are,
#
# - app - application layer
# - ccn - forwarding layer
# - link - link layer
#
# All layer modules and the parameters have to be defined in the
# lib/settings.py module.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2022
#

import pycom
import gc
import os
import _thread
import machine
import time
import common
import settings

# basic initializations
time.sleep(2)
gc.enable()
pycom.heartbeat(False)

# setup the environment
try:

    # load modules of the configured 3-layer protocol stack
    app = __import__(settings.APP_LAYER)
    ccn = __import__(settings.CCN_LAYER)
    link = __import__(settings.LINK_LAYER)

    # initialize common environment
    common.initialize()

    # initialize all layers
    app.initialize()
    ccn.initialize()
    link.initialize()

    # activate all layers
    app.start()
    ccn.start()
    link.start()

    # wait endlessly while the threads do their work
    while True:

        # loop with a pause
        time.sleep(5)

except Exception as e:
    print(e)

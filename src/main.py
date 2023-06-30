# A program that implements a content centric (CCN) node. It
# has a 3-layer protocol architecture, where different modules can
# be configured and loaded to serve different supported specific
# layer supporting modules.
#
# - app - application layer
# - ccn - forwarding layer
# - link - link layer
#
# All layer modules and the parameters have to be defined in the
# lib/settings.py module. Depending on the node type, the settings.py
# must be created by copying the appropriate file as follows.
#
# - settings.node.py
#   for an internet based CCN node
# - settings.sensor.py
#   for a CCN based sensor node
# - settings.gateway.py
#   for a CCN based IoT gateway conntecting a sensor network and the internet
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 22-jun-2023
#

import sys
from threading import Thread
from threading import Lock
sys.path.append('./lib')
import definitions
import settings
import common

# import module references
appmodules = []
ccnmodule = None
linkmodules = []

def main():
    global appmodules
    global ccnmodule
    global linkmodules

    # setup the environment
    try:

        # initialize and setup environment
        common.setup()

        # load & call setup of forwarding module
        ccn = __import__(settings.CCN_LAYER)
        handler = ccn.setup(dispatch)

        # save references for later use
        modinfo = common.ModuleInfo()
        modinfo.module_name = module
        modinfo.module_ref = link
        ccnmodule = modinfo

        # load & setup each link module
        for module in settings.LINK_LAYER:
            # import link module
            link = __import__(module)
            
            # call setup to intialize and start threads
            handler = link.setup(dispatch)

            # save references for later use
            modinfo = common.ModuleInfo()
            modinfo.module_name = module
            modinfo.module_ref = link
            modinfo.face_handler_ref = handler
            linkmodules.append(modinfo)

        # load and setup each application module
        for module in settings.APP_LAYER:
            # import link module
            app = __import__(module)
            
            # call setup to intialize and start threads
            handler = app.setup(dispatch)

            # save references for later use
            modinfo = common.ModuleInfo()
            modinfo.module_name = module
            modinfo.module_ref = app
            modinfo.face_handler_ref = handler
            appmodules.append(modinfo)

        # wait endlessly while the rest of the threads do their work
        while True:

            # loop with a pause
            time.sleep(5)

    except Exception as e:
        print(e)


# All layer handling modules (e.g. eth, tempreader, stdccn) will call 
# dispatch to deliver to their packets to other layer handling 
# modules. The encap must carry information about where to deliver.
def dispatch(encap):


    # CCN module destined packet
    if encap.to_direcion == common.DirectionType.TO_CCN:
        ccnmodule.face_handler_ref.handle_msg(encap)

    # application module destined packet, find from list
    else if encap.to_direcion == common.DirectionType.TO_APP:
        for modinfo in appmodules:
            if encap.to_direction_module_name == modinfo.module_name:
                modinfo.face_handler_ref.handle_msg(encap)

    # link module destined packet, find from list
    else if encap.to_direcion == common.DirectionType.TO_LINK:
        for modinfo in linkmodules:
            if encap.to_direction_module_name == modinfo.module_name:
                modinfo.face_handler_ref.handle_msg(encap)


if __name__ == "__main__":
    main()

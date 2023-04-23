# A program that implements a standard content centric (CCN) gateway. It
# has a 3-layer protocl parchitecture, where different protols can
# be configured for each layer. The 3 layer are,
#
# - app - application layer
# - ccn - forwarding layer
# - link - link layer
#
# All layer modules and the parameters have to be defined in the
# lib/settings.py module.
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


def main():
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


if __name__ == "__main__":
    main()
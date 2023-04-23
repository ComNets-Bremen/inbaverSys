# Holds all the settings used by other modules.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2022
#

# general settings
BROADCAST_ADDRESS = 'FFFF'
MAX_QUEUE_SIZE = 50
MAINTAIN_CONSOLE_LOG = True
MAINTAIN_WRITTEN_LOG = True
LOG_FILE_NAME = '/sd/log.txt'

# app layer settings
APP_LAYER = 'dummyapp'
DATA_GEN_INTERVAL_SEC = 13

# CCN layer settings
CCN_LAYER = 'dummyccn'
CACHE_ITEM_LIMIT = 50

# link layer settings
LINK_LAYER = 'dummylink'
HELLO_INTERVAL_SEC = 5
MISSED_HELLOS = 3
SEND_BLINK_COLOUR = 'blue'
RECV_BLINK_COLOUR = 'green'

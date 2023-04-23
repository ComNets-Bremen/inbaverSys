# Holds all the settings used by other modules.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#

# general settings
MAX_QUEUE_SIZE = 50
MAINTAIN_CONSOLE_LOG = True
MAINTAIN_WRITTEN_LOG = True
LOG_FILE_NAME = 'log.txt'

# app layer settings
APP_LAYER = 'dummygwapp'
DATA_GEN_INTERVAL_SEC = 13

# CCN layer settings
CCN_LAYER = 'dummygwccn'
CACHE_ITEM_LIMIT = 50

# link layer settings
LINK_LAYER = 'dummygwlink'
HELLO_INTERVAL_SEC = 5
MISSED_HELLOS = 3
SEND_BLINK_COLOUR = 'blue'
RECV_BLINK_COLOUR = 'green'


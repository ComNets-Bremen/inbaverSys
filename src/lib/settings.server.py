# Holds all the settings used by other modules.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#


#----- general settings -----
NODE_TYPE = NodeType.SERVER
NODE_ID = 'c1'
NODE_NAME = 'content-server-1 Computer'


# SD card info
SD_CARD = False
SD_MOUNT_PATH = '/sd'

# logging info
LOG_FILE_WRITE = True
LOG_CONSOLE_WRITE = True
LOG_FILE_PATH = './log.txt'

# layer modules
APP_LAYER = ['tempreader', 'humreader']
CCN_LAYER = 'stdccn'
LINK_LAYER = ['ipoverwlan', 'ipovereth']



#----- app layer settings -----

# content server application settings
SERVER_MODULE_NAME = 'server'
SERVER_FACE_ID = 'server'
SERVER_START_DELAY_SEC = 20
SERVER_DOC_REQ_INTERVAL_SEC = 30
SERVER_SEGMENT_REQ_INTERVAL_SEC = 2
SERVER_DATA_REQ_PREFIX = 'ccn://comnets/docs'
SERVER_DATA_NAME_PREFIXES = 'lecture:paper:hackathon'
SERVER_DATA_NAME_SUFFIX_RANGE = '300:900'


#----- CCN layer settings -----


# stdccn forwarder settings
STDCCN_MODULE_NAME = 'stdccn'
STDCCN_CACHE_ITEM_LIMIT = 50


#----- link layer settings -----

# IP over eth link settings
IPOVERETH_MODULE_NAME = 'ipovereth'
IPOVERETH_FACE_IDS = ['eth1']
IPOVERETH_IP_COMM_PROTO = 'UDP'
IPOVERETH_LOCAL_PORTS = [10000]
IPOVERETH_IP_CONNECTIONS = ['10.10.1.1:10000']


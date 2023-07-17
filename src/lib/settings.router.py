# Holds all the settings used by other modules.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#

import common


#----- general settings -----
NODE_TYPE = common.NodeType.ROUTER
NODE_ID = 'r2'
NODE_NAME = 'router-2 Computer'


# SD card info
SD_CARD = False
SD_MOUNT_PATH = '/sd'

# logging info
LOG_FILE_WRITE = True
LOG_CONSOLE_WRITE = True
LOG_FILE_PATH = './log.txt'

# layer modules
APP_LAYER = []
CCN_LAYER = 'stdccn'
LINK_LAYER = ['ipovereth']



#----- app layer settings -----


#----- CCN layer settings -----


# stdccn forwarder settings
STDCCN_MODULE_NAME = 'stdccn'
STDCCN_CACHE_ITEM_LIMIT = 50


#----- link layer settings -----


# IP over eth link settings
IPOVERETH_MODULE_NAME = 'ipovereth'
IPOVERETH_FACE_IDS = ['eth1', 'eth2', 'eth3']
IPOVERETH_IP_COMM_PROTO = 'UDP'
IPOVERETH_LOCAL_PORTS = [10001, 10003, 10002]
IPOVERETH_IP_CONNECTIONS = ['127.0.0.1:9001', '127.0.01:12001', '127.0.01:11000']

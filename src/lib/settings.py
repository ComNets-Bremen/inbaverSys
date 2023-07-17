# Holds all the settings used by other modules.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#

import common


#----- general settings -----
NODE_TYPE = common.NodeType.NODE
NODE_ID = '31FE61'
NODE_NAME = 'node-1 Computer'


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

# temp application settings
TEMPREADER_MODULE_NAME = 'tempreader'
TEMPREADER_FACE_ID = 'tempreader'
TEMPREADER_START_DELAY_SEC = 20
TEMPREADER_DATA_REQ_INTERVAL_SEC = 30
TEMPREADER_DATA_REQ_PREFIX = 'ccn://comnets/s2120'
TEMPREADER_DATA_NAME = 'temperature'


# hum application settings
HUMREADER_MODULE_NAME = 'humreader'
HUMREADER_FACE_ID = 'humreader'
HUMREADER_START_DELAY_SEC = 30
HUMREADER_DATA_REQ_INTERVAL_SEC = 30
HUMREADER_DATA_REQ_PREFIX = 'ccn://comnets/s2120'
HUMREADER_DATA_NAME = 'humidity'


#----- CCN layer settings -----


# stdccn forwarder settings
STDCCN_MODULE_NAME = 'stdccn'
STDCCN_CACHE_ITEM_LIMIT = 50


#----- link layer settings -----

# IP over wlan link settings
IPOVERWLAN_MODULE_NAME = 'ipoverwlan'
IPOVERWLAN_FACE_IDS = ['wlan1', 'wlan2']
IPOVERWLAN_SSID = 'ComNets'
IPOVERWLAN_IP_COMM_PROTO = 'UDP'
IPOVERWLAN_LOCAL_PORTS = [9000, 9001]
IPOVERWLAN_IP_CONNECTIONS = ['127.0.0.1:10000', '127.0.0.1:10001']


# IP over eth link settings
IPOVERETH_MODULE_NAME = 'ipovereth'
IPOVERETH_FACE_IDS = ['eth1', 'eth2']
IPOVERETH_IP_COMM_PROTO = 'UDP'
IPOVERETH_LOCAL_PORTS = [9002, 9003]
IPOVERETH_IP_CONNECTIONS = ['127.0.0.1:10002', '127.0.01:10003']

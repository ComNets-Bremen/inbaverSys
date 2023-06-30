# Holds all the settings used by other modules.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#


#----- general settings -----
NODE_TYPE = NodeType.NODE
NODE_ID = '31FE61'
NODE_NAME = 'Daniel\'s Computer'


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

# wlan link settings
WLAN_MODULE_NAME = 'ipoverwlan'
WLAN_FACE_IDS = ['wlan1', 'wlan2']
WLAN_SSID = 'ComNets'
WLAN_IP_COMM_PROTO = 'UDP'
WLAN_LOCAL_PORTS = [9000, 9001]
WLAN_IP_CONNECTIONS = ['192.168.1.1:9000', '192.168.1.2:9000']


# eth link settings
ETH_MODULE_NAME = 'ipovereth'
ETH_FACE_IDS = ['eth1', 'eth2']
ETH_IP_COMM_PROTO = 'UDP'
ETH_LOCAL_PORTS = [10000, 10001]
ETH_IP_CONNECTIONS = ['10.10.1.1:10000', '10.10.1.2:10000']
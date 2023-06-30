# Holds all the settings used by other modules.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#


#----- general settings -----
NODE_TYPE = NodeType.NODE
NODE_ID = 'DE3CF4'
NODE_NAME = 'EE Gateway'


# SD card info
SD_CARD = False
SD_MOUNT_PATH = '/sd'

# logging info
LOG_FILE_WRITE = True
LOG_CONSOLE_WRITE = True
LOG_FILE_PATH = './log.txt'

# layer modules
APP_LAYER = ['sensorgw']
CCN_LAYER = 'stdccn'
LINK_LAYER = ['wlan', 'lora']



#----- app layer settings -----

# sensor data caching application settings
SENSORGW_FACE_ID = 'iotgwapp'
SENSORGW_CACHE_ITEM_LIMIT = 100




#----- CCN layer settings -----


# stdccn forwarder settings
STDCCN_MODULE_NAME = 'stdccn'
STDCCN_CACHE_ITEM_LIMIT = 50


#----- link layer settings -----

# wlan link settings
WLAN_MODULE_NAME = 'wlan'
WLAN_FACE_IDS = ['wlan1', 'wlan2']
WLAN_SSID = 'ComNets'
WLAN_IP_COMM_PROTO = 'UDP'
WLAN_LOCAL_PORT = 9000
WLAN_IP_CONNECTIONS = ['192.168.1.1:9000', '192.168.1.2:9000']


# lora link settings
LORA_MODULE_NAME = 'lora'
LORA_FACE_IDS = ['lora1']

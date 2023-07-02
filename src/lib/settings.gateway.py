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

# settings of gateway application that stores and responds to sensor data
IOTGWAPP_MODULE_NAME = 'iotgwapp'
IOTGWAPP_FACE_ID = 'iotgwapp'
IOTGWAPP_START_DELAY_SEC = 10
IOTGWAPP_CACHE_ITEM_LIMIT = 100
IOTGWAPP_SERVED_PREFIXES = ['ccn://comnets/s2120']
IOTGWAPP_DATA_HOSTED = ['temperature', 'humidity']
IOTGWAPP_DATA_RANGES = ['16.2:18.5', '78.5:80.5']


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
IPOVERWLAN_IP_CONNECTIONS = ['192.168.1.1:9000', '192.168.1.2:9000']


# lora link settings
LORA_MODULE_NAME = 'lora'
LORA_FACE_IDS = ['lora1']

# Holds all the settings used by other modules.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#


#----- general settings -----
NODE_TYPE = NodeType.NODE
NODE_ID = '13AC4F'
NODE_NAME = 'EE Sensor'


# SD card info
SD_CARD = False
SD_MOUNT_PATH = '/sd'

# logging info
LOG_FILE_WRITE = True
LOG_CONSOLE_WRITE = True
LOG_FILE_PATH = './log.txt'

# layer modules
APP_LAYER = ['tempsensor', 'humsensor']
CCN_LAYER = 'stdccn'
LINK_LAYER = ['lora']



#----- app layer settings -----

# temp application settings
TEMP_FACE_ID = 'tempsensor'
TEMP_DATA_GEN_INTERVAL_SEC = 13


# hum application settings
HUM_FACE_ID = 'humsensor'
HUM_DATA_GEN_INTERVAL_SEC = 13


#----- CCN layer settings -----


# stdccn forwarder settings
STDCCN_MODULE_NAME = 'stdccn'
STDCCN_CACHE_ITEM_LIMIT = 50


#----- link layer settings -----

# lora link settings
LORA_MODULE_NAME = 'lora'
LORA_FACE_IDS = ['lora1']


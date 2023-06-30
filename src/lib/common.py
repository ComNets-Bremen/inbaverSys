# Holds all the common variables and functions used by all the
# other functions.
#
# @author: Asanga Udugama (adu@comnets.uni-bremen.de)
# @date: 23-apr-2023
#

import sys
from threading import Thread
from threading import Lock
sys.path.append('./lib')
import settings
from enum import Enum

# node info
node_id = None
node_long_id = None

# locks
system_lock = None

# SD card variables
sd = None
sd_card_present = False

# initialize and setup
def setup():
    global node_id
    global node_long_id
    global system_lock
    global sd
    global sd_card_present

    # set node info
    node_id = settings.NODE_ID
    node_long_id = settings.NODE_NAME

    # setup global lock
    system_lock = _thread.allocate_lock()
    
    # log start of init
    with system_lock:
        log_activity('initialization started...')

    # mount SD card
    if SD_CARD:
        try:
            sd = machine.SD()
            os.mount(sd, SD_MOUNT_PATH)
            sd_card_present = True

        except:
            pass

    # log completion of init
    with logging_lock:
        log_activity('initialization completed')


# log activity given as string
# IMPORTANT: always call this function after holding common.system_lock
def log_activity(info):
    global node_id

    # build log string
    log_str = str(utime.ticks_ms()) + ' ' + node_id +  ' ' + info

    # print to console
    if settings.LOG_CONSOLE_WRITE:
        print(log_str)

    # if SD card present, write to log
    if sd_card_present and settings.LOG_FILE_WRITE:

        # write to log file
        try:
            logfp = open(settings.LOG_FILE_PATH, mode='a')
            logfp.write(log_str)
            logfp.write('\n')
            logfp.close()
        except:
            print('something wrong with the log file')
            print('could be - wrong path, log full')


# enums for the type of node
class NodeType(Enum):
    NODE, ROUTER, SERVER, IOTGATEWAY, SENSOR = range(1, 6)


# enums for the cross layer direction
class DirectionType(Enum):
    TO_APP, TO_CCN, TO_LINK, FROM_APP, FROM_CCN, FROM_LINK = range(1, 7)


# message encapsulator class to use to pass messages between 
# layers, containing some header information
class PacketEncap:
    def __init__(self):
        self.from_direction = None
        self.from_direction_module_name = None
        self.to_direction = None
        self.to_direction_module_name = None
        self.from_face_id = None
        self.to_face_id = None
        self.packet_contents = None


# holds face handler module info to use to pass packets when they
# need processing
class ModuleInfo:
    def __init__(self):
        self.module_name = None
        self.module_ref = None
        self.face_handler_ref = None


class FaceRegistration:
    def __init__(self):
        self.face_id = None
        self.face_module_name = None
        self.prefix_served = None


class Interest:
    def __init__(self):
        self.prefix = None
        self.name = None


class ContentObject:
    def __init__(self):
        self.prefix = None
        self.name = None
        self.payload = None


#!/usr/bin/python

import struct
import time
import sys
import os
import socket
import subprocess
from resources.gui.app import *
import resources.XboxController as XboxController
from pythonzenity import Warning, Message, Error

#infile_path = ''
#in_file = ''
#FORMAT = 'llHHI'
#EVENT_SIZE = struct.calcsize(FORMAT)
#event = in_file.read(EVENT_SIZE)
laptopbasedir='/home/iainstott/GitRepo/Submersible'
submarinebasedir='/home/pi/Submersible'
hostname=(socket.gethostname())
basedir=''


def setBase():
    if ( hostname == 'Iains-Laptop'):
        basedir=laptopbasedir
    elif ( hostname == 'submarine-pi'):
        basedir=submarinebasedir
    os.chdir(basedir)
    sys.path.append(basedir)
            
if __name__ == "__main__":
    setBase()
    subprocess.Popen('resources/gui/app.py')
    #infile_path = "/dev/input/event2"
    #in_file = open(infile_path, "rb")
    #while event:
        #(tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)
    #if type != 0 or code != 0 or value != 0:
        #print("Event type %u, code %u, value %u at %d.%d" % \
            #(type, code, value, tv_sec, tv_usec))
    #else:
        ## Events with code, type and value == 0 are "separator" events
        #print("===========================================")
        #event = in_file.read(EVENT_SIZE)
    #in_file.close()

#!/usr/bin/python

import sys
import os
import socket
import subprocess
from resources.gui.app import *
import resources.XboxController as Controller
from pythonzenity import Warning, Message, Error
import struct
import time
import sys

FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)
infile_path = "/dev/input/event2"
in_file = open(infile_path, "rb")
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
    
def xBoxController():
    if (hostname == 'submarine-pi' ):
        xboxCont = Controller.XboxController(
            controllerCallBack = None,
            joystickNo = 0,
            deadzone = 0.1,
            scale = 1,
            invertYAxis = False)   
        xboxCont.start()
    else:
        Message(text="Test Environment")
        
if __name__ == "__main__":
    setBase()
    subprocess.Popen('resources/gui/app.py')
    event = in_file.read(EVENT_SIZE)
    while event:
        (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)
        if type != 0 or code != 0 or value != 0:
            print("Event type %u, code %u, value %u at %d.%d" % \
                (type, code, value, tv_sec, tv_usec))
        else:
            print("===========================================")
            event = in_file.read(EVENT_SIZE)
    in_file.close()

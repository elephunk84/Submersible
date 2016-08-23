#!/usr/bin/python

import sys
import os
import socket
import subprocess
from resources.gui.app import *
import resources.XboxController as XboxController
from pythonzenity import Warning, Message, Error
from evdev import InputDevice, categorize

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
        xboxCont = XboxController.XboxController(
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
    xBoxController()
    subprocess.Popen('resources/gui/app.py')

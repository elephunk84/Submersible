#!/usr/bin/python3

import struct
import time
import sys
import os
import socket
import subprocess
import resources.gui.app as app
import resources.XboxController as XboxController
from pythonzenity import Warning, Message, Error
    
laptopbasedir='/home/iainstott/GitRepo/Submersible'
submarinebasedir='/home/pi/Submersible'
hostname=(socket.gethostname())
basedir=''

def myCallBack(controlId, value):
    print "Control id = {}, Value = {}".format(controlId, value)

xboxCont = XboxController.XboxController(
    controllerCallBack = myCallBack)
    
def setBase():
    if ( hostname == 'Iains-Laptop'):
        basedir=laptopbasedir
    elif ( hostname == 'submarine-pi'):
        basedir=submarinebasedir
    os.chdir(basedir)
    sys.path.append(basedir)
            
if __name__ == "__main__":
    setBase()
    xboxCont.start()
    app.showGUI()
    

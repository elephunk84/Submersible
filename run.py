#!/usr/bin/python

import struct
import time
import sys
import os
import socket
import subprocess
import thread
import resources.gui.app as gui
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
    thread.start_new_thread( gui.showGUI )
    xboxCont.start()

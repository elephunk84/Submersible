#!/usr/bin/python

import sys
import os
import socket
import subprocess
from resources.gui.app import *
from pythonzenity import Warning, Message, Error

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
        try:
            subprocess.call('/usr/bin/lxterminal')
        except subprocess.CalledProcessError as e:
            Error(text=e.output())
    else:
        Message(text="Test Environment")
        
if __name__ == "__main__":
    setBase()
    xBoxController()
    subprocess.Popen('resources/gui/app.py')

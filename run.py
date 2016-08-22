#!/usr/bin/python

import os
import socket
import subprocess
from resources.gui.app import *
from pythonzenity import Warning

laptopbasedir='/home/iainstott/GitRepo/Submersible'
submarinebasedir='/home/pi/Submersible'

def setBase():
    hostname=(socket.gethostname())
    if ( hostname == 'Iains-Laptop'):
        basedir=laptopbasedir
    elif ( hostname == 'submarine-pi'):
        basedir=submarinebasedir
    os.chdir(basedir)
    
def xBoxController():
    if (hostname == 'submarine-pi' ):
        try:
            subprocess.call("'/usr/bin/lxterminal' './resources/XboxController.py'")
        except subprocess.CalledProcessError as e:
            print e.output
    else:
        pass
        
if __name__ == "__main__":
    setBase()
    subprocess.Popen('./resources/gui/app.py')

#!/usr/bin/python

import os
import socket
import subprocess
from resources.gui.app import *
from pythonzenity import Warning

hostname=(socket.gethostname())
if ( hostname == 'Iains-Laptop'):
    basedir='/home/iainstott/GitRepo/Submersible'
elif ( hostname == 'submarine-pi'):
    basedir='/home/pi/Submersible'
    
    
if __name__ == "__main__":
    os.chdir(basedir)
    subprocess.Popen('./resources/gui/app.py')

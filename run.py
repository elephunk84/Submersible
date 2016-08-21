#!/usr/bin/python
from resources.gui.app import *
import resources.XboxController

xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)
    
if __name__ == "__main__":
    xboxCont.start()
    gui()

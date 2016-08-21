#!/usr/bin/python
###
from resources.gui.app import *
from pythonzenity import Warning
import resources.XboxController
import pygame
import sys

try:
    xboxCont = resources.XboxController.XboxController(controllerCallBack = None, joystickNo = 0, deadzone = 0.1, scale = 1, invertYAxis = False)
    xboxCont.start()
    pass
except pygame.error:
    e = sys.exc_info()[1]
    Warning(text="PyGame Error: %s" % e)
    pass
    
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    MainWindow = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(MainWindow)
    MainWindow.Show()
    app.MainLoop()
    

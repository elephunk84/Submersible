#!/usr/bin/python
###
from resources.gui.app import *
import resources.XboxController
import pygame

try:
    xboxCont = resources.XboxController.XboxController(controllerCallBack = None, deadzone = 0.1, scale = 1, invertYAxis = False)
except pygame.error:
    print('error')
    
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    MainWindow = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(MainWindow)
    MainWindow.Show()
    app.MainLoop()
    

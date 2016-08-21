#!/usr/bin/python
###
from resources.gui.app import *
import resources.XboxController

xboxCont = resources.XboxController.XboxController(controllerCallBack = None, joystickNo = 1, deadzone = 0.1, scale = 1, invertYAxis = False)
    
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    MainWindow = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(MainWindow)
    MainWindow.Show()
    app.MainLoop()
    xboxCont.start()
    

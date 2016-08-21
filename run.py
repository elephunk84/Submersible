#!/usr/bin/python
from resources.gui.app import *
import resources.XboxController

xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)
xboxCont.start()
    
if __name__ == "__main__":
    gettext.install("app")
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Sub_Control = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(Sub_Control)
    Sub_Control.Show()
    app.MainLoop()

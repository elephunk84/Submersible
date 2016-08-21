#!/usr/bin/python
###
from resources.gui.app import *
from pythonzenity import Warning
import resources.XboxController
import sys
    
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.App()
    wx.InitAllImageHandlers()
    MainWindow = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(MainWindow)
    MainWindow.Show()
    app.MainLoop()
    

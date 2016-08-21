#!/usr/bin/python
from resources.gui.app import *

if __name__ == "__main__":
    gettext.install("app")
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Sub_Control = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(Sub_Control)
    Sub_Control.Show()
    app.MainLoop()


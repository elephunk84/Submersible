#!/usr/bin/python
###
from resources.gui.app import *
from pythonzenity import Warning
import resources.XboxController
import pygame
import sys

def mainWindow():
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    MainWindow = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(MainWindow)
    MainWindow.Show()
    app.MainLoop()
    
if __name__ == "__main__":
    mainWindow()

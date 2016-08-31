#!/usr/bin/python

import struct
import time
import sys
import os
import socket
import subprocess
import threading
import resources.XboxController as XboxController
from pythonzenity import Warning, Message, Error
import wx
import gettext
    
laptopbasedir = '/home/iainstott/GitRepo/Submersible'
submarinebasedir = '/home/pi/Submersible'
hostname = (socket.gethostname())
basedir = ''
threads = []

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.MainWindow_menubar = wx.MenuBar()
        self.sysMenu = wx.Menu()
        self.sysMenu.Append(wx.ID_ANY, _("item"), "", wx.ITEM_NORMAL)
        self.sysMenu.Append(wx.ID_ANY, _("item"), "", wx.ITEM_NORMAL)
        self.sysMenu.AppendSeparator()
        self.shutdownButton = wx.MenuItem(self.sysMenu, wx.ID_ANY, _("Shutdown Dialog"), "", wx.ITEM_NORMAL)
        self.sysMenu.AppendItem(self.shutdownButton)
        self.MainWindow_menubar.Append(self.sysMenu, _("System Menu"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Restart GUI"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Reset Sub Control"), "", wx.ITEM_NORMAL)
        self.MainWindow_menubar.Append(wxglade_tmp_menu, _("Submersible Menu"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Network Manager"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Create Hotspot"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Disable WiFi"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_ANY, _("WiFi Hacking"), "", wx.ITEM_NORMAL)
        self.MainWindow_menubar.Append(wxglade_tmp_menu, _("WiFi Menu"))
        self.SetMenuBar(self.MainWindow_menubar)
        # Menu Bar end
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
        self.mainPane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.button_navLights = wx.Button(self.mainPane, wx.ID_ANY, _("Nav Lights"))
        self.button_fullBeam = wx.Button(self.mainPane, wx.ID_ANY, _("Full Beam"))
        self.button_Light1 = wx.ToggleButton(self.mainPane, wx.ID_ANY, _("Light 1"))
        self.button_Light2 = wx.ToggleButton(self.mainPane, wx.ID_ANY, _("Light 2"))
        self.button_Light3 = wx.ToggleButton(self.mainPane, wx.ID_ANY, _("Light 3"))
        self.button_Light4 = wx.ToggleButton(self.mainPane, wx.ID_ANY, _("Light 4"))
        self.button_camLights = wx.ToggleButton(self.mainPane, wx.ID_ANY, _("Cam LED"))
        self.button_Camera = wx.ToggleButton(self.mainPane, wx.ID_ANY, _("Camera"))
        self.label_1 = wx.StaticText(self.mainPane, wx.ID_ANY, _("Motor Power"), style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.slider_3 = wx.Slider(self.mainPane, wx.ID_ANY, 0, 0, 10)
        self.label_2 = wx.StaticText(self.mainPane, wx.ID_ANY, _("LED Power"), style=wx.ALIGN_RIGHT | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.slider_4 = wx.Slider(self.mainPane, wx.ID_ANY, 0, 0, 10)
        self.label_3 = wx.StaticText(self.mainPane, wx.ID_ANY, _("Cam LED Power"), style=wx.ALIGN_RIGHT | wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)
        self.slider_5 = wx.Slider(self.mainPane, wx.ID_ANY, 0, 0, 10)
        self.tree_ctrl_1 = wx.TreeCtrl(self.mainPane, wx.ID_ANY, style=wx.TR_HAS_BUTTONS | wx.TR_DEFAULT_STYLE | wx.SUNKEN_BORDER)
        self.settingsPane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.statusPane = wx.Panel(self.notebook_1, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("Sub Control - Main Window"))
        self.SetSize((800, 600))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_2.Add(self.button_navLights, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.button_fullBeam, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.button_Light1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.button_Light2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.button_Light3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.button_Light4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.button_camLights, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.button_Camera, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(grid_sizer_2, 1, wx.TOP | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.slider_3, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add(self.label_2, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(self.slider_4, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_7.Add(self.label_3, 0, wx.EXPAND | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add(self.slider_5, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_3.Add(self.tree_ctrl_1, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_2.Add((200, 20), 0, 0, 0)
        sizer_2.Add((410, 20), 0, 0, 0)
        self.mainPane.SetSizer(sizer_2)
        self.notebook_1.AddPage(self.mainPane, _("Main"))
        self.notebook_1.AddPage(self.settingsPane, _("Settings"))
        self.notebook_1.AddPage(self.statusPane, _("Status"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class Main_menu(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Main_menu.__init__
        wx.MenuBar.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Main_menu.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Main_menu.__do_layout
        pass
        # end wxGlade

def showGUI():
    gettext.install("app") # replace with the appropriate catalog name
    app = wx.App(0)
    MainWindow = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(MainWindow)
    MainWindow.Show()
    app.MainLoop()

def myCallBack(controlId, value):
    print "Control id = {}, Value = {}".format(controlId, value)

xboxCont = XboxController.XboxController(
    controllerCallBack = myCallBack)
    
def setBase():
    if ( hostname == 'Iains-Laptop'):
        basedir=laptopbasedir
    elif ( hostname == 'submarine-pi'):
        basedir=submarinebasedir
    os.chdir(basedir)
    sys.path.append(basedir)
            
if __name__ == "__main__":
    setBase()
    xboxCont.start()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Sun Aug 21 12:38:38 2016
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
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
        self.slider_1 = wx.Slider(self.mainPane, wx.ID_ANY, 75, 0, 100, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.settingsPane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.statusPane = wx.Panel(self.notebook_1, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("Main Window"))
        self.SetSize((800, 600))
        self.slider_1.SetToolTipString(_("LED Brightness"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
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
        sizer_3.Add(self.slider_1, 0, wx.TOP | wx.EXPAND, 0)
        sizer_3.Add((20, 100), 0, 0, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
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

# end of class Main_menu
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    Sub_Control = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(Sub_Control)
    Sub_Control.Show()
    app.MainLoop()
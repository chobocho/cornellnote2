import wx
from simpleguipanel import *
from simpleguimenu import * 

class SimpleGuiFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(SimpleGuiFrame, self).__init__(*args, **kw)
        self.panel = SimpleGuiPanel(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self._addMenubar()

    def _addMenubar(self):
        self.menu = SimpleGuiMenu(self)

    def OnSave(self, event):
        self.panel.OnSave()

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        msg = 'Simeple GUI Template V0.1\nhttp://chobocho.com'
        title = 'About'
        wx.MessageBox(msg, title, wx.OK | wx.ICON_INFORMATION)

    def OnClear(self, event):
        self.panel.OnClear()

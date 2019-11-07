import wx
from simpleguipanel import *
from simpleguimenu import * 

class SimpleGuiFrame(wx.Frame):
    def __init__(self, *args, version, **kw):
        super(SimpleGuiFrame, self).__init__(*args, title=version, **kw)
        self.panel = SimpleGuiPanel(self)
        self.version = version
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self._addMenubar()

    def _addMenubar(self):
        self.menu = SimpleGuiMenu(self)

    def OnLoad(self, event):
        self.panel.OnLoad()

    def OnSave(self, event):
        self.panel.OnSave()

    def OnQuit(self, event):
        self.Close()

    def OnCopyToClipboard(self, event):
        self.panel.OnCopyToClipboard()

    def OnClear(self, event):
        self.panel.OnClear()

    def OnAbout(self, event):
        msg = self.version + '\nhttp://chobocho.com'
        title = 'About'
        wx.MessageBox(msg, title, wx.OK | wx.ICON_INFORMATION)
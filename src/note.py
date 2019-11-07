import wx
from simpleguiframe import *

SW_TITLE = "Cornell note V0.1105SK2"
WINDOW_W_SIZE = 720
WINDOW_H_SIZE = 800

def main(): 
    app = wx.App()
    frm = SimpleGuiFrame(None, version=SW_TITLE, size=(WINDOW_W_SIZE,WINDOW_H_SIZE))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
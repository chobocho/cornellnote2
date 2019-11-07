import wx
from filedrop import *
from filemanager import *
import random

WINDOW_SIZE = 720
WINDOW_H_SIZE = 520

class SimpleGuiPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(SimpleGuiPanel, self).__init__(*args, **kw)
        filedrop = FileDrop(self)
        self.SetDropTarget(filedrop)
        self._initUi()
        self.SetAutoLayout(True)


    def _initUi(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        ##
        filenameBox = wx.BoxSizer(wx.HORIZONTAL)
        self.lblFileName = wx.StaticText(self, style = wx.ALIGN_CENTRE_HORIZONTAL,label="FileName", size=(70,30))
        self.lblFileName.SetBackgroundColour(wx.Colour(255, 255, 204))
        filenameBox.Add(self.lblFileName, 0, wx.EXPAND, 1)

        self.filename = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, size=(WINDOW_SIZE-70,30))
        self.filename.SetValue("")
        self.filename.SetBackgroundColour(wx.Colour(255, 255, 204))
        filenameBox.Add(self.filename, 1, wx.EXPAND, 1)
        sizer.Add(filenameBox, 0, wx.EXPAND, 1)

        ##
        titleBox = wx.BoxSizer(wx.HORIZONTAL)
        self.title = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER|wx.TE_MULTILINE, size=(WINDOW_SIZE,100))
        self.title.SetValue("")
        self.title.SetBackgroundColour(wx.Colour(255, 255, 204))
        titleBox.Add(self.title, 1, wx.EXPAND, 1)
        sizer.Add(titleBox, 0, wx.EXPAND, 1)
        ##
        memoBox = wx.BoxSizer(wx.HORIZONTAL)
        self.keyword = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER|wx.TE_MULTILINE, size=(200,WINDOW_H_SIZE))
        self.keyword.SetValue("")
        self.keyword.SetBackgroundColour(wx.Colour(255, 255, 204))
        memoBox.Add(self.keyword, 0, wx.EXPAND, 1)

        self.memo = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER|wx.TE_MULTILINE, size=(WINDOW_SIZE-200,WINDOW_H_SIZE))
        self.memo.SetValue("")
        self.memo.SetBackgroundColour(wx.Colour(255, 255, 204))
        memoBox.Add(self.memo, 1, wx.EXPAND, 1)
        sizer.Add(memoBox, 1, wx.EXPAND, 1)
        ##
        self.summary = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER|wx.TE_MULTILINE, size=(WINDOW_SIZE,100))
        self.summary.SetValue("")
        self.summary.SetBackgroundColour(wx.Colour(255, 255, 204))
        sizer.Add(self.summary, 0, wx.EXPAND, 1)
        self.SetSizer(sizer)

        self.UiList = [self.title, self.keyword, self.memo, self.summary]

    def OnCallback(self, filelist):
        if (".json" in filelist[0].lower()) == False:
            return

        memo = self.OnLoad(filelist[0])
        self.filename.SetValue(filelist[0])
        self._UpdateNote(memo)

    def _UpdateNote(self, data):
        idx = 0
        for text in self.UiList:
            text.SetValue(data[idx])
            idx += 1

    def OnCopyToClipboard(self):
        header = ['#Filename\n', '\n\n#Title\n', '\n\n#Summary\n', '\n\n#Note\n', '\n\n#Keyword\n']
        memo = []
        memo.append(header[0] + self.filename.GetValue())
        memo.append(header[1] + self.title.GetValue())
        memo.append(header[2] + self.summary.GetValue())
        memo.append(header[3] + self.memo.GetValue())
        memo.append(header[4] + self.keyword.GetValue())

        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject("\n".join(memo)))
            wx.TheClipboard.Close()

    def OnClear(self):
        for text in self.UiList:
            text.SetValue("")

    def OnLoad(self, filename_=""):
        print("OnLoad")
        if len(filename_) > 0:
            fm = FileManager()
            return fm.OnLoad(filename_)

        filename = ""
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="*.json",
            style=wx.FD_OPEN | 
                  #wx.FD_MULTIPLE |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
            )

        if dlg.ShowModal() == wx.ID_OK:
            print("ShwoModal")
            filename = dlg.GetPath()
        dlg.Destroy()

        if len(filename) > 0:
            fm = FileManager()
            memo = fm.OnLoad(filename)
            self.filename.SetValue(filename)
            self._UpdateNote(memo)
        return []

    def OnSave(self):
        print("OnSave")
        fm = FileManager()
        filename = self.filename.GetValue()
        if len(filename) == 0:
            filename = "untitle" + str(random.randrange(100,1000)) + ".json"
        if (".json" in filename.lower()) == False:
            filename += ".json"
        memo = []
        
        for text in self.UiList:
            memo.append(text.GetValue())
        print(filename)
        fm.OnSave(filename, memo)


import wx

class SimpleGuiMenu():
    def __init__(self, parent):
        self.parent = parent
        self._addMenubar()

    def _addMenubar(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        saveItemId = wx.NewId()
        saveItem = fileMenu.Append(saveItemId, 'Save', 'Save')
        self.parent.Bind(wx.EVT_MENU, self.parent.OnSave, saveItem)

        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit App')
        self.parent.Bind(wx.EVT_MENU, self.parent.OnQuit, fileItem)
        menubar.Append(fileMenu, '&File')

        noteMenu = wx.Menu()
        clearItemId = wx.NewId()
        clearItem = noteMenu.Append(clearItemId, 'Clear', 'Clear')
        self.parent.Bind(wx.EVT_MENU, self.parent.OnClear, clearItem)
        menubar.Append(noteMenu, '&Note')


        helpMenu = wx.Menu()
        aboutItemId = wx.NewId()
        aboutItem = helpMenu.Append(aboutItemId, 'About', 'About')
        self.parent.Bind(wx.EVT_MENU, self.parent.OnAbout, aboutItem)
        menubar.Append(helpMenu, '&Help')

        self.parent.SetMenuBar(menubar)

import wx
import pygame


class WindowFunction(wx.Frame):

    def __init__(self, parent, title):
        super(WindowFunction, self).__init__(parent, title=title,
                                             size=(500, 700))

        self.file_path = None
        self.Centre()
        # self.InitUI()
        # pnl = wx.Panel(self)
        # closeButton = wx.Button(pnl, label='Choose file...', pos=(20, 20))

        self.fileNameLabel = None
        self.fileName = None
        # self.file_path = None

        # pnl = wx.Panel(self)

        self.chooseButton = wx.Button(self, label='Choose file...', pos=(20, 20))
        self.playButton = wx.Button(self, label='Play', pos=(250, 20))
        self.stopButton = wx.Button(self, label='Stop', pos=(350, 20))

        # font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'microsoft yahei ui')
        # audioNameText = wx.StaticText(self, label=self.txt1, pos=(150, 25))
        # audioNameText.SetFont(font)

        # # vbox.Add(st1, flag=wx.ALL, border=15)
        # #
        # # pnl.SetSizer(vbox)
        #
        # # self.SetTitle('Bittersweet')
        # # self.Centre()
        #
        self.chooseButton.Bind(wx.EVT_BUTTON, self.ChooseFile)
        # self.playButton.Bind(wx.EVT_BUTTON, self.PlayFunction(self.file_path))
        # self.stopButton.Bind(wx.EVT_BUTTON, self.StopFunction())

    # def StopFunction(self):
    #     pygame.mixer.music.pause()
    #
    # def PlayFunction(self, file_path):
    #     pygame.mixer.init(22050, -16, 2, 2048)
    #     pygame.mixer.music.load(file_path)
    #     pygame.mixer.music.play()
    #
    # def PlayAudio(self, e):
    #     pnl = wx.Panel(self)
    #     font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'microsoft yahei ui')
    #     st1 = wx.StaticText(pnl, label=self.file_path, pos=(150, 25))
    #     st1.SetFont(font)
    #
    #     playButton = wx.Button(pnl, label='Play Audio', pos=(100, 20))
    #     playButton.Bind(wx.EVT_BUTTON, self.PlayFunction(self.file_path))
    #
    def ChooseFile(self, e):
        with wx.FileDialog(self, "Open mp3 file", wildcard="mp3 files (*.mp3)|*.mp3",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.file_path = fileDialog.GetPath()
            self.fileName = self.file_path.rsplit("/", 1)
            self.fileNameLabel = wx.StaticText(self, label=self.fileName[1], pos=(150, 25))
    #
    #     # self.PlayAudio(wx.EVT_BUTTON, file_path)
    #
    #     # pnl = wx.Panel(self)
    #     # st1 = wx.StaticText(pnl, label=file_path, pos=(150, 25))
    #     # st1.SetFont(font=wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'microsoft yahei ui'))

    # def PlayAudio(self, e):
    #     pnl = wx.Panel(self)
    #     font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, 'microsoft yahei ui')
    #     st1 = wx.StaticText(pnl, label=self.file_path, pos=(150, 25))
    #     st1.SetFont(font)
    #
    #     playButton = wx.Button(pnl, label='Play Audio', pos=(100, 20))
    #     playButton.Bind(wx.EVT_BUTTON, self.PlayFunction(self.file_path))



def main():
    app = wx.App()
    ex = WindowFunction(None, title='Audio Import')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

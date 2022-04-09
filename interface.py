import wx
import pygame


class WindowFunction(wx.Frame):

    def __init__(self, parent, title):
        super(WindowFunction, self).__init__(parent, title=title,
                                             size=(500, 700))

        self.file_path = ""
        self.fileNameLabel = None
        self.fileName = None
        self.Centre()

        self.chooseButton = wx.Button(self, label='Choose file...', pos=(20, 20))
        self.playButton = wx.Button(self, label='Play', pos=(20, 50))
        self.stopButton = wx.Button(self, label='Stop', pos=(20, 80))
        self.errorWindow = wx.Frame(self, title="Error", size=(300, 300))

        self.chooseButton.Bind(wx.EVT_BUTTON, self.ChooseFile)
        self.playButton.Bind(wx.EVT_BUTTON, self.PlayFunction)
        self.stopButton.Bind(wx.EVT_BUTTON, self.StopFunction)

    def ChooseFile(self, e):
        with wx.FileDialog(self, "Open mp3 file", wildcard="mp3 files (*.mp3)|*.mp3",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            self.file_path = fileDialog.GetPath()
            self.fileName = self.file_path.rsplit("/", 1)
            self.fileNameLabel = wx.StaticText(self, label=self.fileName[1], pos=(140, 20))

    def PlayFunction(self, e):
        if self.file_path == "":
            toastTone = wx.MessageDialog(None, "Please Choose a mp3 file!", "Error", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastTone.ShowModal() == wx.ID_YES:
                toastTone.Destroy()
        else:
            pygame.mixer.init(22050, -16, 2, 2048)
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def StopFunction(self, e):
        if self.file_path == "":
            toastTone = wx.MessageDialog(None, "Please Choose a mp3 file!", "Error", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if toastTone.ShowModal() == wx.ID_YES:
                toastTone.Destroy()
        else:
            pygame.mixer.music.pause()


def main():
    app = wx.App()
    ex = WindowFunction(None, title='Audio Import')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

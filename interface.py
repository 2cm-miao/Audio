from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from moviepy.editor import *
import sys
import os
import matplotlib.pyplot as plt
import librosa.display
import imageio_ffmpeg


class WindowFunction(QMainWindow):

    def __init__(self, parent=None):
        self.fileName = ''

        super(WindowFunction, self).__init__(parent)
        self.setWindowTitle("Video Player")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Create open file action
        openAction = QAction('&Open File', self)
        openAction.triggered.connect(self.openFile)

        # Create spectrogram showing action
        soundTrackSepctrogramAction = QAction('Sepctrogram', self)
        soundTrackSepctrogramAction.triggered.connect(self.spectrogramProcess)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(soundTrackSepctrogramAction)

        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        # self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

    def openFile(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Open File",
                                                       QDir.homePath())

        if self.fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(self.fileName)))
            self.playButton.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

    def spectrogramProcess(self):
        video = VideoFileClip(self.fileName)
        audio = video.audio
        fileBasename = os.path.splitext(self.fileName)[0]
        audio.write_audiofile(fileBasename + '.mp3')

        x, sr = librosa.load(self.fileName, sr=16000)
        spectrogram = librosa.amplitude_to_db(librosa.stft(x))
        librosa.display.specshow(spectrogram, y_axis='log')
        plt.colorbar(format='%+2.0f dB')
        plt.title('spectrogram')
        plt.xlabel('time(second)')
        plt.ylabel('Hertz(Hz)')
        plt.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = WindowFunction()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())

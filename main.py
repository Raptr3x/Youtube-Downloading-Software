import sys, youtube_dl
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog

#https://github.com/rg3/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312
# 'format': '137/136/135...'
# 137: 1080p
# 136: 720p
# 135: 480p
# 134: 360p
# 133: 240p

qtCreatorFile = "YDS.ui"  #ime fajla ubaci ovde

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.button_download.clicked.connect(self.download)
        self.button_destination.clicked.connect(self.destination)

    def download(self):
        self.link = self.edit_link.text()
        self.checkFormat()

        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([self.link])

    def checkFormat(self):
        if self.comboBox.currentText() == "*.mp3":
            print('sound')
            self.mp3()
        elif self.comboBox.currentText() == "*.mp4":
            print('video')
            self.mp4()

    def destination(self):
        self.downloadDir = str(QFileDialog.getExistingDirectory(self, "Select Download Directory"))




#**************FILE FORMATS****************************FILE FORMATS*******************************FILE FORMATS*****************
    def mp3(self):
        self.ydl_opts = {
        'outtmpl':self.downloadDir,
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }]}
    def mp4(self):
        self.ydl_opts = {
        'outtmpl':self.downloadDir,
        'format':'mp4'
        }



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

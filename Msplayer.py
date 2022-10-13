# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Music.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 893)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 170, 981, 521))
        self.frame.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Volume = QtWidgets.QSlider(self.frame)
        self.Volume.setGeometry(QtCore.QRect(40, 450, 891, 51))
        self.Volume.setOrientation(QtCore.Qt.Horizontal)
        self.Volume.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Volume.setObjectName("Volume")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(590, 40, 331, 311))
        self.textBrowser.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(130, 46, 321, 81))
        self.textBrowser_2.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_3.setGeometry(QtCore.QRect(70, 166, 461, 81))
        self.textBrowser_3.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.Previous = QtWidgets.QPushButton(self.frame)
        self.Previous.setGeometry(QtCore.QRect(60, 270, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        font.setItalic(False)
        self.Previous.setFont(font)
        self.Previous.setStyleSheet("background-color: rgb(255, 159, 25);\n"
"image: url(:/pic/pngtree-cartoon-play-button-icon-download-image_1196877-removebg-preview.png);")
        self.Previous.setText("")
        self.Previous.setObjectName("Previous")
        self.PlayPause = QtWidgets.QPushButton(self.frame)
        self.PlayPause.setGeometry(QtCore.QRect(240, 270, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(7)
        font.setItalic(False)
        self.PlayPause.setFont(font)
        self.PlayPause.setStyleSheet("background-color: rgb(255, 159, 25);\n"
"image: url(:/pic/play.png);")
        self.PlayPause.setText("")
        self.PlayPause.setObjectName("PlayPause")
        self.Skip = QtWidgets.QPushButton(self.frame)
        self.Skip.setGeometry(QtCore.QRect(350, 270, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        font.setItalic(False)
        self.Skip.setFont(font)
        self.Skip.setStyleSheet("background-color: rgb(255, 159, 25);\n"
"image: url(:/pic/right-removebg-preview.png);")
        self.Skip.setText("")
        self.Skip.setObjectName("Skip")
        self.Add = QtWidgets.QPushButton(self.frame)
        self.Add.setGeometry(QtCore.QRect(570, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.Add.setFont(font)
        self.Add.setStyleSheet("background-color: rgb(255, 159, 25);\n"
"image: url(:/pic/add-create-new-plus-icon-20-removebg-preview.png);")
        self.Add.setText("")
        self.Add.setObjectName("Add")
        self.Remove = QtWidgets.QPushButton(self.frame)
        self.Remove.setGeometry(QtCore.QRect(700, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.Remove.setFont(font)
        self.Remove.setStyleSheet("background-color: rgb(255, 159, 25);\n"
"image: url(:/pic/minus-removebg-preview.png);")
        self.Remove.setText("")
        self.Remove.setObjectName("Remove")
        self.Clear = QtWidgets.QPushButton(self.frame)
        self.Clear.setGeometry(QtCore.QRect(820, 380, 102, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.Clear.setFont(font)
        self.Clear.setStyleSheet("background-color: rgb(255, 159, 25);\n"
"image: url(:/pic/trash-can-icon-15-removebg-preview.png);")
        self.Clear.setText("")
        self.Clear.setObjectName("Clear")
        self.Progress = QtWidgets.QProgressBar(self.frame)
        self.Progress.setGeometry(QtCore.QRect(50, 370, 481, 31))
        self.Progress.setProperty("value", 0)
        self.Progress.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Progress.setTextVisible(False)
        self.Progress.setInvertedAppearance(False)
        self.Progress.setObjectName("Progress")
        self.ListSong = QtWidgets.QTextBrowser(self.frame)
        self.ListSong.setGeometry(QtCore.QRect(580, 50, 331, 311))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.ListSong.setFont(font)
        self.ListSong.setStyleSheet("background-color: rgb(255, 187, 103);")
        self.ListSong.setObjectName("ListSong")
        self.ArtistName = QtWidgets.QTextBrowser(self.frame)
        self.ArtistName.setGeometry(QtCore.QRect(120, 50, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.ArtistName.setFont(font)
        self.ArtistName.setStyleSheet("background-color: rgb(255, 187, 103);")
        self.ArtistName.setObjectName("ArtistName")
        self.SongName = QtWidgets.QTextBrowser(self.frame)
        self.SongName.setGeometry(QtCore.QRect(60, 170, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(17)
        self.SongName.setFont(font)
        self.SongName.setStyleSheet("background-color: rgb(255, 187, 103);")
        self.SongName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SongName.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.SongName.setObjectName("SongName")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(60, 270, 171, 71))
        self.plainTextEdit_7.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(240, 270, 101, 71))
        self.plainTextEdit_8.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(350, 270, 171, 71))
        self.plainTextEdit_9.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(570, 379, 117, 31))
        self.graphicsView.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_2.setGeometry(QtCore.QRect(700, 379, 107, 31))
        self.graphicsView_2.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_3.setGeometry(QtCore.QRect(820, 379, 108, 31))
        self.graphicsView_3.setStyleSheet("background-color: rgb(212, 103, 14);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_4.setGeometry(QtCore.QRect(60, 70, 41, 41))
        self.graphicsView_4.setStyleSheet("background-color: rgb(234, 0, 0);\n"
"border-radius: 20px;")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView_5.setGeometry(QtCore.QRect(70, 80, 22, 21))
        self.graphicsView_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 30, 3, 450))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(960, 30, 3, 450))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.graphicsView_3.raise_()
        self.graphicsView_2.raise_()
        self.graphicsView.raise_()
        self.plainTextEdit_9.raise_()
        self.plainTextEdit_8.raise_()
        self.plainTextEdit_7.raise_()
        self.Volume.raise_()
        self.Previous.raise_()
        self.PlayPause.raise_()
        self.Skip.raise_()
        self.Add.raise_()
        self.Remove.raise_()
        self.Clear.raise_()
        self.ListSong.raise_()
        self.ArtistName.raise_()
        self.SongName.raise_()
        self.graphicsView_4.raise_()
        self.graphicsView_5.raise_()
        self.Progress.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_6.setGeometry(QtCore.QRect(150, 160, 981, 521))
        self.graphicsView_6.setStyleSheet("background-color: rgb(217, 118, 60);\n"
"border-radius: 15px;")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_7.setGeometry(QtCore.QRect(160, 150, 981, 520))
        self.graphicsView_7.setStyleSheet("background-color: rgb(255, 157, 38);\n"
"border-radius: 15px;")
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setGeometry(QtCore.QRect(170, 140, 980, 520))
        self.graphicsView_8.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"border-radius: 15px;")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.graphicsView_8.raise_()
        self.graphicsView_7.raise_()
        self.graphicsView_6.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1273, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
                
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 663)
        MainWindow.setStyleSheet("background-color: rgb(255, 164, 128);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Maindish = QtWidgets.QPushButton(self.centralwidget)
        self.Maindish.setGeometry(QtCore.QRect(100, 110, 261, 81))
        self.Maindish.setStyleSheet("background-color: rgb(255, 167, 161);\n"
"image: url(:/pic/fd80ecec48eba2a9adb76e4133905879.png);\n"
"border-radius: 15px;")
        self.Maindish.setText("")
        self.Maindish.setObjectName("Maindish")
        self.Apptize = QtWidgets.QPushButton(self.centralwidget)
        self.Apptize.setGeometry(QtCore.QRect(100, 260, 261, 81))
        self.Apptize.setStyleSheet("image: url(:/pic/80511.png);\n"
"background-color: rgb(255, 221, 97);\n"
"border-radius: 15px;")
        self.Apptize.setText("")
        self.Apptize.setObjectName("Apptize")
        self.Dessert = QtWidgets.QPushButton(self.centralwidget)
        self.Dessert.setGeometry(QtCore.QRect(100, 410, 261, 91))
        self.Dessert.setStyleSheet("image: url(:/pic/1046885.png);\n"
"background-color: rgb(255, 207, 207);\n"
"border-radius: 15px;")
        self.Dessert.setText("")
        self.Dessert.setObjectName("Dessert")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(107, 117, 261, 81))
        self.graphicsView_2.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(255, 215, 202);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(107, 267, 261, 81))
        self.graphicsView_3.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(255, 255, 180);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(107, 417, 261, 91))
        self.graphicsView_4.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(255, 235, 252);")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.graphicsView_4.raise_()
        self.graphicsView_3.raise_()
        self.graphicsView_2.raise_()
        self.Maindish.raise_()
        self.Apptize.raise_()
        self.Dessert.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 26))
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
        self.label.setText(_translate("MainWindow", "วันนี้กินอะไรดี"))
import foodpic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

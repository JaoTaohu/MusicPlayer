# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cupcake.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 1039)
        MainWindow.setStyleSheet("background-color: rgb(255, 162, 138);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 51, 28))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 216, 183);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.foodpic = QtWidgets.QGraphicsView(self.centralwidget)
        self.foodpic.setGeometry(QtCore.QRect(0, 0, 831, 441))
        self.foodpic.setStyleSheet("border-image: url(:/pic/b0fa2a4a-3184-4f6b-83f2-00eb175bf3f8.jpg);")
        self.foodpic.setObjectName("foodpic")
        self.ingredient = QtWidgets.QTextBrowser(self.centralwidget)
        self.ingredient.setGeometry(QtCore.QRect(30, 460, 381, 531))
        self.ingredient.setStyleSheet("background-color: rgb(255, 223, 212);\n"
"border-radius: 15px;")
        self.ingredient.setObjectName("ingredient")
        self.recipe = QtWidgets.QTextBrowser(self.centralwidget)
        self.recipe.setGeometry(QtCore.QRect(430, 460, 381, 531))
        self.recipe.setStyleSheet("background-color: rgb(255, 223, 212);\n"
"border-radius: 15px;")
        self.recipe.setObjectName("recipe")
        self.foodpic.raise_()
        self.pushButton_5.raise_()
        self.ingredient.raise_()
        self.recipe.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 26))
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
        self.pushButton_5.setText(_translate("MainWindow", "Back"))
        self.ingredient.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">วัตถุดิบ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">เนยสด 120 กรัม</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">น้ำตาลทราย 120 กรัม</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">กลิ่นวานิลลา 1/2 ช้อนชา</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ไข่ 2 ฟอง</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">แป้งสาลีอเนกประสงค์ 120 กรัม</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ครีมและเกล็ดน้ำตาลตกแต่งตามชอบ</span></p></body></html>"))
        self.recipe.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">วิธีทำ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">STEP 1 : เทเนยสดอุณหภูมิห้องและน้ำตาลทรายขาวลงในชาม</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">ผสม และปั่นให้เข้ากันจนเนยเริ่มขึ้นฟูเนื้อเนียน หลังจากเนยกับน้ำตาลเข้ากันดีแล้ว เติมกลิ่นวานิลลาลงไป ทยอยใส่ไข่ครั้งละฟองและปั่นให้เข้ากันดี ทยอยแบ่งใส่แป้ง 3 รอบและตีจนกระทั่งเนื้อแป้งเนียน</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">STEP 2 : นำแป้งที่ได้มาเทใส่พิมพ์ปริมาณ 1/2 ถ้วย</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">STEP 3 : ใส่น้ำรองก้นจานก่อนจะนำเข้าเวฟ ใช้กำลังไฟ 800 วัตต์ ประมาณ 2 นาที ตกแต่งด้วยครีมและเกล็ดน้ำตาลตามชอบ</span></p></body></html>"))
import foodpic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

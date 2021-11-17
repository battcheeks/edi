from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QtCursor
import qdarkstyle
from PyQt5 import Qt
import webbrowser
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys

class GUI(QDialog):
    def __init__(self):
        super(GUI,self).__init__()
        loadUi('gui (1).ui',self)
        self.move(0,150)
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.on_click2)
        self.pushButton_3.clicked.connect(self.on_click3)
        self.pushButton_4.clicked.connect(self.on_click4)
        self.pushButton_5.clicked.connect(self.on_click5)
        self.pushButton_6.clicked.connect(self.on_click6)
        self.pushButton_7.clicked.connect(self.on_click7)
        self.pushButton_8.clicked.connect(self.on_click8)
        self.pushButton_9.clicked.connect(self.on_click9)
        self.pushButton_10.clicked.connect(self.on_click10)
        self.pushButton_11.clicked.connect(self.on_click11)
        self.pushButton_12.clicked.connect(self.on_click12)
        self.pushButton_13.clicked.connect(self.on_click13)
        self.pushButton_14.clicked.connect(self.on_click14)
        self.checkBox.clicked.connect(self.checkbox1)
        self.checkBox_2.clicked.connect(self.checkbox2)
        self.checkBox_3.clicked.connect(self.checkbox3)
        self.pushButton_15.clicked.connect(self.checkifclicked)
    
    def checkifclicked(self):
        a = self.lineEdit.text()
        b= "https://"+ a
        if a[0:8]=="https://":
           webbrowser.open(a) 
        else:
            a = "https://" + a 
            webbrowser.open(a)
        self.lineEdit.setText("")

    def checkbox1(self):
        if self.checkBox.isChecked():
            self.close()

    def checkbox2(self):
        if self.checkBox_2.isChecked():
            self.setWindowFlags(Qt.Qt.WindowStaysOnTopHint)
            self.setWindowFlag(Qt.Qt.FramelessWindowHint)
            self.show()
        else:
            self.setWindowFlags(Qt.Qt.WindowStaysOnBottomHint)
            self.setWindowFlag(Qt.Qt.FramelessWindowHint)
            self.show()

    def checkbox3(self):
        if self.checkBox_3.isChecked():
            self.setWindowFlag(Qt.Qt.FramelessWindowHint)
            self.show()
        else:
            self.setWindowFlags(Qt.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(Qt.Qt.WindowStaysOnBottomHint)
            self.show()


    def on_click(self):
        webbrowser.open("https://google.com")

    def on_click2(self):
        webbrowser.open("https://www.youtube.com/")

    def on_click3(self):
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    def on_click4(self):
        webbrowser.open("https://mail.google.com/mail/u/1/#inbox")

    def on_click5(self):
        webbrowser.open("https://docs.google.com/document/u/1/?tgif=d")

    def on_click6(self):
        webbrowser.open("https://docs.google.com/spreadsheets/u/1/?tgif=d")

    def on_click7(self):
        webbrowser.open("https://docs.google.com/forms/u/1/?tgif=d")

    def on_click8(self):
        webbrowser.open("https://docs.google.com/presentation/u/1/?tgif=d")

    def on_click9(self):
        webbrowser.open("https://instagram.com")

    def on_click10(self):
        webbrowser.open("https://github.com/battcheeks")

    def on_click11(self):
        webbrowser.open("https://netflix.com")

    def on_click12(self):
        webbrowser.open("https://primevideo.com")

    def on_click13(self):
        webbrowser.open("https://hotstar.com")

    def on_click14(self):
        webbrowser.open("https://meet.google.com?authuser=1")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    window.setWindowTitle('Dock')
    # window.setStyleSheet(qdarkstyle.load_stylesheet())
    window.show()
    sys.exit(app.exec_())

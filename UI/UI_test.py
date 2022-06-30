import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

dir = 'UI/Main GUI.ui'
form_class = uic.loadUiType(dir)[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__=='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
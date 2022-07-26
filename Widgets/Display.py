from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

class Display(QWidget):
    def __init__(self, canvas, scroll_area, model):
        super().__init__()
        self.Model = model

        self.canvas = canvas
        self.scroll_area = scroll_area

    def setScrollArea(self):
        pass

    def setDisplayAnnotInfo(self):
        pass

    def displayImage(self):
        pass
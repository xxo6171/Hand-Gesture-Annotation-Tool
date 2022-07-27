from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

class Display(QWidget):
    def __init__(self, canvas, scroll_area, model):
        super().__init__()
        self.Model = model

        self.canvas = canvas
        self.scroll_area = scroll_area

    def setDisplayAnnotInfo(self):
        pass

    def displayImage(self, img, w, h):
        self.canvas.clear()

        self.canvas.setGeometry(0, 0, w, h)
        self.canvas.setPixmap(img)

        self.scroll_area.setWidget(self.canvas)
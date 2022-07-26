from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from Widgets.Display import *

class Draw(QWidget):
    def __init__(self, view, model):
        super().__init__()

        self.Model = model

        self.canvas = QLabel(self)
        self.scroll_area = view

        # Init Display Class
        self.Display = Display(self.canvas, self.scroll_area, self.Model)


    # ----- Set View -----
    def setCanvas(self):
        pass


    # ----- Mouse Event -----
    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass


    def startMouseTracking(self):
        pass

    def stopMouseTracking(self):
        pass


    # ----- Draw -----
    def draw(self):
        pass


    # ----- Retouch -----
    def movePoint(self):
        pass
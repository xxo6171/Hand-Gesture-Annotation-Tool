from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from Widgets.Display import *

class Zoom(QWidget):
    def __init__(self, view, model):
        super().__init__()

        self.Model = model

        self.canvas = QLabel(self)
        self.scroll_area = view

        # Init Display Class
        self.Display = Display(self.canvas, self.scroll_area, self.Model)

        # Set Focus Policy
        self.setFocusPolicy(Qt.ClickFocus)


    # ----- Set View -----
    def setCanvas(self):
        pass
    

    # ----- Focus Event -----
    def focusInEvent(self, event):
        pass

    def focusOutEvent(self, event):
        pass


    # ----- Wheel Event -----
    def wheelEvent(self, event):
        pass


    # ----- Zoom -----
    def zoomIn(self):
        pass

    def zoomOut(self):
        pass
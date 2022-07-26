from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
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
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from Widgets.Draw import *
from Widgets.Zoom import *

class ViewModel(QWidget):
    def __init__(self, view, model):
        super().__init__()
        self.Model = model

        self.actions = view[0]
        self.widgets = view[1]

        # Widgets Init
        self.scroll_area = self.widgets[0]

        # Function Class Init
        self.Draw = Draw(self.scroll_area, self.Model)
        self.Zoom = Zoom(self.scroll_area, self.Model)

        # Actions Init
        self.action = view

        # Actions Connections
        self.action.triggered.connect(self.method)
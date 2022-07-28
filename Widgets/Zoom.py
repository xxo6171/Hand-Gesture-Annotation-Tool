from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from Widgets.Display import *

class Zoom(QWidget):
    def __init__(self, view, model):
        super().__init__()
        self.deleteLater()

        self.Model = model

        self.canvas = QLabel(self)
        self.scroll_area = view

        # Init Display Class
        self.Display = Display(self.canvas, self.scroll_area, self.Model)

        # Set Focus Policy
        self.setFocusPolicy(Qt.ClickFocus)


    # ----- Set View -----
    def setCanvas(self):
        self.Display.setDisplayAnnotInfo()
        img, w, h, c = self.Model.getImgScaled()

        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)

        self.Display.displayImage(img, w, h)
        self.scroll_area.setWidget(self)
    

    # ----- Focus Event -----
    def focusInEvent(self, event):
        print('Zoom Focus In')

    def focusOutEvent(self, event):
        print('Zoom Focus Out')


    # ----- Wheel Event -----
    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            print('Zoom Wheel Up')
        elif event.angleDelta().y() < 0:
            print('Zoom Wheel Down')


    # ----- Zoom -----
    def zoomIn(self):
        pass

    def zoomOut(self):
        pass
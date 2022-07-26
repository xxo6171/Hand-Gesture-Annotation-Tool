from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from Widgets.Display import *
from Widgets.AddObjectDialog import *

class Draw(QWidget):
    def __init__(self, view, model):
        super().__init__()

        self.Model = model

        self.canvas = QLabel(self)
        self.scroll_area = view[0]
        self.label_list = view[1]
        self.object_list = view[2]

        # Init Display Class
        self.Display = Display(self.canvas, self.scroll_area, self.Model)


    # ----- Set View -----
    def setCanvas(self):
        pass


    # ----- Context Menu Event -----
    def contextMenuEvent(self, event):
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

    def setObject(self):
        pass


    # ----- Retouch -----
    def movePoint(self):
        pass

    
    # ----- Object List Click Event -----
    def objectClicked(self):
        pass

    def objectDoubleClicked(self):
        pass


    # ----- Delete -----
    def deleteObject(self):
        pass
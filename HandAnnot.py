from PyQt5 import uic
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
import sys


from Model import *
from Widgets.Draw import *
from Widgets.Zoom import *

mainUI_dir = 'Resource/UI/Main GUI.ui'
main_form_class = uic.loadUiType(mainUI_dir)[0]

class HandAnnot(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.binding()
        self.actionConnect()

    def binding(self):
        self.Model = Model()

        self.Draw = Draw([self.scrollArea_Canvas, self.listWidget_LabelList, self.listWidget_ObjectList], self.Model)
        self.Zoom = Zoom(self.scrollArea_Canvas, self.Model)

    def actionConnect(self):
        self.action_Open.triggered.connect(self.openFile)
        self.action_Save.triggered.connect(self.saveJson)
        self.action_Exit.triggered.connect(self.exit)

        self.action_Polygon.triggered.connect(self.setPolygon)
        self.action_Right_Gesture.triggered.connect(self.setRightGesture)
        self.action_Left_Gesture.triggered.connect(self.setLeftGesture)
        self.action_Rectangle.triggered.connect(self.setRect)
        self.action_Circle.triggered.connect(self.setCircle)
        self.action_Line.triggered.connect(self.setLine)
        self.action_Dot.triggered.connect(self.setDot)

        self.action_Retouch.triggered.connect(self.setRetouch)
        self.action_Auto_Annotation.triggered.connect(self.setAuto)

        self.action_Zoom_In.triggered.connect(self.setZoomIn)
        self.action_Zoom_Out.triggered.connect(self.setZoomOut)


    # ----- File Actions -----
    def openFile(self):
        pass

    def saveJson(self):
        pass

    def exit(self):
        pass


    # ----- Edit Actions -----
    def setPolygon(self):
        pass

    def setRightGesture(self):
        pass

    def setLeftGesture(self):
        pass

    def setRect(self):
        pass

    def setCircle(self):
        pass

    def setLine(self):
        pass

    def setDot(self):
        pass

    def setRetouch(self):
        pass

    def setAuto(self):
        pass


    # ----- Zoom Actions -----
    def setZoomIn(self):
        pass

    def setZoomOut(self):
        pass


    # ----- Key Event -----
    def keyPressEvent(self, event):
        pass

    def keyReleaseEvent(self, event):
        pass


    # ----- Undo -----
    def undo(self):
        pass


if __name__=='__main__':
    app = QApplication(sys.argv)
    view = HandAnnot()
    view.show()
    app.exec_()
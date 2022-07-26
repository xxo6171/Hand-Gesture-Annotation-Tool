from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from Widgets.Draw import *
from Widgets.Zoom import *

class ViewModel(QWidget):
    def __init__(self, view, model):
        super().__init__()
        
        self.Model = model

        self.viewActions = view[0]
        self.viewWidgets = view[1]

        # Widgets Init
        self.scroll_area = self.viewWidgets[0]
        self.label_list = self.viewWidgets[1]
        self.object_list = self.viewWidgets[1]
        
        # Function Class Init
        self.Draw = Draw(self.scroll_area, self.Model)
        self.Zoom = Zoom(self.scroll_area, self.Model)

        # Actions Init
        self.initActions()

        # Actions Connections
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
    

    def initActions(self):
        # File Actions
        file_actions = self.viewActions[0]

        self.action_Open = file_actions[0]
        self.action_Save = file_actions[1]
        self.action_Exit = file_actions[2]

        # Edit Actions
        edit_actions = self.viewActions[1]

        self.action_Polygon = edit_actions[0]
        self.action_Right_Gesture = edit_actions[1]
        self.action_Left_Gesture = edit_actions[2]
        self.action_Rectangle = edit_actions[3]
        self.action_Circle = edit_actions[4]
        self.action_Line = edit_actions[5]
        self.action_Dot = edit_actions[6]

        self.action_Retouch = edit_actions[7]
        self.action_Auto_Annotation = edit_actions[8]

        # Zoom Actions
        zoom_actions = self.viewActions[2]

        self.action_Zoom_In = zoom_actions[0]
        self.action_Zoom_Out = zoom_actions[1]
    
    
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
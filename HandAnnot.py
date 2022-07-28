from PyQt5 import uic
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

import sys
import os

from Model import *
from Widgets.Draw import *
from Widgets.Zoom import *

from Utils.ConvertAnnotation import *
from Utils.ImageProc import *

mainUI_dir = 'Resource/UI/Main GUI.ui'
main_form_class = uic.loadUiType(mainUI_dir)[0]

class HandAnnot(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.binding()
        self.actionConnect()

        # Disable Menu
        self.menu_Edit.setEnabled(False)
        self.menu_Zoom.setEnabled(False)
        self.action_Save.setEnabled(False)

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
        # File Open by Dialog
        title = 'Open Image'
        filter = 'Images(*.jpg *.jpeg *.png)'
        file_path = QFileDialog.getOpenFileName(self, title, filter=filter)[0]

        # Exception Handling - Unavailable File Path
        if file_path == '': 
            return

        # Initialize Data in Model
        self.initData()

        # Extract Image File Name
        base_name = os.path.basename(file_path)
        file_name, extension_type = os.path.splitext(base_name)

        # Set *.json File Name for Exist Check
        json_path = os.path.dirname(file_path) + '/' + file_name + '.json'

        # Load Image From File Path
        img, w, h, c = loadImgData(file_path)

        if ( extension_type == '.json' ) or ( os.path.isfile(json_path) ):
            # Save Loaded Annotation Info to Model
            opened_annot_info = json2Dict(json_path)
            self.Model.setAnnotDict(opened_annot_info)

            cur_annot_info = self.Model.getAnnotInfo()
            normalized_annot_info = normalization(cur_annot_info, w, h)
            self.model.setAnnotDict(normalized_annot_info)
        else :
            self.Model.setAnnotInfo(file_path, w, h)

        # Save Original Image to Model
        self.Model.setImgData(img, w, h, c)

        # Save Image for Display to Model
        img_QPixmap = self.img2QPixmap(img, w, h, c)
        self.Model.setImgScaled(img_QPixmap, w, h, c)

        # Activate Menu
        self.Model.setMenuFlag(True)
        self.menuRefresh()

        # Set List Widgets

        # Display Canvas
        self.Draw.setCanvas()
    
    def menuRefresh(self):
        if self.Model.getMenuFlag():
            self.menu_Edit.setEnabled(True)
            self.menu_Zoom.setEnabled(True)
            self.action_Save.setEnabled(True)
        else:
            self.menu_Edit.setEnabled(False)
            self.menu_Zoom.setEnabled(False)
            self.action_Save.setEnabled(False)

    def img2QPixmap(self, img, w, h, c):
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        qPixmap = QPixmap.fromImage(qImg)

        return qPixmap

    def initData(self):
        self.Model.setImgData(None, None, None, None)
        self.Model.setImgScaled(None, None, None, None)
        self.Model.initAnnotStack()
        self.Model.initAnnotInfo()
        self.Model.initLabelList()


    def saveJson(self):
        pass

    def exit(self):
        pass


    # ----- Edit Actions -----
    def setPolygon(self):
        self.setDraw('Polygon')
        self.Model.setKeepTracking(True)

    def setRightGesture(self):
        self.setGesture('right')

    def setLeftGesture(self):
        self.setGesture('left')

    def setRect(self):
        self.setDraw('Rectangle')

    def setCircle(self):
        self.setDraw('Circle')

    def setLine(self):
        self.setDraw('Line')

    def setDot(self):
        self.setDraw('Dot')
        self.Draw.setTracking(True)

    def setGesture(self, hand_dir):
        self.setDraw('Gesture Polygon', draw=False)
        
        # 손목 Point
        self.Model.addCurPoint([0.5, 0.65], True)

        # 엄지손가락 시작점 설정
        if hand_dir == 'right':
            x_pos = 0.4
        elif hand_dir == 'left':
            x_pos = 0.6
        y_pos = 0.5

        # 점찍기 시작
        nb_points = 21
        for idx in range(1, nb_points):
            if idx%4 == 1:
                # 오른손은 왼쪽에서 오른쪽
                if hand_dir == 'right':
                    x_pos += 0.05
                # 왼손은 오른쪽에서 왼쪽
                elif hand_dir == 'left':
                    x_pos -= 0.05
                y_pos = 0.5
            pos = [round(x_pos, 2), round(y_pos, 2)]
            self.Model.addCurPoint(pos, True)
            y_pos -= 0.05

        self.Draw.addObject()

    def setDraw(self, shape, draw=True):
        self.Draw.setCanvas()

        self.Model.setDrawFlag(draw)
        self.Model.setCurShapeType(shape)
        self.Model.resetCurPoints()

        self.statusBar.showMessage('Seleted Shape: {shape}'.format(shape = shape))
        
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
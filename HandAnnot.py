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

        # Extract Image File Name
        base_name = os.path.basename(file_path)
        file_name, extension_type = os.path.splitext(base_name)

        # Set *.json File Name for Exist Check
        json_path = os.path.dirname(file_path) + '/' + file_name + '.json'

        '''!!!! 여기 과연 필요할까 !!!!'''
        self.initWindow()

        # Load Image From File Path
        img, w, h, c = loadImgData(file_path)

        if ( extension_type == '.json' ) or ( os.path.isfile(json_path) ):
            # Save Loaded Annotation Info to Model
            opened_annot_info = json2Dict(json_path)
            self.Model.setAnnotDict(opened_annot_info)

            '''!!! 정규화 - 많이 쓰이기 때문에 함수화 팔요 !!!'''
            cur_annot_info = self.Model.getAnnotInfo(no_deep = True)
            shapes = cur_annot_info['shapes']
            for shape in shapes:
                points = shape['points']
                for point in points:
                    point[0] /= w
                    point[1] /= h
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

    ''' 없애는 방법 생각해야함'''
    def initWindow(self):
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
from tkinter import W
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.ImageProc import *
from Utils.AutoAnnotation import *
import Constant

class Canvas(QMainWindow):
    def __init__(self, view, model):
        # Initialize
        super().__init__()
        self.flag = False

        self.action_Open, self.label_Canvas, self.scrollArea_Canvas = view[0],view[1],view[2]
        self.menu_Edit, self.menu_Zoom, self.action_Save = view[3],view[4],view[5]

        self.action_Line = view[6]
        self.statusBar = view[7]

        self.model = model
        self.menuRefresh(self.flag)
        #Triggered connect
        self.action_Open.triggered.connect(self.openImage)
        self.action_Line.triggered.connect(self.drawLine)

        #Widget setting
        self.label_Canvas.setAlignment(Qt.AlignCenter)
        self.scrollArea_Canvas.setWidget(self.label_Canvas)

    # Refresh menu
    def menuRefresh(self, flag):
        if flag: self.menu_Edit.setEnabled(True);self.menu_Zoom.setEnabled(True);self.action_Save.setEnabled(True);
        else:self.menu_Edit.setEnabled(False);self.menu_Zoom.setEnabled(False);self.action_Save.setEnabled(False);


    def openImage(self):
        self.filepath = QFileDialog.getOpenFileName(self, 'Open File',filter='Images(*.jpg *.jpeg *.png)')
        if self.filepath[0] != '' :
            img = loadImgData(self.filepath[0])
            
            # !!! Auto Annotation 부분 지워도 무방 !!!
            img, landmark = autoAnnotation(img)

            self.model.setImgData(img)
            self.displayImage(img)

    def displayImage(self, img):
        h, w, c = img.shape  # height, width, channel
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        self.qPixmap = QPixmap.fromImage(qImg)
        self.label_Canvas.setPixmap(self.qPixmap)
        self.flag = True
        self.menuRefresh(self.flag)
    
    def drawLine(self):
        self.model.setDrawFlag(Constant.LINE)
    
    def scaleImage(self, img):
        h, w, c = img.shape
        scaled_img = img

        if h>w:
            scale = 810 / h
        else:
            scale = 1280 / w
        self.model.setScaleRatio(scale)

        scaled_img = cv2.resize(scaled_img, dsize=(0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
        self.model.setImgScaled(scaled_img)
        
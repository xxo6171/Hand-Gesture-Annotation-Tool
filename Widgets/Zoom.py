from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Utils.ImageProc import *
from Utils.Display import *

class Zoom(QWidget):
    def __init__(self, model):
        super().__init__()

        self.Model = model

        self.canvas = QLabel(self)

        # Set Focus Policy
        self.setFocusPolicy(Qt.ClickFocus)


    # ----- Set View -----
    def setCanvas(self):
        qimg, annot_info, point_scale = loadQImg(self.Model)
        qimg_add_info = setDisplayAnnotInfo(qimg, annot_info, point_scale)
        w, h, c = self.Model.getImgScaled(no_img=True)

        self.Model.setImgScaled(qimg_add_info, w, h, c)

        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)

        displayImage(self.canvas, qimg_add_info, w, h)
    

    # ----- Wheel Event -----
    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoomIn()
        elif event.angleDelta().y() < 0:
            self.zoomOut()


    # ----- Zoom -----
    def zoomIn(self):
        img, w, h, c = self.Model.getImgData()
        interpolation = 1
        self.Model.setScaleRatio(self.Model.getScaleRatio() * 1.25)
        ratio = self.Model.getScaleRatio()

        if ratio > 3.05 : self.Model.setScaleRatio(3.05)

        if ratio > 0.99 and ratio < 1.001 : self.Model.setScaleRatio(1.0)

        if ratio <= 3.05 :
            img, w, h, c = resizeImage(img, self.Model.getScaleRatio(), interpolation)
            img_scaled = self.img2QPixmap(img, w, h, c)
            self.Model.setImgScaled(img_scaled, w, h, c)
            
        self.setCanvas()

    def zoomOut(self):
        img, w, h, c = self.Model.getImgData()
        interpolation = 0
        self.Model.setScaleRatio(self.Model.getScaleRatio() * 0.8)
        ratio = self.Model.getScaleRatio()

        if ratio < 0.21: self.Model.setScaleRatio(0.21)

        if ratio > 0.99 and ratio < 1.001 : self.Model.setScaleRatio(1.0)

        if ratio >= 0.21:
            img, w, h, c = resizeImage(img, self.Model.getScaleRatio(), interpolation)
            img_scaled = self.img2QPixmap(img, w, h, c)
            self.Model.setImgScaled(img_scaled, w, h, c)

        self.setCanvas()
        
    def img2QPixmap(self, img, w, h, c):
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        qPixmap = QPixmap.fromImage(qImg)

        return qPixmap
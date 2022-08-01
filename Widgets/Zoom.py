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
        self.Model.setZoomType('In') if event.angleDelta().y() > 0 else self.Model.setZoomType('Out')
        self.resizeZoomInOut()

    # ----- Resize Zoom -----
    def resizeZoomInOut(self):
        # 이미지 데이터 불러오기
        img, w, h, c = self.Model.getImgData()

        # 확대/축소 type 가져오기
        type = self.Model.getZoomType()

        # 확대의 경우 interpolation=LINEAR(쌍선형보간법), 축소의 경우 interpolation=AREA(영역보간법)
        interpolation = 'LINEAR' if type == 'In' else 'AREA'

        # 배율에 곱할 n 변수, flag가 확대의 경우 n = 1.25, 축소의 경우 n = 0.8
        n = 1.25 if type == 'In' else 0.8

        # 기존 저장된 Scale Ratio와 f를 곱하여 Scale Ratio에 저장
        self.Model.setScaleRatio(self.Model.getScaleRatio() * n)

        # 계산하여 저장된 ScaleRatio 값 가져오기, 밑 3줄 코드에 만족하지 않으면 해당 가져온 값 그대로 내려감
        ratio = self.Model.getScaleRatio()

        # 확대/축소 최대 배율 고정
        ratio = 3.05 if type == 'In' and ratio > 3.05 else ratio
        ratio = 0.21 if type == 'Out' and ratio < 0.21 else ratio

        # 확대/축소 작업 중 원본으로 맞출 때 크기 1로 나누어 떨어지지 않음. 조건 범위에 존재하면 1로 설정
        ratio = 1.0 if (type == 'In' or type == 'Out') and (ratio > 0.99 and ratio < 1.001) else ratio

        self.Model.setScaleRatio(ratio)

        # cv2로 이미지를 resize한 이미지 데이터 반환
        img, w, h, c = resizeImgData(img, ratio, interpolation)

        img_scaled = self.img2QPixmap(img, w, h, c)
        self.Model.setImgScaled(img_scaled, w, h, c)
        self.setCanvas()

    def img2QPixmap(self, img, w, h, c):
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        qPixmap = QPixmap.fromImage(qImg)

        return qPixmap
from tkinter import W
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from Utils.ImageProc import *
from Utils.AutoAnnotation import *

class Canvas(QWidget):
    def __init__(self, view, model):
        # Initialize
        super().__init__()

        self.label_Canvas = QLabel(self)

        self.action_Open = view[0]

        self.menu_Edit = view[1]
        self.menu_Zoom = view[2]
        self.action_Save = view[3]

        self.action_Polygon = view[4][0]
        self.action_Gesture_Polygon = view[4][1]
        self.action_Rectangle = view[4][2]
        self.action_Circle = view[4][3]
        self.action_Line = view[4][4]
        self.action_Dot = view[4][5]
        
        self.statusBar = view[5]

        self.action_Zoom_In = view[6]
        self.action_Zoom_Out = view[7]

        self.model = model
        self.model.setCtrlFlag(False)
        self.model.setMenuFlag(False)
        self.model.setFocusFlag(False)
        self.menuRefresh(self.model.getMenuFlag())

        #Triggered connect
        self.action_Open.triggered.connect(self.openImage)
        
        self.action_Polygon.triggered.connect(self.drawPoly)
        self.action_Gesture_Polygon.triggered.connect(self.drawGesturePoly)
        self.action_Rectangle.triggered.connect(self.drawRect)
        self.action_Circle.triggered.connect(self.drawCircle)
        self.action_Line.triggered.connect(self.drawLine)
        self.action_Dot.triggered.connect(self.drawDot)
        self.action_Zoom_In.triggered.connect(self.zoomInImage)
        self.action_Zoom_Out.triggered.connect(self.zoomOutImage)

        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.ClickFocus)


    # Refresh menu
    def menuRefresh(self, flag):
        if flag: self.menu_Edit.setEnabled(True);self.menu_Zoom.setEnabled(True);self.action_Save.setEnabled(True);
        else:self.menu_Edit.setEnabled(False);self.menu_Zoom.setEnabled(False);self.action_Save.setEnabled(False);

    def openImage(self):
        self.filepath = QFileDialog.getOpenFileName(self, 'Open File',filter='Images(*.jpg *.jpeg *.png)')
        if self.filepath[0] != '' :
            img, w, h, c = loadImgData(self.filepath[0])
            self.model.setImgData(img, w, h, c)
            self.model.setImgScaled(img, w, h, c)
            self.displayImage()

    def displayImage(self):
        img, w, h, c = self.model.getImgScaled()
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        qPixmap = QPixmap.fromImage(qImg)

        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)
        self.label_Canvas.setGeometry(0, 0, w, h)
        self.label_Canvas.setPixmap(qPixmap)

        self.model.setMenuFlag(True)
        self.menuRefresh(self.model.getMenuFlag())

    def zoomInImage(self):
        img, w, h, c = self.model.getImgData()
        interpolation = 1
        self.model.setScaleRatio(self.model.getScaleRatio() * 1.25)
        if self.model.getScaleRatio() > 3.05 :
            self.model.setScaleRatio(3.05)

        # 배율을 조정하면 1로 나누어 떨어지지 않음
        if self.model.getScaleRatio() > 0.99 and self.model.getScaleRatio() < 1.001 :
            self.model.setScaleRatio(1.0)

        if self.model.getScaleRatio() <= 3.05 :
            img, w, h, c = resizeImage(img, self.model.getScaleRatio(), interpolation)
            self.model.setImgScaled(img, w, h, c)
        self.displayImage()
        print('배율 = ', self.model.getScaleRatio())

    def zoomOutImage(self):
        img, w, h, c = self.model.getImgData()
        interpolation = 0
        self.model.setScaleRatio(self.model.getScaleRatio() * 0.8)
        if self.model.getScaleRatio() < 0.21:
            self.model.setScaleRatio(0.21)

        # 배율을 조정하면 1로 나누어 떨어지지 않음
        if self.model.getScaleRatio() > 0.99 and self.model.getScaleRatio() < 1.001 :
            self.model.setScaleRatio(1.0)

        if self.model.getScaleRatio() >= 0.21:
            img, w, h, c = resizeImage(img, self.model.getScaleRatio(), interpolation)
            self.model.setImgScaled(img, w, h, c)
        self.displayImage()
        print('배율 = ', self.model.getScaleRatio())
    
    def drawLine(self):
        self.model.setDrawFlag('Line')

    def focusInEvent(self,event):
        self.model.setFocusFlag(True)
        print(self.model.getFocusFlag())
        QWidget.focusInEvent(self, event)

    def focusOutEvent(self, event):
        self.model.setFocusFlag(False)
        print(self.model.getFocusFlag())
        QWidget.focusOutEvent(self, event)

    # Image scaling using keyboard, mouse wheel event
    def keyPressEvent(self, event):  # Press Control Key
        if event.key() == Qt.Key_Control:
            self.model.setCtrlFlag(True)
            print(self.model.getCtrlFlag())

    def keyReleaseEvent(self, event):  # Release Control Key
        if event.key() == Qt.Key_Control:
            self.model.setCtrlFlag(False)
            print(self.model.getCtrlFlag())

    def wheelEvent(self, event):       # Move Mouse Wheel
        if not self.model.getFocusFlag():
            return
        if self.model.getImgData() is None:
            return
        if not self.model.getCtrlFlag():
            return
        if event.angleDelta().y() > 0 :
            self.zoomInImage()
        elif event.angleDelta().y() < 0 :
            self.zoomOutImage()

    def mouseMoveEvent(self, event):
        if self.model.getDrawFlag() in 'No Draw':
            return
        x_pos = event.x()
        y_pos = event.y()
        self.model.setCurPos([x_pos, y_pos])
        text = '[ {x_pos}, {y_pos} ] {draw}'.format(x_pos=x_pos, y_pos=y_pos, draw = self.model.getDrawFlag())
        self.statusBar.showMessage(text)
        self.draw()
        
    def mouseReleaseEvent(self, event):
        if self.label_Canvas.hasMouseTracking():
            self.stopMouseTracking()
        else:
            past_x_pos = event.x()
            past_y_pos = event.y()
            self.model.setPrePos([past_x_pos, past_y_pos])
            self.startMouseTracking()
    
    def draw(self):
        flag = self.model.getDrawFlag()
        img, w, h, c = self.model.getImgScaled()

        draw_img = img.copy()
        draw_img = QImage(draw_img.data, w, h, w * c, QImage.Format_RGB888)
        draw_img = QPixmap.fromImage(draw_img)

        painter = QPainter(draw_img)
        painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))

        pre_pos = self.model.getPrePos()
        cur_pos = self.model.getCurPos()

        if flag == 'No Draw':
            return
        elif flag == 'Polygon':
            pass
        elif flag == 'Gesture Polygon':
            pass
        elif flag == 'Rectangle':
            x_pos = pre_pos[0]
            y_pos = pre_pos[1]
            width = cur_pos[0] - x_pos
            height = cur_pos[1] - y_pos
            painter.drawRect(x_pos, y_pos, width, height)

        elif flag == 'Circle':
            pass
        elif flag == 'Line':
            src_x = pre_pos[0]
            src_y = pre_pos[1]
            dst_x = cur_pos[0]
            dst_y = cur_pos[1]
            painter.drawLine(src_x, src_y, dst_x, dst_y)
            
        elif flag == 'Dot':
            painter.drawPoint(cur_pos[0], cur_pos[1])

        painter.end()
        self.label_Canvas.setPixmap(draw_img)

    def drawPoly(self):
        self.model.setDrawFlag('Polygon')
        self.stopMouseTracking()

    def drawGesturePoly(self):
        self.model.setDrawFlag('Gesture Polygon')
        self.stopMouseTracking()

    def drawRect(self):
        self.model.setDrawFlag('Rectangle')
        self.stopMouseTracking()

    def drawCircle(self):
        self.model.setDrawFlag('Circle')
        self.stopMouseTracking()

    def drawLine(self):
        self.model.setDrawFlag('Line')
        self.stopMouseTracking()

    def drawDot(self):
        self.model.setDrawFlag('Dot')
        self.stopMouseTracking()

    def stopMouseTracking(self):
        self.label_Canvas.setMouseTracking(False)

    def startMouseTracking(self):
        self.label_Canvas.setMouseTracking(True)
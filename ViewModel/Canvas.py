import os
import math

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Utils.ImageProc import *
from Utils.AutoAnnotation import *
from Utils.ConvertAnnotation import *

from ViewModel.AddLabelDialog import AddLabelDialog

class Canvas(QWidget):
    def __init__(self, view, model):
        # Initialize
        super().__init__()
        self.initUI(view)
        self.initData(model)

    def initUI(self, view):
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
        self.action_Retouch = view[4][6]

        self.statusBar = view[5]

        self.action_Zoom_In = view[6]
        self.action_Zoom_Out = view[7]

        self.listWidget_LabelList = view[8]

        # Triggered connect
        self.action_Open.triggered.connect(self.openImage)
        self.action_Save.triggered.connect(self.saveJson)

        self.action_Polygon.triggered.connect(self.drawPoly)
        self.action_Gesture_Polygon.triggered.connect(self.drawGesturePoly)
        self.action_Rectangle.triggered.connect(self.drawRect)
        self.action_Circle.triggered.connect(self.drawCircle)
        self.action_Line.triggered.connect(self.drawLine)
        self.action_Dot.triggered.connect(self.drawDot)
        self.action_Retouch.triggered.connect(self.retouch)

        self.action_Zoom_In.triggered.connect(self.zoomInImage)
        self.action_Zoom_Out.triggered.connect(self.zoomOutImage)

        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.ClickFocus)

    def initData(self, model):
        self.model = model
        self.model.setCtrlFlag(False)
        self.model.setMenuFlag(False)
        self.model.setFocusFlag(False)
        self.menuRefresh()

    # Refresh menu
    def menuRefresh(self):
        if self.model.getMenuFlag():
            self.menu_Edit.setEnabled(True)
            self.menu_Zoom.setEnabled(True)
            self.action_Save.setEnabled(True)
        else:
            self.menu_Edit.setEnabled(False)
            self.menu_Zoom.setEnabled(False)
            self.action_Save.setEnabled(False)

    def openImage(self):
        self.filePath = QFileDialog.getOpenFileName(self, 'Open File',filter='Images(*.jpg *.jpeg *.png)')
        if self.filePath[0] == '' :
            return
        img, w, h, c = loadImgData(self.filePath[0])
        self.model.setImgData(img, w, h, c)
        self.model.setImgScaled(img, w, h, c)
        self.model.setAnnotInfo(self.filePath[0], w, h)
        self.displayImage()

    def saveJson(self):
        fileName = os.path.splitext(os.path.basename(self.filePath[0]))
        jsonPath = os.path.dirname(self.filePath[0]) + '/' + fileName[0] + '.json'
        dict2Json(self.model.getAnnotInfo(), jsonPath)

    def displayImage(self):
        img, w, h, c = self.model.getImgScaled()
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        qPixmap = QPixmap.fromImage(qImg)

        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)
        self.label_Canvas.setGeometry(0, 0, w, h)
        self.label_Canvas.setPixmap(qPixmap)

        self.model.setMenuFlag(True)
        self.menuRefresh()

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
        QWidget.focusInEvent(self, event)

    def focusOutEvent(self, event):
        self.model.setFocusFlag(False)
        QWidget.focusOutEvent(self, event)

    # Image scaling using keyboard, mouse wheel event
    def keyPressEvent(self, event):  # Press Control Key
        if event.key() == Qt.Key_Control:
            self.model.setCtrlFlag(True)

    def keyReleaseEvent(self, event):  # Release Control Key
        if event.key() == Qt.Key_Control:
            self.model.setCtrlFlag(False)

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
        if self.model.getDrawFlag() is False:
            return
        x_pos = event.x()
        y_pos = event.y()
        self.model.setCurPos([x_pos, y_pos])
        text = '[ {x_pos}, {y_pos} ] {draw}'.format(x_pos=x_pos, y_pos=y_pos, draw = self.model.getDrawFlag())
        self.statusBar.showMessage(text)
        try:
            self.draw()
        except:
            print('error')
        
    def mouseReleaseEvent(self, event):
        if self.model.getDrawFlag() is False:
            return            

        pos = [event.x(), event.y()]
        points = self.model.getCurPoints()
        tracking = self.label_Canvas.hasMouseTracking()

        if len(points) == 0:
            self.model.setCurPoints(pos)

        if tracking:
            if self.model.isKeepTracking():
                if points[0] == self.model.getPrePos():
                    self.model.setKeepTracking(False)
                    self.stopMouseTracking()
                    self.model.setDrawFlag(False)
                    dlg = AddLabelDialog(self.listWidget_LabelList, self.model)
                    dlg.exec_()
                    self.model.setCurShapeToDict()
                else:
                    self.model.setCurPoints(self.model.getPrePos())
            else:
                self.stopMouseTracking()
                self.model.setCurPoints(self.model.getCurPos())
                self.model.setDrawFlag(False)
                dlg = AddLabelDialog(self.listWidget_LabelList, self.model)
                dlg.exec_()
                self.model.setCurShapeToDict()

        if not tracking:
            self.model.setPrePos(pos)
            self.startMouseTracking()
            
    def draw(self):
        draw_type = self.model.getCurShapeType()
        img, w, h, c = self.model.getImgScaled()

        draw_img = img.copy()
        draw_img = QImage(draw_img.data, w, h, w * c, QImage.Format_RGB888)
        draw_img = QPixmap.fromImage(draw_img)

        painter = QPainter(draw_img)

        pre_pos = self.model.getPrePos()
        cur_pos = self.model.getCurPos()

        painter.setPen(QPen(Qt.green, 3, Qt.SolidLine))
        if draw_type == 'No Draw':
            return
        elif draw_type == 'Polygon':
            src_x = self.model.getCurPoints()[-1][0]#self.polygon_list[-1][0]
            src_y = self.model.getCurPoints()[-1][1]#self.polygon_list[-1][1]
            click_range = 10
            start_point = self.model.getCurPoints()[0]#self.polygon_list[0]
            if cur_pos[0] < start_point[0]+click_range and cur_pos[0] > start_point[0]-click_range:
                if cur_pos[1] < start_point[1]+click_range and cur_pos[1] > start_point[1]-click_range:
                    cur_pos[0] = start_point[0]
                    cur_pos[1] = start_point[1]
            self.model.setCurPos([cur_pos[0], cur_pos[1]])
            self.model.setPrePos([cur_pos[0], cur_pos[1]])
            dst_x = cur_pos[0]
            dst_y = cur_pos[1]

            painter.setPen(QPen(Qt.green, 3, Qt.SolidLine))
            painter.drawLine(src_x, src_y, dst_x, dst_y)

            painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
            painter.drawPoint(src_x, src_y)
            painter.drawPoint(start_point[0], start_point[1])

        elif draw_type == 'Gesture Polygon':
            pass
        elif draw_type == 'Rectangle':
            x_pos = pre_pos[0]
            y_pos = pre_pos[1]
            width = cur_pos[0] - x_pos
            height = cur_pos[1] - y_pos
            painter.drawRect(x_pos, y_pos, width, height)

        elif draw_type == 'Circle':
            try:
                rad = math.sqrt(math.pow(pre_pos[0]-cur_pos[0], 2) + math.pow(pre_pos[1]-cur_pos[1], 2))
            except:
                rad = 0
            x_pos = pre_pos[0] - rad
            y_pos = pre_pos[1] - rad
            painter.drawEllipse(x_pos, y_pos, rad*2, rad*2)

        elif draw_type == 'Line':
            src_x = pre_pos[0]
            src_y = pre_pos[1]
            dst_x = cur_pos[0]
            dst_y = cur_pos[1]
            painter.drawLine(src_x, src_y, dst_x, dst_y)
            
        elif draw_type == 'Dot':
            painter.drawPoint(cur_pos[0], cur_pos[1])

        painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
        painter.drawPoint(pre_pos[0], pre_pos[1])
        painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
        painter.drawPoint(cur_pos[0], cur_pos[1])
        painter.end()
        self.label_Canvas.setPixmap(draw_img)

    def drawPoly(self):
        self.model.setDrawFlag(True)
        self.model.setCurShapeType('Polygon')
        self.model.resetCurPoints()
        self.model.setKeepTracking(True)
        self.stopMouseTracking()

    def drawGesturePoly(self):
        self.model.setDrawFlag(True)
        self.model.setCurShapeType('Gesture Polygon')
        self.model.resetCurPoints()
        self.stopMouseTracking()

    def drawRect(self):
        self.model.setDrawFlag(True)
        self.model.setCurShapeType('Rectangle')
        self.model.resetCurPoints()
        self.model.setKeepTracking(False)
        self.stopMouseTracking()

    def drawCircle(self):
        self.model.setDrawFlag(True)
        self.model.setCurShapeType('Circle')
        self.model.resetCurPoints()
        self.model.setKeepTracking(False)
        self.stopMouseTracking()

    def drawLine(self):
        self.model.setDrawFlag(True)
        self.model.setCurShapeType('Line')
        self.model.resetCurPoints()
        self.model.setKeepTracking(False)
        self.stopMouseTracking()

    def drawDot(self):
        self.model.setDrawFlag(True)
        self.model.setCurShapeType('Dot')
        self.model.resetCurPoints()
        self.model.setKeepTracking(False)
        self.stopMouseTracking()

    def stopMouseTracking(self):
        self.label_Canvas.setMouseTracking(False)
        self.model.setTracking(False)

    def startMouseTracking(self):
        self.label_Canvas.setMouseTracking(True)
        self.model.setTracking(True)

    def retouch(self):
        test = self.model.getAnnotInfo()
        print(test)
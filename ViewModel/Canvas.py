import os
import math
import copy

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.ImageProc import *
from Utils.AutoAnnotation import *
from Utils.ConvertAnnotation import *
from ViewModel.AddLabelDialog import AddLabelDialog

class Canvas(QWidget):
    def __init__(self, view, model):
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
        self.action_Open.triggered.connect(self.openFile)
        self.action_Save.triggered.connect(self.saveJson)

        self.action_Polygon.triggered.connect(self.drawPoly)
        self.action_Gesture_Polygon.triggered.connect(self.drawGesturePoly)
        self.action_Rectangle.triggered.connect(self.drawRect)
        self.action_Circle.triggered.connect(self.drawCircle)
        self.action_Line.triggered.connect(self.drawLine)
        self.action_Dot.triggered.connect(self.drawDot)

        self.action_Zoom_In.triggered.connect(self.zoomInImage)
        self.action_Zoom_Out.triggered.connect(self.zoomOutImage)

        self.setFocusPolicy(Qt.ClickFocus)

    def initData(self, model):
        self.model = model
        self.model.setCtrlFlag(False)
        self.model.setMenuFlag(False)
        self.model.setFocusFlag(False)
        self.menuRefresh()

    def menuRefresh(self):
        if self.model.getMenuFlag():
            self.menu_Edit.setEnabled(True)
            self.menu_Zoom.setEnabled(True)
            self.action_Save.setEnabled(True)
        else:
            self.menu_Edit.setEnabled(False)
            self.menu_Zoom.setEnabled(False)
            self.action_Save.setEnabled(False)

    def openFile(self):
        self.filePath = QFileDialog.getOpenFileName(self, 'Open File',filter='Images(*.jpg *.jpeg *.png *.json)')

        if self.filePath[0] == '' : return

        self.fileName, ext = os.path.splitext(os.path.basename(self.filePath[0]))
        self.jsonPath = os.path.dirname(self.filePath[0]) + '/' + self.fileName + '.json'
        self.initWindow()

        if ext == '.json' or os.path.isfile(self.jsonPath):
            self.model.setAnnotDict(json2Dict(self.jsonPath))
            img, w, h, c = loadImgData(self.model.getAnnotInfo()['image_path'])
            for idx in range(len(self.model.getAnnotInfo()['shapes'])) :
                add_label = QListWidgetItem(self.model.getAnnotInfo()['shapes'][idx]['label'])
                self.listWidget_LabelList.addItem(add_label)
                self.model.setLabel(self.model.getAnnotInfo()['shapes'][idx]['label'])
        else :
            img, w, h, c = loadImgData(self.filePath[0])
            self.model.setAnnotInfo(self.filePath[0], w, h)

        self.model.setImgData(img, w, h, c)
        self.img2QPixmap(img, w, h, c)
        self.setDisplayAnnot()
        self.displayImage()
        self.model.setMenuFlag(True)
        self.menuRefresh()

    def initWindow(self):
        self.model.initAnnotInfo()
        self.model.initLabelList()
        self.listWidget_LabelList.clear()

    def img2QPixmap(self, img, w, h, c):
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        qPixmap = QPixmap.fromImage(qImg)
        self.model.setImgScaled(qPixmap, w, h, c)

    def saveJson(self):
        dict2Json(self.model.getAnnotInfo(), self.jsonPath)

    def displayImage(self):
        img, w, h, c = self.model.getImgScaled()
        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)
        self.label_Canvas.setGeometry(0, 0, w, h)
        self.label_Canvas.setPixmap(img)

    def zoomInImage(self):
        img, w, h, c = self.model.getImgData()
        interpolation = 1
        self.model.setScaleRatio(self.model.getScaleRatio() * 1.25)
        ratio = self.model.getScaleRatio()

        if ratio > 3.05 : self.model.setScaleRatio(3.05)

        if ratio > 0.99 and ratio < 1.001 : self.model.setScaleRatio(1.0)

        if ratio <= 3.05 :
            img, w, h, c = resizeImage(img, self.model.getScaleRatio(), interpolation)
            self.img2QPixmap(img, w, h, c)

        self.setDisplayAnnot()
        self.displayImage()

    def zoomOutImage(self):
        img, w, h, c = self.model.getImgData()
        interpolation = 0
        self.model.setScaleRatio(self.model.getScaleRatio() * 0.8)
        ratio = self.model.getScaleRatio()

        if ratio < 0.21: self.model.setScaleRatio(0.21)

        if ratio > 0.99 and ratio < 1.001 : self.model.setScaleRatio(1.0)

        if ratio >= 0.21:
            img, w, h, c = resizeImage(img, self.model.getScaleRatio(), interpolation)
            self.img2QPixmap(img, w, h, c)

        self.setDisplayAnnot()
        self.displayImage()
    
    def focusInEvent(self,event):
        self.model.setFocusFlag(True)
        QWidget.focusInEvent(self, event)

    def focusOutEvent(self, event):
        self.model.setFocusFlag(False)
        QWidget.focusOutEvent(self, event)

    # Image scaling using keyboard, mouse wheel event
    def keyPressEvent(self, event):  # Press Control Key
        if event.key() == Qt.Key_Control: self.model.setCtrlFlag(True)
        if event.key() == (Qt.Key_Control and Qt.Key_O) : self.openFile()
        if event.key() == (Qt.Key_Control and Qt.Key_S) : self.saveJson()

    def keyReleaseEvent(self, event):  # Release Control Key
        if event.key() == Qt.Key_Control: self.model.setCtrlFlag(False)

    def wheelEvent(self, event):       # Move Mouse Wheel
        if not self.model.getFocusFlag(): return
        if self.model.getImgData() is None: return
        if not self.model.getCtrlFlag(): return

        if event.angleDelta().y() > 0 : self.zoomInImage()
        elif event.angleDelta().y() < 0 : self.zoomOutImage()

    def contextMenuEvent(self, event):
        if self.model.getImgData() is None: return

        menu = QMenu(self)
        action_Polygon = menu.addAction('Polygon')
        action_Gesture_Polygon = menu.addAction('Gesture Polygon')
        action_Rectangle = menu.addAction('Rectangle')
        action_Circle = menu.addAction('Circle')
        action_Line = menu.addAction('Line')
        action_Dot = menu.addAction('Dot')

        action = menu.exec(self.mapToGlobal(event.pos()))
        if action == action_Polygon: self.drawPoly()
        if action == action_Gesture_Polygon: self.drawGesturePoly()
        if action == action_Rectangle: self.drawRect()
        if action == action_Circle: self.drawCircle()
        if action == action_Line: self.drawLine()
        if action == action_Dot: self.drawDot()

    def mouseMoveEvent(self, event):
        cur_pos = [event.x(), event.y()]
        self.model.setCurPos(cur_pos)
        draw_flag = self.model.getDrawFlag()
    
        text = '[ {x_pos}, {y_pos} ] {draw_flag}'.format(x_pos=cur_pos[0], y_pos=cur_pos[1], draw_flag = draw_flag)
        self.statusBar.showMessage(text)

        if draw_flag is True:
            self.draw()

    def mouseReleaseEvent(self, event):
        if self.model.getDrawFlag() is False:
            return

        pos = [event.x(), event.y()]

        img, w, h, c = self.model.getImgScaled()
        points = self.model.getCurPoints()

        # 초기화된 상태라면 첫 클릭 시 좌표를 시작 좌표로 입력
        if points == []:
            self.model.setCurPoints(pos)

        # Draw Polygon을 위한 이어그리기 플래그
        tracking_flag = self.model.isTracking()
        keep_tracking_flag = self.model.isKeepTracking()

        if tracking_flag is True:
            # Polygon일 때
            if keep_tracking_flag is True:
                points[0][0] = int(points[0][0]*w)
                points[0][1] = int(points[0][1]*h)

                # 시작점을 클릭하면 그리기 종료하는 코드
                if points[0] == self.model.getPrePos():
                    keep_tracking_flag = False
                    self.model.setKeepTracking(keep_tracking_flag)
                    self.model.setDrawFlag(False)
                    self.stopMouseTracking()

                # 시작점이 아니라면 그리기 계속
                else:
                    self.model.setCurPoints(self.model.getPrePos())
            else:
                self.stopMouseTracking()
                self.model.setCurPoints(self.model.getCurPos())
                self.model.setDrawFlag(False)

            # Rect, Circle, Line, Dot일 때
            if keep_tracking_flag is False:
                dlg = AddLabelDialog(self.listWidget_LabelList, self.model)
                dlg.exec_()
                if self.model.getCurLabel() != '':
                    self.model.setCurShapeToDict()
                self.model.setCurLabel('')
                
        else:
            self.model.setPrePos(pos)
            self.startMouseTracking()

        self.setDisplayAnnot()
        self.displayImage()
            
    def draw(self):
        draw_type = self.model.getCurShapeType()
        img, w, h, c = self.model.getImgScaled()

        draw_img = img.copy()

        painter = QPainter(draw_img)

        pre_pos = self.model.getPrePos()
        cur_pos = self.model.getCurPos()
        cur_points = self.model.getCurPoints()
        click_range = 10

        # 정규화 해제
        for point in cur_points:
            point[0] *= w
            point[1] *= h

        painter.setPen(QPen(Qt.green, 3, Qt.SolidLine))

        if draw_type == 'Polygon':
            if cur_points == []:
                painter.end()
                return

            # 시작점 저장
            start_point = cur_points[0]
            start_point[0] = int(start_point[0])
            start_point[1] = int(start_point[1])

            # click_range에 따라 start_point에 현재 좌표 세팅
            if cur_pos[0] < start_point[0]+click_range and cur_pos[0] > start_point[0]-click_range:
                if cur_pos[1] < start_point[1]+click_range and cur_pos[1] > start_point[1]-click_range:
                    cur_pos[0] = start_point[0]
                    cur_pos[1] = start_point[1]

            # 이전까지 그린 선들 표시
            pre = cur_points[0]
            for point in cur_points:
                cur = point
                painter.setPen(QPen(Qt.green, 3, Qt.SolidLine))
                painter.drawLine(pre[0], pre[1], cur[0], cur[1])
                painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
                painter.drawPoint(pre[0], pre[1])
                painter.drawPoint(cur[0], cur[1])
                pre = point

            # 현재 그리려고 하는 선 Draw
            src_x = cur_points[-1][0]
            src_y = cur_points[-1][1]
            dst_x = cur_pos[0]
            dst_y = cur_pos[1]

            painter.setPen(QPen(Qt.green, 3, Qt.SolidLine))
            painter.drawLine(src_x, src_y, dst_x, dst_y)
            painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
            painter.drawPoint(src_x, src_y)
            painter.drawPoint(start_point[0], start_point[1])

            # 현재 좌표에서 다음에 계속 그리기 위함
            self.model.setPrePos([cur_pos[0], cur_pos[1]])

        elif draw_type == 'Rectangle':
            width = cur_pos[0] - pre_pos[0]
            height = cur_pos[1] - pre_pos[1]
            painter.drawRect(pre_pos[0], pre_pos[1], width, height)

        elif draw_type == 'Circle':
            try:
                rad = math.sqrt(math.pow(pre_pos[0]-cur_pos[0], 2) + math.pow(pre_pos[1]-cur_pos[1], 2))
            except:
                rad = 0
            x_pos = pre_pos[0] - rad
            y_pos = pre_pos[1] - rad
            painter.drawEllipse(x_pos, y_pos, rad*2, rad*2)

        elif draw_type == 'Line':
            painter.drawLine(pre_pos[0], pre_pos[1], cur_pos[0], cur_pos[1])
            
        elif draw_type == 'Dot':
            painter.drawPoint(cur_pos[0], cur_pos[1])

        # 시작점, 끝점 빨간 점으로 표시
        painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
        painter.drawPoint(pre_pos[0], pre_pos[1])
        painter.drawPoint(cur_pos[0], cur_pos[1])

        painter.end()

        self.label_Canvas.setPixmap(draw_img)

    def drawPoly(self):
        self.model.setDrawFlag(True)
        self.model.setKeepTracking(True)
        self.model.setCurShapeType('Polygon')

        self.model.resetCurPoints()
        self.stopMouseTracking()

    def drawGesturePoly(self):
        self.model.setCurShapeType('Gesture Polygon')
        self.model.resetCurPoints()
        self.stopMouseTracking()

        dlg = AddLabelDialog(self.listWidget_LabelList, self.model)
        dlg.exec_()
        if self.model.getCurLabel() != '' :
            self.model.setCurShapeToDict()

        self.model.setCurPoints([0.5, 0.65], True)
        x_pos = 0.4
        y_pos = 0.5
        nb_points = 21
        for idx in range(1, nb_points):
            if idx%4 == 1:
                x_pos += 0.05
                y_pos = 0.5
            pos = [round(x_pos, 2), round(y_pos, 2)]
            self.model.setCurPoints(pos, True)
            y_pos -= 0.05
        self.model.setCurShapeToDict()
        self.setDisplayAnnot()
        self.displayImage()
        
    def drawRect(self):
        self.model.setDrawFlag(True)
        self.model.setKeepTracking(False)
        self.model.setCurShapeType('Rectangle')

        self.model.resetCurPoints()
        self.stopMouseTracking()

    def drawCircle(self):
        self.model.setDrawFlag(True)
        self.model.setKeepTracking(False)
        self.model.setCurShapeType('Circle')

        self.model.resetCurPoints()
        self.stopMouseTracking()

    def drawLine(self):
        self.model.setDrawFlag(True)
        self.model.setKeepTracking(False)
        self.model.setCurShapeType('Line')

        self.model.resetCurPoints()
        self.stopMouseTracking()

    def drawDot(self):
        self.model.setDrawFlag(True)
        self.model.setKeepTracking(False)
        self.model.setCurShapeType('Dot')

        self.model.resetCurPoints()
        self.stopMouseTracking()

    def stopMouseTracking(self):
        self.model.setTracking(False)
        self.setMouseTracking(False)
        self.label_Canvas.setMouseTracking(False)

    def startMouseTracking(self):
        self.model.setTracking(True)
        self.setMouseTracking(True)
        self.label_Canvas.setMouseTracking(True)

    def setDisplayAnnot(self):
        dict = self.model.getAnnotInfo()
        sImg, w, h, c = self.model.getImgScaled()
        
        draw_img = sImg

        painter = QPainter(draw_img)
        
        for shape in dict['shapes']:
            shape_type = shape['shape_type']
            points = copy.deepcopy(shape['points'])

            # 정규화 해제
            for idx in range(len(points)):
                points[idx][0] *= w
                points[idx][1] *= h
                        
            if shape_type == 'Polygon':
                painter.setPen(QPen(Qt.magenta, 3, Qt.SolidLine))
                pre = points[0]
                for point in points:
                    cur = point
                    painter.drawLine(pre[0], pre[1], cur[0], cur[1])
                    pre = point
                painter.drawLine(points[0][0], points[0][1], pre[0], pre[1])

            elif shape_type == 'Gesture Polygon':
                painter.setPen(QPen(Qt.cyan, 3, Qt.SolidLine))
                nb_points = 21
                for idx in range(1, nb_points):
                    if idx%4 == 1:
                        src_pos = points[idx]
                        continue
                    dst_pos = points[idx]
                    painter.drawLine(src_pos[0], src_pos[1], dst_pos[0], dst_pos[1])

                painter.drawLine(points[0][0], points[0][1], points[1][0], points[1][1])
                painter.drawLine(points[0][0], points[0][1], points[5][0], points[5][1])
                painter.drawLine(points[0][0], points[0][1], points[17][0], points[17][1])
                painter.drawLine(points[5][0], points[5][1], points[9][0], points[9][1])
                painter.drawLine(points[9][0], points[9][1], points[13][0], points[13][1])
                painter.drawLine(points[13][0], points[13][1], points[17][0], points[17][1])

            elif shape_type == 'Rectangle':
                width = (points[1][0] - points[0][0])
                height = (points[1][1] - points[0][1])

                color = QPen(Qt.blue, 3, Qt.SolidLine)
                painter.setPen(color)
                painter.drawRect(points[0][0], points[0][1], width, height)

            elif shape_type == 'Circle':
                rad = math.sqrt(math.pow(points[0][0]-points[1][0], 2) + math.pow(points[0][1]-points[1][1], 2))

                color = QPen(Qt.red, 3, Qt.SolidLine)
                painter.setPen(color)
                painter.drawEllipse(points[0][0]-rad, points[0][1]-rad, rad*2, rad*2)

            elif shape_type == 'Line':
                color = QPen(Qt.yellow, 3, Qt.SolidLine)
                painter.setPen(color)
                painter.drawLine(points[0][0], points[0][1], points[1][0], points[1][1])

            elif shape_type == 'Dot':
                painter.drawPoint(points[0][0], points[0][1])

        painter.end()

        self.model.setImgScaled(draw_img, w, h, c)
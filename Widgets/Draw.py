from PyQt5.QtWidgets import *
from pyparsing import opAssoc
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from Widgets.Display import *
from Widgets.AddObjectDialog import *

class Draw(QWidget):
    def __init__(self, view, Model):
        super().__init__()

        self.Model = Model

        self.canvas = QLabel(self)
        self.scroll_area = view[0]
        self.label_list = view[1]
        self.object_list = view[2]

        # Init Display Class
        self.Display = Display(self.canvas, self.scroll_area, self.Model)


    # ----- Set View -----
    def setCanvas(self):
        img, w, h, c = self.Model.getImgScaled()

        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)

        self.Display.displayImage(img, w, h)


    # ----- Context Menu Event -----
    def contextMenuEvent(self, event):
        pass    
    
    
    # ----- Mouse Event -----
    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        print("아")

    def mouseReleaseEvent(self, event):
        print("킹")
        # Draw 활성화 되었을 때만 기능 작동
        if self.Model.getDrawFlag() is False:
            return

        # 마우스 뗏을 때 좌표 저장
        pos = [event.x(), event.y()]

        img, w, h, c = self.Model.getImgScaled()
        points = self.Model.getCurPoints()

        # 초기화된 상태라면 첫 클릭 시 좌표를 시작 좌표로 입력
        if points == [] and self.Model.getCurShapeType() is not 'Dot':
            self.Model.addCurPoint(pos)

        # 플래그 상태 확인
        tracking_flag = self.Model.isTracking()
        keep_tracking_flag = self.Model.isKeepTracking()

        # 그리기 시작
        if tracking_flag is False:
            self.Model.setPrePos(pos)
            self.setTracking(tracking = True, keep_tracking = False)

        # 그리기 완료 시
        else:
            # Polygon일 때
            if keep_tracking_flag is True:
                points[0][0] = int(points[0][0]*w)
                points[0][1] = int(points[0][1]*h)

                # 시작점을 클릭하면 그리기 종료하는 코드
                if points[0] == self.Model.getPrePos():
                    self.setTracking(tracking = False, keep_tracking = False)
                    self.Model.setDrawFlag(False)

                # 시작점이 아니라면 그리기 계속
                else:
                    self.Model.addCurPoint(self.Model.getPrePos())

            # Rect, Circle, Line, Dot일 때
            else:
                self.setTracking(tracking = False, keep_tracking = False)
                self.Model.setDrawFlag(False)
                self.Model.addCurPoint(self.Model.getCurPos())

            # 그리기 종료 후 Object 추가
            if keep_tracking_flag is False:
                self.addObject()

    def setTracking(self, tracking, keep_tracking=False):
        self.Model.setTracking(tracking)
        self.Model.setKeepTracking(keep_tracking)
        self.setMouseTracking(tracking)
        self.canvas.setMouseTracking(tracking)


    # ----- Draw -----
    def draw(self):
        pass
    
    def addObject(self):
        dlg = AddObjectDialog([self.label_list, self.object_list], self.Model)
        dlg.exec_()

        if self.Model.getCurLabel() != '':
            self.Model.setCurShapeToDict()

        self.Model.setCurLabel('')


    # ----- Retouch -----
    def movePoint(self):
        pass

    
    # ----- Object List Click Event -----
    def objectClicked(self):
        pass

    def objectDoubleClicked(self):
        pass


    # ----- Delete -----
    def deleteObject(self):
        pass
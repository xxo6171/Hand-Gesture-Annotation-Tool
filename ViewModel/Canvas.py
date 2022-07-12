from tkinter import W
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.ImageProc import *
from Utils.AutoAnnotation import *

class Canvas(QWidget):
    def __init__(self, view, model):
        # Initialize
        super().__init__()
        self.flag = False

        self.label_Canvas = QLabel(self)

        self.action_Open = view[0]

        self.menu_Edit = view[1]
        self.menu_Zoom = view[2]
        self.action_Save = view[3]

        self.action_Line = view[4]
        self.statusBar = view[5]

        self.model = model
        self.menuRefresh(self.flag)

        #Triggered connect
        self.action_Open.triggered.connect(self.openImage)
        self.action_Line.triggered.connect(self.drawLine)

        self.setMouseTracking(True)

    # Refresh menu
    def menuRefresh(self, flag):
        if flag: self.menu_Edit.setEnabled(True);self.menu_Zoom.setEnabled(True);self.action_Save.setEnabled(True);
        else:self.menu_Edit.setEnabled(False);self.menu_Zoom.setEnabled(False);self.action_Save.setEnabled(False);

    def openImage(self):
        self.filepath = QFileDialog.getOpenFileName(self, 'Open File',filter='Images(*.jpg *.jpeg *.png)')
        if self.filepath[0] != '' :
            img = loadImgData(self.filepath[0])

            # !!! Auto Annotation 부분 !!!
            # img, landmark = autoAnnotation(img)
            h, w, c = img.shape  # height, width, channel
            qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
            qPixmap = QPixmap.fromImage(qImg)

            self.model.setImgData(qPixmap, w, h)
            self.model.setImgScaled(qPixmap, w, h)
            self.displayImage(qPixmap, w, h)

    def displayImage(self, img, w, h):
        self.setMinimumSize(w, h)
        self.setMaximumSize(w, h)       
        self.label_Canvas.setGeometry(0, 0, w, h)
        self.label_Canvas.setPixmap(img)

        self.flag = True 
        self.menuRefresh(self.flag)
    
    def drawLine(self):
        self.model.setDrawFlag('Line')
    
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
            self.label_Canvas.setMouseTracking(False)
        else:
            past_x_pos = event.x()
            past_y_pos = event.y()
            self.model.setPrePos([past_x_pos, past_y_pos])
            self.label_Canvas.setMouseTracking(True)
    
    def draw(self):
        flag = self.model.getDrawFlag()
        img, w, h = self.model.getImgScaled()

        draw_img = img.copy()
        painter = QPainter(draw_img)
        painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))

        pre_pos = self.model.getPrePos()
        cur_pos = self.model.getCurPos()
        if flag == 'No Draw':
            return
        elif flag == 'Line':
            painter.drawLine(pre_pos[0], pre_pos[1], cur_pos[0], cur_pos[1])
            painter.end()
        
        self.displayImage(draw_img, w, h)
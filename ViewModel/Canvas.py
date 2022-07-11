from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.ImageProc import ImageProc

class Canvas(QMainWindow):
    def __init__(self, view, model):
        # Initialize
        super().__init__()
        self.flag = False

        self.action_Open, self.label_Canvas, self.scrollArea_Canvas = view[0],view[1],view[2]
        self.menu_Edit, self.menu_Zoom, self.action_Save = view[3],view[4],view[5]

        self.model = model
        self.imgProc = ImageProc()
        self.menuRefresh(self.flag)
        #Triggered connect
        self.action_Open.triggered.connect(self.openImage)

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
            img = self.imgProc.loadImgData(self.filepath[0])
            self.model.setImgData(img)
            self.displayImage(img)

    def displayImage(self, img):
        h, w, c = img.shape  # height, width, channel
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        self.qPixmap = QPixmap.fromImage(qImg)
        self.label_Canvas.setPixmap(self.qPixmap)
        self.flag = True
        self.menuRefresh(self.flag)
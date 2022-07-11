from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Utils.ImageProc import ImageProc

class Canvas(QMainWindow):
    def __init__(self, view, model):
        #Initialize
        self.action_Open = view[0]
        self.label_Canvas = view[1]
        self.scrollArea_Canvas = view[2]
        '''
        self.list_listWidget = view[0]
        self.add_btn = view[1]
        self.delete_btn = view[2]
        self.string_lineEdit = view[3]
        '''
        self.model = model
        self.imgProc = ImageProc()

        #Triggered connect
        self.action_Open.triggered.connect(self.openImage)

        #Widget setting
        self.label_Canvas.setAlignment(Qt.AlignCenter)
        self.scrollArea_Canvas.setWidget(self.label_Canvas)

    def openImage(self):
        self.filepath = QFileDialog.getOpenFileName(self, 'Open File',filter='Images(*.jpg *.jpeg *.png)')
        if self.filepath[0] != '' :
            img = self.imgProc.loadImgData(self.filepath[0])
            self.model.setImgData(img)
            h, w, c = img.shape  # height, width, channel
            qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
            self.qPixmap = QPixmap.fromImage(qImg)
            self.label_Canvas.setPixmap(self.qPixmap)
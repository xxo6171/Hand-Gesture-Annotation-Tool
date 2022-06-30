import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

dir = 'UI/Main GUI.ui'
form_class = uic.loadUiType(dir)[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
        ----------------------------------------------------------------------------
                            이 부분에 시그널을 입력한다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수( 슬롯 )로 작성한다.
        ----------------------------------------------------------------------------
        '''
        # ==== Canvas Area ====
        self.test_pic_dir = 'Resource\Image\kitty.jpg'
        self.qPixmap_Canvas = QPixmap(self.test_pic_dir)
        self.label_Canvas.setPixmap(self.qPixmap_Canvas)

        # ==== File Menu Area ====
        self.action_Open.triggered.connect(self.openImage)

    """
    ----------------------------------------------------------------------------
                            이 부분에 슬롯을 입력한다.
               시그널과 연결된 작동 함수 부분을 멤버함수 형태로 작성한다.
    ----------------------------------------------------------------------------
    """

    # ==== file Menu Area ====
    def openImage(self):
        extension_Filter = '*.jpg, *.jpeg, *.png'
        img_Dir = QFileDialog.getOpenFileName(self, 'Open File', filter=extension_Filter)
        self.qPixmap_Canvas = QPixmap(img_Dir[0])

        width = self.qPixmap_Canvas.width()
        height = self.qPixmap_Canvas.height()
        if(height>width):
            self.qPixmap_Canvas_Scaled = self.qPixmap_Canvas.scaledToHeight(810)
        else:
            self.qPixmap_Canvas_Scaled = self.qPixmap_Canvas.scaledToWidth(1280)
        self.label_Canvas.setPixmap(self.qPixmap_Canvas_Scaled)

if __name__=='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
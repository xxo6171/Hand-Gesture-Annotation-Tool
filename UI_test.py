from pickle import GLOBAL
import sys
import cv2
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# ====== Global Variable =====
GLOBAL_label_List = []

# ======= Add Label Dialog =======
add_label_UI_dir = 'UI/Add Lable Dialog.ui'
add_label__form_class = uic.loadUiType(add_label_UI_dir)[0]

class AddLabelDialog(QDialog, add_label__form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global GLOBAL_label_List

        for label in GLOBAL_label_List:
            new_Item = QListWidgetItem(label)
            self.listWidget_LabelList.addItem(new_Item)
        '''
        ----------------------------------------------------------------------------
                            이 부분에 시그널을 입력한다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수( 슬롯 )로 작성한다.
        ----------------------------------------------------------------------------
        '''
        # ==== Button Area ====
        self.pushButton_OK.clicked.connect(self.set_Label)
        self.pushButton_Cancel.clicked.connect(self.close_Dialog)

    '''
    ----------------------------------------------------------------------------
                            이 부분에 슬롯을 입력한다.
               시그널과 연결된 작동 함수 부분을 멤버함수 형태로 작성한다.
    ----------------------------------------------------------------------------
    '''

    # ==== Button Area ====
    def set_Label(self):
        label_Name = self.lineEdit_NewLabel.text()
        
        if label_Name not in GLOBAL_label_List:
            label_List_New_Item = QListWidgetItem(label_Name)
            self.listWidget_LabelList.addItem(label_Name)
            GLOBAL_label_List.append(label_Name)
        self.lineEdit_NewLabel.clear()

    def close_Dialog(self):
        self.close()

# ======= Image Open from IP Camera Dialog =======
image_from_camera_UI_dir = 'UI/Image From Camera.ui'
image_from_camera_form_class = uic.loadUiType(image_from_camera_UI_dir)[0]

class ImageFromCameraDialog(QDialog, image_from_camera_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
        ----------------------------------------------------------------------------
                            이 부분에 시그널을 입력한다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수( 슬롯 )로 작성한다.
        ----------------------------------------------------------------------------
        '''
        self.pushButton_Capture.clicked.connect(self.image_Capture)
        self.pushButton_Cancel.clicked.connect(self.close_Dialog)

    '''
    ----------------------------------------------------------------------------
                            이 부분에 슬롯을 입력한다.
               시그널과 연결된 작동 함수 부분을 멤버함수 형태로 작성한다.
    ----------------------------------------------------------------------------
    '''
    def image_Capture(self):
        capture = cv2.VideoCapture(1)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

        ret, frame = capture.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, c = frame.shape
        qImg = QImage(frame.data, w, h, w*c, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.label_CaptureImage.setPixmap(pixmap)
        self.label_CaptureImage.show()

    def close_Dialog(self):
        self.close()



# ======= Main Window =======
mainUI_dir = 'UI/Main GUI.ui'
main_form_class = uic.loadUiType(mainUI_dir)[0]

class HandAnnot(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global GLOBAL_label_List
        
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
        
        # ==== TEST Menu Area ====
        self.action_Add_Label.triggered.connect(self.openDialog_addLabel)
        self.action_Delete_Label.triggered.connect(self.deleteLabel)

        self.action_Image_from_IP_Camera.triggered.connect(self.openDialog_imgFromCamera)

    '''
    ----------------------------------------------------------------------------
                            이 부분에 슬롯을 입력한다.
               시그널과 연결된 작동 함수 부분을 멤버함수 형태로 작성한다.
    ----------------------------------------------------------------------------
    '''
    # ==== File Menu Area ====
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

    # ==== TEST Menu Area ====
    def openDialog_addLabel(self):
        dlg = AddLabelDialog()
        dlg.exec_()

        self.listWidget_LabelList.clear()
        for label in GLOBAL_label_List:
            new_Item = QListWidgetItem(label)
            self.listWidget_LabelList.addItem(new_Item)

    def deleteLabel(self):
        print("Delete Label")

    def openDialog_imgFromCamera(self):
        dlg = ImageFromCameraDialog()
        dlg.exec_()

if __name__=='__main__':
    app = QApplication(sys.argv)
    handannot = HandAnnot()
    handannot.show()
    app.exec_()


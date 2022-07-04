from pickle import GLOBAL
import sys
import cv2
import numpy as np
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# ====== Global Variable =====
GLOBAL_label_List = []
GLOBAL_nb_cam = 1



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
class IPCameThread(QThread):
    global GLOBAL_nb_cam
    power = False
    change_pixmap = pyqtSignal(QImage)

    def run(self):
        self.power = True
        cap = cv2.VideoCapture(GLOBAL_nb_cam)

        while self.power:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                scaled_image = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.change_pixmap.emit(scaled_image)

image_from_camera_UI_dir = 'UI/Image From Camera.ui'
image_from_camera_form_class = uic.loadUiType(image_from_camera_UI_dir)[0]



class ImageFromCameraDialog(QDialog, image_from_camera_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global GLOBAL_nb_cam
        '''
        ----------------------------------------------------------------------------
                            이 부분에 시그널을 입력한다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수( 슬롯 )로 작성한다.
        ----------------------------------------------------------------------------
        '''
        self.th = IPCameThread()
        self.th.change_pixmap.connect(self.setImage)
        self.th.start()

        self.pushButton_Capture.clicked.connect(self.image_Capture)
        self.pushButton_Cancel.clicked.connect(self.close_Dialog)

    '''
    ----------------------------------------------------------------------------
                            이 부분에 슬롯을 입력한다.
               시그널과 연결된 작동 함수 부분을 멤버함수 형태로 작성한다.
    ----------------------------------------------------------------------------
    '''
    def setImage(self, scaled):
        self.label_CaptureImage.setPixmap(QPixmap.fromImage(scaled))
        self.label_CaptureImage.show()

    def image_Capture(self):
        self.th.power = False
        self.th.quit()
        
        capture = cv2.VideoCapture(GLOBAL_nb_cam)

        ret, frame = capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, c = frame.shape
            qImg = QImage(frame.data, w, h, w*c, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            
        self.close()

    def close_Dialog(self):
        self.th.power = False
        self.th.quit()
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
    # Open / Load Image
    def openImage(self):
        self.file_name, self.extension_filter = QFileDialog.getOpenFileName(self, 'Open File',
                                                                           filter='Images(*.jpg *.jpeg *.png)')
        if self.file_name != '' :
            try :
                self.loadImage(self.file_name)
            except Exception as exc:
                self.app.outputException(exc, 'An error occurred while loading the file : ')
                #Display error message box
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Error")  # 메세지창의 상단 제목
                msgBox.setIcon(QMessageBox.Critical)  # 메세지창 내부에 표시될 아이콘
                msgBox.setText("Error")  # 메세지 제목
                msgBox.setInformativeText("An error occurred while loading the file :")  # 메세지 내용
                msgBox.setStandardButtons(QMessageBox.Close)  # 메세지창의 버튼
                msgBox.setDefaultButton(QMessageBox.Close)  # 포커스가 지정된 기본 버튼

    def loadImage(self, filename):
        self.img = cv2.imread(filename)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        h, w, c = self.img.shape #height, width, channel
        qImg = QImage(self.img.data, w, h, w*c, QImage.Format_RGB888)
        self.qPixmap = QPixmap.fromImage(qImg)
        self.label_Canvas.setPixmap(self.qPixmap)

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
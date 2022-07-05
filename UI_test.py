from pickle import GLOBAL
import sys
import cv2
import mediapipe as mp
import numpy as np
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

# ====== Global Variable =====
GLOBAL_label_List = []
GLOBAL_nb_cam = 0



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

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands

        with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

            while self.power:
                ret, frame = cap.read()
                if ret:
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    # hand recognization
                    results = hands.process(rgbImage)

                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            finger1 = int(hand_landmarks.landmark[4].x * 100 )
                            finger2 = int(hand_landmarks.landmark[8].x * 100 )
                            dist = abs(finger1 - finger2)
                            cv2.putText(
                                rgbImage, text='f1=%d f2=%d dist=%d ' % (finger1,finger2,dist), org=(10, 30),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                                color=255, thickness=3)
            
                            mp_drawing.draw_landmarks(
                                rgbImage, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    # -hand recognition

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
        cap = cv2.VideoCapture(GLOBAL_nb_cam)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        global img

        ret, frame = cap.read()
        if ret:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.th.power = False
        self.th.quit()
        
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
        self.draw_flag = 0
        self.draw_type = 'No Draw'

        global img
        img = cv2.imread('')
        # Initial menu settings, Disable before loading image

        '''
        ----------------------------------------------------------------------------
                            이 부분에 시그널을 입력한다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수( 슬롯 )로 작성한다.
        ----------------------------------------------------------------------------
        '''
        # ==== Component Area ====
        # Initial menu settings, Disable before loading image

        self.flag = False
        self.menuRefresh(self.flag)

        # ==== File Menu Area ====
        self.action_Open.triggered.connect(self.openImage)

        # ==== Edit Menu Area ====
        self.action_Polygon.triggered.connect(self.drawPolygon)
        self.action_Gesture_Polygon.triggered.connect(self.drawGesturePolygon)
        self.action_Rectangle.triggered.connect(self.drawRectangle)
        self.action_Circle.triggered.connect(self.drawCircle)
        self.action_Line.triggered.connect(self.drawLine)
        self.action_Dot.triggered.connect(self.drawDot)



        #==== Zoom Menu Area ====
        self.f = 1 #ratio
        self.action_Zoom_In.triggered.connect(self.zoomInImage)
        self.action_Zoom_Out.triggered.connect(self.zoomOutImage)

        # ==== TEST Menu Area ====
        self.action_Add_Label.triggered.connect(self.openDialog_addLabel)
        self.action_Delete_Label.triggered.connect(self.deleteLabel)
        self.action_Image_from_IP_Camera.triggered.connect(self.openDialog_imgFromCamera)
        
        # ==== Canvas Area ====
        # label_Canvas
        self.scrollArea_Canvas.setWidget(self.label_Canvas)
        self.scrollArea_Canvas.setWidgetResizable(True)
        
    '''
    ----------------------------------------------------------------------------
                            이 부분에 슬롯을 입력한다.
               시그널과 연결된 작동 함수 부분을 멤버함수 형태로 작성한다.
    ----------------------------------------------------------------------------
    '''

    # ==== Component Area ====
    # Refresh menu
    def menuRefresh(self, flag):
        if flag : self.menu_Edit.setEnabled(True) ; self.menu_Zoom.setEnabled(True); self.action_Save.setEnabled(True);
        else : self.menu_Edit.setEnabled(False); self.menu_Zoom.setEnabled(False); self.action_Save.setEnabled(False);

    # ==== File Menu Area ====
    # Open / Load Image
    def openImage(self):
        self.file_name, self.extension_filter = QFileDialog.getOpenFileName(self, 'Open File',
                                                                           filter='Images(*.jpg *.jpeg *.png)')
        if self.file_name != '' : self.loadImage(self.file_name)

    def loadImage(self, filename):
        global img
        # 경로 한글 깨짐으로 인한 오류 방지 -> numpy 배열로 변환 후 decode
        img = np.fromfile(filename, np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, c = img.shape    #height, width, channel
        qImg = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
        self.qPixmap = QPixmap.fromImage(qImg)
        self.label_Canvas.setPixmap(self.qPixmap)
        self.flag = True
        self.menuRefresh(self.flag)     #Refresh menu


    # ==== Zoom Menu Area ====
    # Zoom In
    def zoomInImage(self):
        global img
        resize_img = img
        self.f = self.f * 1.25
        interpolation = cv2.INTER_LINEAR
        self.resizeImage(resize_img, self.f, interpolation)

    # Zoom Out
    def zoomOutImage(self):
        global img
        resize_img = img
        self.f = self.f * 0.8
        interpolation = cv2.INTER_AREA
        self.resizeImage(resize_img, self.f, interpolation)

    # Image resize
    def resizeImage(self, img, f, interpolation):
        resize_img = cv2.resize(img, None, fx=f, fy=f, interpolation=interpolation)
        h, w, c = resize_img.shape  # height, width, channel
        qImg = QImage(resize_img.data, w, h, w * c, QImage.Format_RGB888)
        self.qPixmap = QPixmap.fromImage(qImg)
        self.label_Canvas.setPixmap(self.qPixmap)
        self.update()

    # Image scaling using keyboard, mouse wheel event
    def keyPressEvent(self, e):         # Press Control Key
        if e.key() == Qt.Key_Control: self.bCtrl = True
        self.update()

    def keyReleaseEvent(self, e):     # Release Control Key
        if e.key() == Qt.Key_Control: self.bCtrl = False
        self.update()

    def wheelEvent(self, e):                # Move Mouse Wheel
        if self.bCtrl :
            if (e.angleDelta().y() > 0) : self.zoomInImage()        # Wheel Up
            elif (e.angleDelta().y() < 0) : self.zoomOutImage()  # Wheel Down
        self.update()

    # ==== Edit Menu Area ====
    def mouseMoveEvent(self, event):
        #self.draw(event.x(), event.y())
        text = "Mouse Point: [ {x_pos}, {y_pos} ]   Draw Type: [ {d_type} ]  Mouse Tracking: [ {mt} ]".format(x_pos=event.x(), y_pos=event.y(), d_type=self.draw_type, mt=self.scrollArea_Canvas.hasMouseTracking())
        self.statusBar.showMessage(text)

    def mouseReleaseEvent(self, event):
        if self.scrollArea_Canvas.hasMouseTracking():
            self.scrollArea_Canvas.setMouseTracking(False)
        else:
            self.scrollArea_Canvas.setMouseTracking(True)
        
    def draw(self, x_pos, y_pos):
        if self.draw_flag == 0:
            self.draw_type = 'No Draw'
        elif self.draw_flag == 1:
            pass
        elif self.draw_flag == 2:
            pass
        elif self.draw_flag == 3:
            pass
        elif self.draw_flag == 4:
            pass
        elif self.draw_flag == 5:
            pass
        elif self.draw_flag == 6:
            pass

    def drawPolygon(self):
        self.draw_flag = 1
        self.draw_type = 'Polygon'

    def drawGesturePolygon(self):
        self.draw_flag = 2
        self.draw_type = 'Gesture Polygon'

    def drawRectangle(self):
        self.draw_flag = 3
        self.draw_type = 'Rectangle'

    def drawCircle(self):
        self.draw_flag = 4
        self.draw_type = 'Circle'

    def drawLine(self):
        self.draw_flag = 5
        self.draw_type = 'Line'

    def drawDot(self):
        self.draw_flag = 6
        self.draw_type = 'Dot'


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

        global img

        if img is not None:
            h, w, c = img.shape #height, width, channel
            qImg = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
            self.qPixmap = QPixmap.fromImage(qImg)
            self.label_Canvas.setPixmap(self.qPixmap)

            GLOBAL_menubar_Flag = True
            self.menuRefresh(GLOBAL_menubar_Flag)



if __name__=='__main__':
    app = QApplication(sys.argv)
    handannot = HandAnnot()
    handannot.show()
    app.exec_()
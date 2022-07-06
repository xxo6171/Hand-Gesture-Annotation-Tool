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
        cap = cv2.VideoCapture(GLOBAL_nb_cam, cv2.CAP_DSHOW)

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
        cap = cv2.VideoCapture(GLOBAL_nb_cam, cv2.CAP_DSHOW)
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

        img = None
        # Initial menu settings, Disable before loading image

        '''
        ----------------------------------------------------------------------------
                            이 부분에 시그널을 입력한다.
        시그널이 작동할 때 실행될 기능은 보통 이 클래스의 멤버함수( 슬롯 )로 작성한다.
        ----------------------------------------------------------------------------
        '''
        # ==== Component Area ====
        # Control key flag
        self.bCtrl = False
        # Initial menu settings, Disable before loading image
        self.flag = False
        self.menuRefresh(self.flag)

        # ==== File Menu Area ====
        self.action_Open.triggered.connect(self.openImage)
        self.action_Save.triggered.connect(self.saveImg2Json)

        # ==== Edit Menu Area ====
        self.action_Polygon.triggered.connect(self.drawPolygon)
        self.action_Gesture_Polygon.triggered.connect(self.drawGesturePolygon)
        self.action_Rectangle.triggered.connect(self.drawRectangle)
        self.action_Circle.triggered.connect(self.drawCircle)
        self.action_Line.triggered.connect(self.drawLine)
        self.action_Dot.triggered.connect(self.drawDot)

        #==== Zoom Menu Area ====
        self.f = 1 #ratio
        self.bCtrl = False
        self.action_Zoom_In.triggered.connect(self.zoomInImage)
        self.action_Zoom_Out.triggered.connect(self.zoomOutImage)

        # ==== TEST Menu Area ====
        self.action_Add_Label.triggered.connect(self.openDialog_addLabel)
        self.action_Delete_Label.triggered.connect(self.deleteLabel)
        self.action_Image_from_IP_Camera.triggered.connect(self.openDialog_imgFromCamera)
        
        # ==== Canvas Area ====
        # label_Canvas
        self.label_Canvas.setAlignment(Qt.AlignCenter)
        self.scrollArea_Canvas.setWidget(self.label_Canvas)
        self.past_x_pos = 0
        self.past_y_pos = 0
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

    def saveImg2Json(self):
        self.save_file_name, self.extension_filter = QFileDialog.getSaveFileName(self,'Open File',
                                                                                filter='*.json')

    # ==== Zoom Menu Area ====
    # Zoom In
    def zoomInImage(self):
        global img
        resize_img = img
        self.f = self.f * 1.25
        interpolation = cv2.INTER_LINEAR
        if self.f > 3.05 : self.f = 3.05
        if self.f <= 3.05 : self.resizeImage(resize_img, self.f, interpolation)
        print('배율 = ', self.f)

    # Zoom Out
    def zoomOutImage(self):
        global img
        resize_img = img
        self.f = self.f * 0.8
        interpolation = cv2.INTER_AREA
        if self.f < 0.21 : self.f = 0.21
        if self.f >= 0.21 : self.resizeImage(resize_img, self.f, interpolation)
        print('배율 = ', self.f)

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
        global img
        if (img is not None) and (self.bCtrl) and  (e.angleDelta().y() > 0) : self.zoomInImage()        # Wheel Up
        elif (img is not None) and (self.bCtrl) and  (e.angleDelta().y() < 0) : self.zoomOutImage()  # Wheel Down
        self.update()

    # ==== Edit Menu Area ====
    def mouseMoveEvent(self, event):
        global img
        if img is None:
            return
        self.cur_x_pos = event.x()
        self.cur_y_pos = event.y()

        text = "Mouse Point: [ {x_pos}, {y_pos} ]   Draw Type: [ {d_type} ]  Mouse Tracking: [ {mt} ]".format(x_pos=self.cur_x_pos, y_pos=self.cur_y_pos, d_type=self.draw_type, mt=self.hasMouseTracking())
        self.statusBar.showMessage(text)
        # self.draw_Line(x_pos, y_pos)
        self.draw()

    def mouseReleaseEvent(self, event):
        if self.draw_flag == 0:
            return
            
        if self.hasMouseTracking():
            self.setMouseTracking(False)
        else:
            self.past_x_pos = event.x()
            self.past_y_pos = event.y()
            self.setMouseTracking(True)

    def draw(self):
        # No Draw
        if self.draw_flag == 0:
            self.draw_type = 'No Draw'
        # Polygon
        elif self.draw_flag == 1:
            pass
        # Gesture Polygon
        elif self.draw_flag == 2:
            pass
        # Rectangle
        elif self.draw_flag == 3:
            pass
        # Circle
        elif self.draw_flag == 4:
            pass
        # Line
        elif self.draw_flag == 5:
            global img

            h, w, c = img.shape #height, width, channel
            qImg = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
            draw_img = QPixmap.fromImage(qImg)

            painter = QPainter(draw_img)
            painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))
            painter.drawLine(self.past_x_pos, self.past_y_pos, self.cur_x_pos, self.cur_y_pos)
            painter.end()
            self.label_Canvas.setPixmap(QPixmap(draw_img))    
        # Dot
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

        h, w, c = img.shape #height, width, channel
        qImg = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
        self.qPixmap = QPixmap.fromImage(qImg)
        self.label_Canvas.setPixmap(self.qPixmap)
        self.flag = True
        self.menuRefresh(self.flag)



if __name__=='__main__':
    app = QApplication(sys.argv)
    handannot = HandAnnot()
    handannot.show()
    app.exec_()
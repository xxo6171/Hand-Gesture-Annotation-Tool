from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from ViewModel.Canvas import Canvas

import Model

mainUI_dir = 'Resource/UI/Main GUI.ui'
main_form_class = uic.loadUiType(mainUI_dir)[0]

class HandAnnot(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = Model.Model()

        self.draw_actions = [
                                self.action_Polygon,
                                self.action_Right_Gesture,
                                self.action_Left_Gesture,
                                self.action_Rectangle,
                                self.action_Circle,
                                self.action_Line,
                                self.action_Dot,
                                self.action_Retouch,
                                self.action_Auto_Annotation         ]
        self.list_widgets = [
                                self.listWidget_LabelList,
                                self.listWidget_ObjectList          ]

        self.canvas_widgets = [
                                self.action_Open,
                                self.menu_Edit,
                                self.menu_Zoom,
                                self.action_Save,
                                
                                self.draw_actions,
                                self.statusBar,
                                self.action_Zoom_In,
                                self.action_Zoom_Out,

                                self.list_widgets
                            ]

        self.canvas_viewmodel = Canvas(self.canvas_widgets, self.model)

        self.scrollArea_Canvas.setWidget(self.canvas_viewmodel)

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = HandAnnot()
    view.show()
    app.exec_()
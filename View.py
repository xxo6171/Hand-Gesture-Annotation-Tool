from PyQt5 import uic
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
import sys

from Model import *
from ViewModel import *

mainUI_dir = 'Resource/UI/Main GUI.ui'
main_form_class = uic.loadUiType(mainUI_dir)[0]

class HandAnnot(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Binding
        self.Model = Model()
        self.ViewModel = ViewModel(self.getComponents(), self.Model)
    

    def getComponents(self):
        components = []
        
        actions = []
        file_actions = [    self.action_Open,
                            self.action_Save,
                            self.action_Exit        ]

        edit_actions = [    self.action_Polygon,
                            self.action_Right_Gesture,
                            self.action_Left_Gesture,
                            self.action_Rectangle,
                            self.action_Circle,
                            self.action_Line,
                            self.action_Dot,

                            self.action_Retouch,
                            self.action_Auto_Annotation     ]

        zoom_actions = [    self.action_Zoom_In,
                            self.action_Zoom_Out    ]

        actions.append(file_actions)
        actions.append(edit_actions)
        actions.append(zoom_actions)

        widgets = [     self.scrollArea_Canvas,
                        self.listWidget_LabelList,
                        self.listWidget_ObjectList  ]
        
        components.append(actions)
        components.append(widgets)

        return components


if __name__=='__main__':
    app = QApplication(sys.argv)
    view = HandAnnot()
    view.show()
    app.exec_()
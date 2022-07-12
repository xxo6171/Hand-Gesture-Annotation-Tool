from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

from ViewModel.Canvas import Canvas
from ViewModel.LabelList import LabelList
from ViewModel.ObjectList import ObjectList
import Model

mainUI_dir = 'Resource/UI/Main GUI.ui'
main_form_class = uic.loadUiType(mainUI_dir)[0]

class HandAnnot(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = Model.Model()

        canvas_widget = [
                            self.action_Open,
                            self.label_Canvas,
                            self.scrollArea_Canvas,
                            self.menu_Edit,
                            self.menu_Zoom,
                            self.action_Save,
                            
                            self.action_Line,
                            self.statusBar
                        ]

        self.canvas_viewmodel = Canvas(canvas_widget, self.model)

    def mouseMoveEvent(self, event):
        x_pos = event.x() - 20
        y_pos = event.y() - 50
        self.model.setCurPos([x_pos, y_pos])
        text = '{x_pos}, {y_pos}'.format(x_pos=x_pos, y_pos=y_pos)
        self.statusBar.showMessage(text)
    
    def mouseReleaseEvent(self, event):
        if self.hasMouseTracking():
            self.setMouseTracking(False)
        else:
            past_x_pos = event.x() - 20
            past_y_pos = event.y() - 50
            self.model.setPrePos([past_x_pos, past_y_pos])
            self.setMouseTracking(True)

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = HandAnnot()
    view.show()
    app.exec_()
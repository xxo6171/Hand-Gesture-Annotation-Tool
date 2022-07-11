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
        text = '{x_pos}, {y_pos}'.format(x_pos=event.x(), y_pos=event.y())
        self.statusBar.showMessage(text)
    
    def mouseReleaseEvent(self, event):
        if self.model.getDrawFlag is None:
            return
            
        if self.hasMouseTracking():
            self.setMouseTracking(False)
        else:
            self.past_x_pos = event.x()
            self.past_y_pos = event.y()
            self.setMouseTracking(True)

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = HandAnnot()
    view.show()
    app.exec_()
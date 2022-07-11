from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

from Utils import AutoAnnotation
from Utils import ConvertAnnotation
from Utils import ImageProc
from ViewModel import Canvas
from ViewModel import LabelList
from ViewModel import ObjectList
import Model

mainUI_dir = 'Resource/UI/Main GUI.ui'
main_form_class = uic.loadUiType(mainUI_dir)[0]

class HandAnnot(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
        list_widget = [
                        self.listWidget,
                        self.add,
                        self.delete_2,
                        self.lineEdit
                      ]
        self.model = Model.Model()
        self.list_viewmodel = ViewModel.List(list_widget, self.model)
        '''

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = HandAnnot()
    view.show()
    app.exec_()
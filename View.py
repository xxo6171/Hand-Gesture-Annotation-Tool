from PyQt5 import uic
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
import sys

import Model
import ViewModel

mainUI_dir = 'Resource/UI/Main GUI.ui'
main_form_class = uic.loadUiType(mainUI_dir)[0]

class HandAnnot(QMainWindow, main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Binding
        self.Model = Model.Model()
        self.ViewModel = ViewModel.ViewModel(self.getComponents(), self.Model)
    
    def getComponents(self):
        components = []
        
        actions = []
        widgets = []
        
        components.append(actions)
        components.append(widgets)

        return components

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = HandAnnot()
    view.show()
    app.exec_()
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Canvas(QMainWindow):
    def __init__(self, view, model):
        #Initialize
        self.action_Open = view[0]
        self.label_Canvas = view[1]
        self.scrollArea_Canvas = view[2]
        '''
        self.list_listWidget = view[0]
        self.add_btn = view[1]
        self.delete_btn = view[2]
        self.string_lineEdit = view[3]
        '''
        self.model = model

        #Triggered connect
        self.action_Open.triggered.connect(self.OpenImage)

        #Widget setting
        self.label_Canvas.setAlignment(Qt.AlignCenter)
        self.scrollArea_Canvas.setWidget(self.label_Canvas)

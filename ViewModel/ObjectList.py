from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ObjectList:
    def __init__(self, view, model):
        '''
        self.list_listWidget = view[0]
        self.add_btn = view[1]
        self.delete_btn = view[2]
        self.string_lineEdit = view[3]
        '''
        self.model = model

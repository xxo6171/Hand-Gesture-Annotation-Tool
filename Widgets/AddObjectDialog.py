from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
Ui_AddObjectDialog, QtBaseClass = uic.loadUiType(BASE_DIR[:-8] + r'/Resource/UI/Add Object Dialog.ui')

class AddObjectDialog(QDialog, Ui_AddObjectDialog):
    def __init__(self, view, model):
        super().__init__()
        self.setupUi(self)

        self.view_LabelList = view[0]
        self.view_ObjectList = view[1]
        self.model = model
        self.initListWidget()

        self.listWidget_LabelList.itemClicked.connect(self.clickItem)
        self.listWidget_LabelList.itemDoubleClicked.connect(self.doubleClickItem)

        self.pushButton_OK.clicked.connect(self.setLabel)
        self.pushButton_Cancel.clicked.connect(self.closeDialog)

    def initListWidget(self):
        self.label_list = self.model.getLabelList()

        for label in self.label_list:
            add_label = QListWidgetItem(label)
            self.listWidget_LabelList.addItem(add_label)

    def clickItem(self):
        label = self.listWidget_LabelList.currentItem().text()
        self.lineEdit_NewLabel.setText(label)

    def doubleClickItem(self):
        self.setLabel()

    def setLabel(self):
        label_name = self.lineEdit_NewLabel.text()
        if label_name == '':
            self.closeDialog()
            return
        if label_name not in self.label_list:
            self.model.setLabel(label_name)
        self.model.setCurLabel(label_name)
        self.closeDialog()

    def setObject(self):
        self.view_ObjectList.clear()
        annot_info = self.model.getAnnotInfo(True)
        shapes = annot_info['shapes']
        if not shapes:
            return

        for idx in range(len(shapes)):
            obj_type = shapes[idx]['shape_type']
            obj_label = shapes[idx]['label']
            add_object = QListWidgetItem(obj_type + '_' + obj_label)
            self.view_ObjectList.addItem(add_object)

    def closeDialog(self):
        self.view_LabelList.clear()
        labels = self.model.getLabelList()

        for label in labels:
            add_label = QListWidgetItem(label)
            self.view_LabelList.addItem(add_label)

        if self.model.getCurLabel() != '':
            self.model.pushAnnot(self.model.getAnnotInfo())
            self.model.setCurShapeToDict()
        self.model.setCurLabel('')
        self.setObject()
        self.close()
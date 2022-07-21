from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

add_label_UI_dir = 'Resource/UI/Add Lable Dialog.ui'
add_label_form_class = uic.loadUiType(add_label_UI_dir)[0]

class AddLabelDialog(QDialog, add_label_form_class):
    def __init__(self, view, model):
        super().__init__()
        self.setupUi(self)

        self.view = view
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
        if label_name == '' :
            self.closeDialog()
            return
        if label_name not in self.label_list:
            self.model.setLabel(label_name)
        self.model.setCurLabel(label_name)
        self.closeDialog()

    def closeDialog(self):
        self.view.clear()
        labels = self.model.getLabelList()

        for label in labels:
            add_label = QListWidgetItem(label)
            self.view.addItem(add_label)

        if self.model.getCurLabel() != '':
                self.model.setCurShapeToDict()
        self.model.setCurLabel('')
        
        self.close()
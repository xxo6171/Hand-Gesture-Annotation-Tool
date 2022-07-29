from PyQt5.QtWidgets import *

from Utils.ConvertAnnotation import *

class Delete(QWidget):
    def __init__(self, view, model, display):
        super().__init__()

        self.Model = model

        self.label_list = view[0]
        self.object_list = view[1]

        # Connect Object List
        self.object_list.itemClicked.connect(self.objectClicked)
        self.object_list.itemDoubleClicked.connect(self.objectDoubleClicked)

    # ----- Object List Click Event -----
    def objectClicked(self):
        self.Display.setDisplayAnnotInfo()

        qimg, w, h, c = self.Model.getImgScaled()
        origin_annot = self.Model.getAnnotInfo()
        denorm_annot = denormalization(origin_annot)

        cur_shapes = denorm_annot['shapes']

    def objectDoubleClicked(self):
        print('Double Click!')


    # ----- Delete -----
    def deleteObject(self):
        pass
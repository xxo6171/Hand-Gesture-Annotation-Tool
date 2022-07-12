class Model:
    def __init__(self):
        self.imgData = None

        self.img_origin = None
        self.img_scaled = None
        self.scale_ratio = None

        self.label_list = []
        self.object_list = []
        self.annot_info = {}

        self.draw_flag = 'No Draw'
        self.pre_mouse_pos = []
        self.cur_mouse_pos = []
    
    def getImgData(self): return self.imgData
    def setImgData(self, img): self.imgData = img

    def getImgScaled(self):
        return self.img_scaled
    def setImgScaled(self, img):
        self.img_scaled = img

    def getScaleRatio(self):
        return self.scale_ratio
    def setScaleRatio(self, ratio):
        self.scale_ratio = ratio

    def getLabelList(self):
        return self.label_list
    def setLabelList(self, list):
        self.label_list = list

    def getObjectList(self):
        return self.object_list
    def setObjectList(self, list):
        self.object_list = list

    def getAnnotInfo(self):
        return self.annot_info
    def setAnnotInfo(self, dict):
        self.annot_info = dict

    def getDrawFlag(self):
        return self.draw_flag
    def setDrawFlag(self, flag):
        self.draw_flag = flag

    def getPrePos(self):
        return self.pre_mouse_pos
    def setPrePos(self, list):
        self.pre_mouse_pos = list

    def getCurPos(self):
        return self.cur_mouse_pos
    def setCurPos(self, list):
        self.cur_mouse_pos = list
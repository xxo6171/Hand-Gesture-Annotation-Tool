class Model:
    def __init__(self):
        self.imgData = None

        self.img_origin = None
        self.img_origin_width = None
        self.img_origin_height = None

        self.img_scaled = None
        self.img_scaled_width = None
        self.img_scaled_height = None

        self.scale_ratio = 1

        self.label_list = []
        self.object_list = []
        self.annot_info = {}

        self.focus_flag = None
        self.menu_flag = None
        self.ctrl_flag = None
        self.draw_flag = 'No Draw'
        
        self.pre_mouse_pos = []
        self.cur_mouse_pos = []
    
    def getImgData(self):
        if self.imgData is None :
            return None
        return self.imgData.copy(), self.img_origin_width, self.img_origin_height
    def setImgData(self, img, width, height):
        self.imgData = img.copy()
        self.img_origin_width = width
        self.img_origin_height = height

    def getImgScaled(self):
        return self.img_scaled.copy(), self.img_scaled_width, self.img_scaled_height
    def setImgScaled(self, img, width, height):
        self.img_scaled = img.copy()
        self.img_scaled_width = width
        self.img_scaled_height = height


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

    def getFocusFlag(self):
        return self.focus_flag
    def setFocusFlag(self, flag):
        self.focus_flag = flag
        
    def getMenuFlag(self):
        return self.menu_flag
    def setMenuFlag(self, flag):
        self.menu_flag = flag

    def getCtrlFlag(self):
        return self.ctrl_flag
    def setCtrlFlag(self, flag):
        self.ctrl_flag = flag

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
import copy
from re import sub

class Model:
    def __init__(self):
        self.imgData = None

        self.img_origin = None
        self.img_origin_width = None
        self.img_origin_height = None
        self.img_origin_channel = None

        self.img_scaled = None
        self.img_scaled_width = None
        self.img_scaled_height = None
        self.img_scaled_channel = None

        self.scale_ratio = 1

        self.label_list = []
        self.object_list = []
        self.annot_info = {}
        self.initAnnotInfo()

        self.cur_points = []
        self.cur_label = ''

        self.focus_flag = None
        self.menu_flag = None
        self.ctrl_flag = None
        self.draw_flag = 'No Draw'
        self.tracking_flag = False
        self.keep_tracking_flag = False
        
        self.pre_mouse_pos = []
        self.cur_mouse_pos = []
    
    def getImgData(self):
        if self.imgData is None :
            return None
        return self.imgData.copy(), self.img_origin_width, self.img_origin_height, self.img_origin_channel
    def setImgData(self, img, width, height, channel):
        self.imgData = img.copy()
        self.img_origin_width = width
        self.img_origin_height = height
        self.img_origin_channel = channel

    def getImgScaled(self):
        return self.img_scaled.copy(), self.img_scaled_width, self.img_scaled_height, self.img_scaled_channel
    def setImgScaled(self, img, width, height, channel):
        self.img_scaled = img.copy()
        self.img_scaled_width = width
        self.img_scaled_height = height
        self.img_scaled_channel = channel


    def getScaleRatio(self):
        return self.scale_ratio
    def setScaleRatio(self, ratio):
        self.scale_ratio = round(ratio,2)

    def getLabelList(self):
        return self.label_list
    def setLabelList(self, list):
        self.label_list = list

    def getObjectList(self):
        return self.object_list
    def setObjectList(self, list):
        self.object_list = list

    def initAnnotInfo(self):
        self.annot_info['shapes'] = []
        self.annot_info['image_path'] = ''
        self.annot_info['image_width'] = 0
        self.annot_info['image_height'] = 0
    def setAnnotInfo(self, filepath, width, height):
        self.annot_info['image_path'] = filepath
        self.annot_info['image_width'] = width
        self.annot_info['image_height'] = height
    def getAnnotInfo(self):
        return copy.deepcopy(self.annot_info)
    def setCurShapeToDict(self, rad = -1):
        new_shape = {}
        new_shape['label'] = self.cur_label
        new_shape['points'] = self.cur_points
        if rad > 0:
            new_shape['radian'] = rad
        new_shape['shape_type'] = self.draw_flag
        self.annot_info['shapes'].append(new_shape)
    def setCurPoints(self, point):
        pos = point.copy()
        self.cur_points.append(pos)
    def setCurLabel(self, label):
        self.cur_label = label

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

    def isTracking(self):
        return self.tracking_flag
    def setTracking(self, flag):
        self.tracking_flag = flag
 
    def isKeepTracking(self):
        return self.keep_tracking_flag
    def setKeepTracking(self, flag):
        self.keep_tracking_flag = flag
        

    def getPrePos(self):
        return self.pre_mouse_pos.copy()
    def setPrePos(self, list):
        self.pre_mouse_pos = list.copy()

    def getCurPos(self):
        return self.cur_mouse_pos.copy()
    def setCurPos(self, list):
        self.cur_mouse_pos = list.copy()
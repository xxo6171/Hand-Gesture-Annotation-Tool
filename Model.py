import copy

class Model:
    def __init__(self):
        self.img_origin = None
        self.img_origin_width = None
        self.img_origin_height = None
        self.img_origin_channel = None

        self.img_scaled = None
        self.img_scaled_width = None
        self.img_scaled_height = None
        self.img_scaled_channel = None

        self.scale_ratio = 1
        self.top = 0
        self.annot = []
        self.label_list = []
        self.annot_info = {}
        self.initAnnotInfo()

        self.cur_points = [-1]
        self.cur_label = ''
        self.cur_shape_type = ''
        self.zoom_type = ''

        self.menu_flag = False
        self.draw_flag = False
        self.retouch_flag = False
        self.tracking_flag = False
        self.keep_tracking_flag = False
        self.undo_flag = False
        
        self.pre_mouse_pos = [0, 0]
        self.cur_mouse_pos = [0, 0]
        self.click_point_range = 10
        self.move_point = None

        self.selected_object_idx = None
    
    def getImgData(self):
        if self.img_origin is None :
            return None
        return self.img_origin.copy(), self.img_origin_width, self.img_origin_height, self.img_origin_channel
    def setImgData(self, img, width, height, channel):
        if img is None : self.img_origin = None
        else : self.img_origin = img.copy()
        self.img_origin_width = width
        self.img_origin_height = height
        self.img_origin_channel = channel

    def getImgScaled(self, no_img=False):
        if no_img:
            return self.img_scaled_width, self.img_scaled_height, self.img_scaled_channel
        else:
            return self.img_scaled.copy(), self.img_scaled_width, self.img_scaled_height, self.img_scaled_channel
    def setImgScaled(self, img, width, height, channel):
        if img is None : self.img_scaled = None
        else : self.img_scaled = img.copy()
        self.img_scaled_width = width
        self.img_scaled_height = height
        self.img_scaled_channel = channel


    def getScaleRatio(self):
        return self.scale_ratio
    def setScaleRatio(self, ratio):
        self.scale_ratio = round(ratio,2)

    def initLabelList(self):
        self.label_list.clear()
    def getLabelList(self):
        return self.label_list.copy()
    def setLabel(self, label):
        self.label_list.append(label)

    def initAnnotInfo(self):
        self.annot_info['shapes'] = []
        self.annot_info['image_path'] = ''
        self.annot_info['image_width'] = 0
        self.annot_info['image_height'] = 0
    def getAnnotInfo(self, no_deep=False):
        if no_deep:
            return self.annot_info
        return copy.deepcopy(self.annot_info)
    def setAnnotDict(self, dict):
        self.annot_info = copy.deepcopy(dict)
    def setAnnotInfo(self, filepath, width, height):
        self.annot_info['image_path'] = filepath
        self.annot_info['image_width'] = width
        self.annot_info['image_height'] = height
    def setCurShapeToDict(self):
        new_shape = {}
        new_shape['label'] = self.cur_label
        new_shape['points'] = self.cur_points
        new_shape['shape_type'] = self.cur_shape_type
        self.annot_info['shapes'].append(new_shape)
    def resetCurPoints(self):
        self.cur_points = []
    def deleteShape(self, idx):
        del self.annot_info['shapes'][idx]
    def addCurPoint(self, point, raw=False):
        pos = point.copy()
        if not raw:
            pos[0] /= self.img_scaled_width
            pos[1] /= self.img_scaled_height
        self.cur_points.append(pos)
    def getCurPoints(self):
        return copy.deepcopy(self.cur_points)
    def setCurPoints(self, points):
        self.cur_points = points.copy()
    def getCurLabel(self):
        return self.cur_label
    def setCurLabel(self, label):
        self.cur_label = label
    def getCurShapeType(self):
        return self.cur_shape_type
    def setCurShapeType(self, shape_type):
        self.cur_shape_type = shape_type

    def initAnnotStack(self):
        self.top = len(self.annot)
        self.annot.clear()
    def popAnnot(self):
        if len(self.annot) == 1:
            return copy.deepcopy(self.annot[0])
        return copy.deepcopy(self.annot.pop())
    def pushAnnot(self, dict):
        self.annot.append(copy.deepcopy(dict))

    def getZoomType(self):
        return self.zoom_type
    def setZoomType(self, type):
        self.zoom_type = type

    def getUndoFlag(self):
        return self.undo_flag
    def setUndoFlag(self, flag):
        self.undo_flag = flag
        
    def getMenuFlag(self):
        return self.menu_flag
    def setMenuFlag(self, flag):
        self.menu_flag = flag

    def getDrawFlag(self):
        return self.draw_flag
    def setDrawFlag(self, flag):
        self.draw_flag = flag

    def getRetouchFlag(self):
        return self.retouch_flag
    def setRetouchFlag(self, flag):
        self.retouch_flag = flag

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

    def getClickPointRange(self):
        return self.click_point_range
    def setMovePoint(self, point):
        self.move_point = point
    def getMovePoint(self):
        return self.move_point

    def setSelectedObjectIndex(self, idx):
        self.selected_object_idx = idx
    def getSelectedObjectIndex(self):
        return self.selected_object_idx

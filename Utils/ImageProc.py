import cv2
import numpy as np

class ImageProc:
    def __init__(self):
        pass

    def loadImgData(self, filepath):
        img_data = np.fromfile(filepath, np.uint8)
        img_data = cv2.imdecode(img_data, cv2.IMREAD_COLOR)
        img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB)
        return img_data
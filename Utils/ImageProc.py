import cv2
import numpy as np

class ImageProc:
    def __init__(self):
        pass

    def loadImgData(self, filepath):
        img = np.fromfile(filepath, np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
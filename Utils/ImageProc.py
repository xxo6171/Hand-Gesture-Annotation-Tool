import cv2
import numpy as np

def loadImgData(filepath):
    img_data = cv2.cvtColor(cv2.imdecode(np.fromfile(filepath, np.uint8), cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
    h,w,c = img_data.shape
    return img_data, w, h, c

def resizeImage(img, scaleRatio, interpolation):
    if interpolation : itp = cv2.INTER_LINEAR
    else : itp = cv2.INTER_AREA
    img_data = cv2.resize(img, None, fx=scaleRatio, fy=scaleRatio,
                     interpolation=itp)
    h, w, c = img_data.shape
    return img_data, w, h, c
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Utils.ConvertAnnotation import *

import math

class Delete(QWidget):
    def __init__(self, model, display):
        super().__init__()

        self.Model = model

        self.Display = display


    # ----- Object List Click Event -----
    def displaySelectedObject(self):
        idx = self.Model.getSelectedObjectIndex()
        self.Display.setDisplayAnnotInfo()

        qimg, w, h, c = self.Model.getImgScaled()
        origin_annot = self.Model.getAnnotInfo()
        denorm_annot = denormalization(origin_annot, w, h)

        clicked_shape = denorm_annot['shapes'][idx]
        shape_type = clicked_shape['shape_type']
        points = clicked_shape['points']

        painter = QPainter(qimg)
        painter.setPen(QPen(Qt.darkBlue, 10, Qt.SolidLine))

        if shape_type == 'Polygon':
            pre = points[0]

            for point in points:
                cur = point
                painter.drawLine(pre[0], pre[1], cur[0], cur[1])
                pre = point
            painter.drawLine(points[0][0], points[0][1], pre[0], pre[1])

        elif shape_type == 'Gesture Polygon':
            nb_points = 21
            for idx in range(1, nb_points):
                if idx%4 == 1:
                    src_pos = points[idx]
                    continue
                dst_pos = points[idx]
                painter.drawLine(src_pos[0], src_pos[1], dst_pos[0], dst_pos[1])
                src_pos = dst_pos

            list_hand = [(0, 1), (0, 5), (0, 17), (5, 9), (9, 13), (13, 17)]

            for idx in list_hand:
                src = idx[0]
                dst = idx[1]
                painter.drawLine(points[src][0], points[src][1], points[dst][0], points[dst][1])

        elif shape_type == 'Rectangle':
            width = (points[1][0] - points[0][0])
            height = (points[1][1] - points[0][1])

            painter.drawRect(points[0][0], points[0][1], width, height)

        elif shape_type == 'Circle':
            rad = math.sqrt(math.pow(points[0][0]-points[1][0], 2) + math.pow(points[0][1]-points[1][1], 2))

            painter.drawEllipse(points[0][0]-rad, points[0][1]-rad, rad*2, rad*2)

        elif shape_type == 'Line':
            painter.drawLine(points[0][0], points[0][1], points[1][0], points[1][1])

        painter.end()
        self.Model.setImgScaled(qimg, w, h, c)

    def deleteObject(self):
        object_idx = self.Model.getSelectedObjectIndex()
        self.Model.deleteShape(object_idx)

        self.Display.setDisplayAnnotInfo()
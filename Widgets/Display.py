from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Utils.ConvertAnnotation import *

import math, copy

class Display(QWidget):
    def __init__(self, canvas, scroll_area, model):
        super().__init__()
        self.Model = model

        self.canvas = canvas
        self.scroll_area = scroll_area

    def img2QPixmap(self, img, w, h, c):
        qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        qPixmap = QPixmap.fromImage(qImg)

        return qPixmap

    def setDisplayAnnotInfo(self):
        img, w, h, c = self.Model.getImgData()
        ratio = self.Model.getScaleRatio()
        annot_info = self.Model.getAnnotInfo()
        point_scale = self.Model.getClickPointRange()

        qimg = self.img2QPixmap(img, w, h, c)

        annot_info = denormalization(annot_info, w, h)
        painter = QPainter(qimg)

        painter.setPen(QPen(Qt.red, point_scale, Qt.SolidLine))
        for shape in annot_info['shapes']:
            shape_type = shape['shape_type']
            points = copy.deepcopy(shape['points'])
                        
            if shape_type == 'Polygon':
                pre = points[0]
                painter.setPen(QPen(Qt.magenta, 3, Qt.SolidLine))

                for point in points:
                    cur = point
                    painter.drawLine(pre[0], pre[1], cur[0], cur[1])

                    painter.setPen(QPen(Qt.red, point_scale, Qt.SolidLine))
                    painter.drawPoint(cur[0], cur[1])
                    painter.drawPoint(pre[0], pre[1])

                    painter.setPen(QPen(Qt.magenta, 3, Qt.SolidLine))
                    pre = point

                painter.drawLine(points[0][0], points[0][1], pre[0], pre[1])

                painter.setPen(QPen(Qt.red, point_scale, Qt.SolidLine))
                painter.drawPoint(points[0][0], points[0][1])
                painter.drawPoint(pre[0], pre[1])


            elif shape_type == 'Gesture Polygon':
                painter.setPen(QPen(Qt.cyan, 3, Qt.SolidLine))
                nb_points = 21
                for idx in range(1, nb_points):
                    if idx%4 == 1:
                        src_pos = points[idx]
                        continue
                    dst_pos = points[idx]
                    painter.drawLine(src_pos[0], src_pos[1], dst_pos[0], dst_pos[1])

                    painter.setPen(QPen(Qt.red, point_scale, Qt.SolidLine))
                    painter.drawPoint(src_pos[0], src_pos[1])
                    painter.drawPoint(dst_pos[0], dst_pos[1])

                    painter.setPen(QPen(Qt.cyan, 3, Qt.SolidLine))
                    src_pos = dst_pos

                list_hand = [(0, 1), (0, 5), (0, 17), (5, 9), (9, 13), (13, 17)]

                for idx in list_hand:
                    src = idx[0]
                    dst = idx[1]
                    painter.setPen(QPen(Qt.cyan, 3, Qt.SolidLine))
                    painter.drawLine(points[src][0], points[src][1], points[dst][0], points[dst][1])

                    painter.setPen(QPen(Qt.red, point_scale, Qt.SolidLine))
                    painter.drawPoint(points[src][0], points[src][1])
                    painter.drawPoint(points[dst][0], points[dst][1])
     
            elif shape_type == 'Rectangle':
                width = (points[1][0] - points[0][0])
                height = (points[1][1] - points[0][1])

                color = QPen(Qt.blue, 3, Qt.SolidLine)
                painter.setPen(color)
                painter.drawRect(points[0][0], points[0][1], width, height)
                painter.setPen(QPen(Qt.red, point_scale, Qt.SolidLine))
                painter.drawPoint(points[0][0], points[0][1])
                painter.drawPoint(points[1][0], points[1][1])

            elif shape_type == 'Circle':
                rad = math.sqrt(math.pow(points[0][0]-points[1][0], 2) + math.pow(points[0][1]-points[1][1], 2))

                color = QPen(Qt.red, 3, Qt.SolidLine)
                painter.setPen(color)
                painter.drawEllipse(points[0][0]-rad, points[0][1]-rad, rad*2, rad*2)
                painter.setPen(QPen(Qt.red, point_scale, Qt.SolidLine))
                painter.drawPoint(points[0][0], points[0][1])
                painter.drawPoint(points[1][0], points[1][1])


            elif shape_type == 'Line':
                color = QPen(Qt.yellow, 3, Qt.SolidLine)
                painter.setPen(color)
                painter.drawLine(points[0][0], points[0][1], points[1][0], points[1][1])
                painter.setPen(QPen(Qt.red, point_scale, Qt.SolidLine))
                painter.drawPoint(points[0][0], points[0][1])
                painter.drawPoint(points[1][0], points[1][1])


            elif shape_type == 'Dot':
                painter.drawPoint(points[0][0], points[0][1])

        painter.end()

        self.Model.setImgScaled(qimg, w, h, c)

    def displayImage(self, img, w, h):
        self.canvas.clear()

        self.canvas.setGeometry(0, 0, w, h)
        self.canvas.setPixmap(img)
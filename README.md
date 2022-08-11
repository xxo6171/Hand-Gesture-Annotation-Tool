# Introduce

#### 개요

* Hand Gesture Annotation Tool with P\&C Solution Internship
* 본 프로젝트는 연세대학교 미래캠퍼스 SW 중심대학 사업단에서 주관한 하계 단기 인턴십에 참여하며 진행된 프로젝트입니다

## Description

* Hand Annot는 AR Glass에 AI 도입을 위한 모델 개발이 이뤄짐에 따라, 학습 데이터 Annotation Tool 개발이 진행되었습니다.
* Image Annotation Tool인 Labelme를 참고해 Python으로 작성되었으며, GUI를 위해 QT가 사용되었습니다.

## Features

*   [x] Create _Polygon, Hand Gesture, Rectangle, Circle, Line, Dot_ for Image Annotation

    ![image-20220801140559289](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Auto\_After.png) ![image-20220801141136646](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Create\_Polygon.png) ![image-20220801141841416](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Create\_Gesture.png) ![image-20220801141221183](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Create\_Rectangle.png)
*   [x] Retouch Things by Points Move

    ![image-20220801142039426](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Retouch\_Before.png) ![image-20220801142113560](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Retouch\_After.png)
*   [x] Auto _Hand Gesture Annotation_ by Mediapipe Hands

    ![image-20220801141605636](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Auto\_Before.png) ![image-20220801141620506](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Auto\_After.png)
*   [x] Zoom In & Out

    ![image-20220801142245269](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Zoom\_Before.png) ![image-20220801142307207](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Zoom\_In.png) ![image-20220801142331061](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Zoom\_Out.png)
*   [x] Select( Click ) & Delete( Double Click ) Object

    ![image-20220801142631780](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Object\_Select.png) ![image-20220801142643059](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/blob/master/Resource/readme/Object\_Delete.png)

## Requirements

* Python 3.7x
* PyQt5
* OpenCV
* Mediapipe Hands

## Usage

*   Excute Program by HandAnnot.py or Released HandAnnot.exe

    [HandAnnot\_Released](https://github.com/KimJinSeong-Git/Hand-Gesture-Annotation-Tool/releases/tag/HandAnnot)

1. Image File Open
   * If there is a file with the same name as the \*.json extension, load the file.
   * else, create empty info
2. Add Annotation Info( Gesture, Polygon, Rectangle, etc.)
   * set draw type
   * click canvas & set label
3. Retouch Things
   * set retouch mode
   * click the point & drag & drop
4. Save Annotation Info
   *   \*.Json File Structure

       ```json
       {
       	"shapes": [
       		{
       			"label": "{Label Name}",
       			"points": [
       				[
       					x_1,
       					y_1
       				],
       				...
       				,
       				[
       					x_n,
       					y_n
       				]
       			],
       			"shape_type": "{Shape Type}"
       		},
               ...
       	],
       	"image_path": "{File Path}",
       	"image_width": {Width},
       	"image_height": {Height}
       }
       ```

## Gitbook

> https://kim-jin-seong.gitbook.io/hand-annot/

## Contat Us

* acmiheee@gmail.com
* kyung971112@gmail.com

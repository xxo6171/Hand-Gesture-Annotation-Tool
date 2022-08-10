---
description: >-
  본 프로젝트는 연세대학교 미래캠퍼스 SW 중심대학 사업단에서 주관한 하계 단기 인턴십에 참여하며 진행된 프로젝트로, AR Glass에 AI
  도입을 위한 모델 개발이 이뤄짐에 따라, 학습 데이터 Annotation Tool 개발이 진행되었습니다.
---

# Introduce

### Features

* [x] Create _Polygon, Hand Gesture, Rectangle, Circle, Line, Dot_ for Image Annotation
* [x] Retouch Things by Points Move
* [x] Auto _Hand Gesture Annotation_ by Mediapipe Hands
* [x] Zoom In & Out
* [x] Select( Click ) & Delete( Double Click ) Object

### Requirements

* Python 3.7x
* PyQt5
* OpenCV
* Mediapipe Hands

### Usage

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

### Contact Us

* [acmiheee@gmail.com](mailto:acmiheee@gmail.com)
* [kyung971112@gmail.com](mailto:kyung971112@gmail.com)

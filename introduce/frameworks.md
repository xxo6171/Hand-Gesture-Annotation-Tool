---
description: >-
  차후 AI 모델 도입, 유용한 API 사용 및 초기에 잦은 디자인 변화에 빠르게 대응하기 위해 Python 3.7 버전을 사용하게 되었고
  이에 따라 사용한 Python Framework의 종류와 사용 기능에 대한 명세 페이지입니다.
---

# Frameworks

### PyQt5

> 공식 문서: [https://doc.qt.io/qtforpython-5/api.html](https://doc.qt.io/qtforpython-5/api.html)
>
> $ pip install PyQt5

* 다양한 Widgets, Actions 등 다양한 Components와 QT Designer를 통한 워지윅스 기능을 이용해 새로운 기능 추가와 UI 변경의 용이성을 확보해 빠르게 프로토타입 개발을 하기 위한 기반으로 사용된 GUI 구현 Framework&#x20;
* 기본적으로 Menu Action을 통해 기능이 연결되었으며, 화면 표시를 위한 Scroll Area, List View를 위한 List Widget이 사용되었습니다.
* 이외 Key Event( Keyboard ), Wheel Event, Mouse Event를 사용해 Short Cut, Draw, Zoom 기능이 구현되었습니다.&#x20;

### OpenCV

> 공식 문서: [https://docs.opencv.org/4.x/d6/d00/tutorial\_py\_root.html](https://docs.opencv.org/4.x/d6/d00/tutorial\_py\_root.html)
>
> $ pip install opencv-python

* Open Source Computer Vision의 약어로 영상처리에 관련한 문제를 해결하기 위한 프로토타입을 빠르게 구현 가능한 오픈 소스 라이브러리입니다.&#x20;
* C++, Python, Java 등 다양한 프로그래밍 언어로 지원하고 있으며, Windows, Linux, Mac OS, Android, IOS 등의 OS 플랫폼을 지원합니다.
* OpenCV 함수를 이용해 이미지가 처리된 이미지 데이터, 이미지 가로/세로 크기, 채널을 반환하는 역할을 합니다.
* 이미지 파일을 불러오기 위해 원본 이미지 데이터, 크기가 조절( 확대/축소 )된 이미지 데이터를 반환하여 반환 받은 이미지 데이터와 PyQt5의 Widget이 연동되어 처리됩니다.&#x20;

### MediaPipe Hands

> 공식 문서: [https://google.github.io/mediapipe/solutions/hands.html](https://google.github.io/mediapipe/solutions/hands.html)
>
> $ pip install mediapipe&#x20;

* Auto Annotation 기능에 대응하기 위한 AI 모델로, API 모듈 중 Hand Gesture Tracking 기술이 가장 우수한 모듈로 선정했습니다.&#x20;
* 머신러닝을 이용하여 손의 21개 3D Landmark를 추척하며 본 프로그램에서는 3D 데이터를 사용하지 않고 2D 좌표만을 이용해서 프로그램이 구현되었습니다.&#x20;
* 손 사진을 입력해 처리를 요청하면 머신러닝 모델에서 21개의 좌표를 예측해 도출해 내며 각 Landmark 들은 고유의 Index를 가집니다.( 그림 참조 )&#x20;

![](<../.gitbook/assets/image (1).png>)

* 각 좌표는 정규화된 값으로 추출되며, 추적하지 못한 Point는 음수 값으로 출력되어 나오므로 이를 이용해 제대로 추출된 값과 그렇지 못한 값을 구분해낸 뒤 예외처리가 진행되었습니다.&#x20;




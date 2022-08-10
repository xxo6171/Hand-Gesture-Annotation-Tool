---
description: MVVM 디자인 패턴을 적용한 Class Diagram으로 대략적인 프로그램 구조를 살펴볼 수 있습니다.
---

# Class Diagram

![Class Diagram](<../.gitbook/assets/class diagram\_0803.png>)

### View

* PyQt5 Designer에서 설계된 \*.ui 파일이 해당
* 단지 Program Main Window의 요소만을 포함한다.
* Actions
  * File
    * Open
    * Save
    * Exit
  * Edit
    * Create
      * Polygon
      * Right Gesture
      * Left Gesture
      * Rectangle
      * Circle
      * Line
      * Dot
    * Retouch
    * Auto Annotation
  * Zoom
    * In
    * Out
* Widgets
  * Scroll_Area_\_Canvas
  * ListWidget\_LabelList
  * ListWidget\_OjbectList

### Model

* 프로그램 구동에 필요한 모든 데이터를 담당
* 프로그램 실행 시 HandAnnot Class에서 한 번 선언되며 필요 클래스에 Parameter로 전달되어 최초 선언된 하나의 Model Class 공유한다.
* 대표적으로 Image Data, Annotation Info, Flag와 같은 정보를 포함한다.
* Getter(), Setter() 를 통해 데이터를 가져오거나 바꾸는 형식으로 구현
* Python의 고질적 문제인 Call by Reference로 반환하는 방식 때문에 Copy Module을 사용
* 일부 메서드는 필요한 정보만 반환받도록 하는 파라미터를 입력

### HandAnnot

* QMainWindow Class를 상속받아, 프로그램 구동에 핵심이 되는 ViewModel 역할 담당
* View와 Model 및 Method를 연결해주며, 필요 시 Model의 데이터에 접근해 적절하게 사용
* Draw, Zoom Class를 선언한 뒤, Stacked Widget에 포함시켜 기능에 따라 적절하게 필요한 위젯을 Main Window에 포함하고 있는 Scroll Area( 확대 시 스크롤로 화면 이동 ) 출력시키며 Event Control
* 기본적으로 Draw Class를 출력시키며 도형 그리기를 위한 Mouse Event를 제어
* Ctrl Key 입력 시 Zoom Class를 출력시키며 Zoom 기능을 위한 Key, Wheel Event를 제어
* 외에도 File Open, Save, Set Flag, Delete Object, Undo 등의 기능을 포함

#### Draw

* QWIdget Class를 상속받아 도형 즉, 주석 정보 입력에 핵심이 되는 Mouse Tracking Event를 담당
* HandAnnot Class에서 설정된 Shape Type에 따라 Canvas에 그려지는 도형이 달라지며, 그리기가 완료되면 AddObjectDialog를 호출해 Label을 설정한 뒤, Model Class에 주석 정보( shapes )를 입력&#x20;
* 초기화 시 View( 필요 Widgets ), Model을 입력받아 클래스 변수의 값으로 설정되며, Main Window에 출력하기 위한 canvas가 선언되며 HandAnnot에서 Draw, Zoom 중 어떤 Widget을 출력할지 결정
* 플래그에 따라 도형 그리기 미리보기, Point 수정 기능을 수정&#x20;
* 그리기 종료 시 AddObjectDialog를 호출해 Label 설정 및 List Widget에 항목 추가&#x20;

#### AddObjectDialog

* QDialog Class를 상속받아 Object에 Label 부여 및 List Widget에 항목을 추가하는 역할 담당
* 내부 List Widget에 현재까지 등록된 Label을 선택해서 고를 수 있으며, 새로운 Label을 추가해 해당 Object에 Label Name을 부여 또한 가능
* 초기화 시 Model과 List Widget( Label, Object )을 받아 클래스 변수로 사용
* 종료 시 Main Window에 있는 Label List와 Object List를 현재 객체에 따라 재설정&#x20;

#### Zoom

* QWidget Class를 상속받아 이미지 크기를 조절(확대/축소) 역할 담당&#x20;
* 초기화 시 View(필요 Widgets), Model을 입력받아 클래스 변수 값으로 설정되며, Main Window에 출력하기 위한 canvas가 선언되어 Main Window에서 Ctrl 입력 시 Zoom canvas로 전환됨&#x20;
* HandAnnot Class에서 메뉴 아이템 클릭 또는 MouseWheelEvent에 따라 설정된 Zoom Type을 이용하여 Canvas에 있는 이미지 크기를 변경&#x20;
* 크기가 변경된 이미지 출력 &#x20;


---
description: >-
  MVVM 패턴에서 ViewModel 역할을 하는 프로그램의 핵심이 되는 클래스입니다. View에서 사용자가 보내는 Action을 처리하고,
  화면 갱신, 데이터 갱신 등 대부분의 작업을 처리합니다.
---

# HandAnnot

<details>

<summary>init(): void</summary>

#### I. Description

* 초기화 함수
* binding(), actionConnect(), menuRefresh() 호출

#### II. Input



#### III. Output



</details>



<details>

<summary>binding(): void</summary>

#### I. Description

* Model, Draw, Zoom 클래스를 생성 및 Display Widget과 연결하는 작업을 담당
* QStackedWidget Class를 사용해 필요 기능에 따라 Draw, Zoom으로 화면 변환하도록 설계

#### II. Input



#### III. Output



</details>

<details>

<summary>actionConnect(): void</summary>

#### I. Description

* 사용자 Action과 기능 메서드를 연결하는 메서드&#x20;
* 각 메서드는 View의 요청을 처리하고 필요에 따라 화면 갱신, 데이터 갱신을 진행

#### II. Input



#### III. Output



</details>



<details>

<summary>openFile(): void</summary>

#### I. Description

* 이미지 파일 열기
  * QFileDialog.getOpenFileName() 함수를 이용하여 파일 경로명 얻기&#x20;
  * model 초기화
    * 새로운 파일을 불러올 때 초기화
  * Utils.ImageProc.loadImgData 함수에 파일경로를 입력받아 이미지 데이터 불러오기&#x20;
  * isExistJsonFile()함수에 파일경로를 입력받아 해당 이미지 파일에 json파일 존재 확인
    * json 파일이 존재할 경우
      * json 데이터를 dict 데이터로 변환
      * Utils.ConvertAnnotation.normalization() 함수에 변환된 dict 형태의 주석 정보를 입력하여 정규화&#x20;
      * 정규화된 주석 정보를 model에 저장&#x20;
    * json 파일이 존재하지 않을 경우
      * 파일경로, 이미지 가로 길이, 이미지 세로 길이를 model에서 dict형식의 annot\_info에 저장
  * 이미지 데이터를 model에 저장
  * 메뉴 아이템 활성화
  * 이미지 출력&#x20;

#### II. Input



#### III. Output



</details>

<details>

<summary>isExistJsonFile( filepath ): Bool</summary>

#### I. Description

* 입력받은 이미지 파일 경로에 같은 파일 이름을 가진 json 파일이 존재하는지 확인&#x20;
  * filepath 이용하여 파일 이름 분리
    * os 모듈 사용&#x20;
  * json 파일경로 이름 설정 (self.jsonPath)
    * self.jsonPath = 이미지가 들어있는 폴더 경로 + 이미지 파일 이름 + '.json'&#x20;
  * json 파일이 존재할 경우 True 반환
  * json 파일이 존재하지 않을 경우 False 반환&#x20;

#### II. Input

* _**filepath: String**_
  * 이미지 파일 경로

#### III. Output

* _**True: Bool**_
* _**False: Bool**_



</details>

<details>

<summary>loadLabelList(): void</summary>

#### I. Description

* model에서 저장된 주석 정보의 label을 가져온 후 Label List Widget에 표시&#x20;
* 출력 형태: '{ label }'

#### II. Input



#### III. Output





</details>

<details>

<summary>loadOjbectList(): void</summary>

#### I. Description

* model에서 저장된 주석 정보의 label을 이용하여 Object List Widget에 표시&#x20;
* 출력 형태: '{ shape\_type }' + '\_' + '{ label }'

#### II. Input



#### III. Output



</details>

<details>

<summary>menuRefresh(): void</summary>

#### I. Description

* 메뉴 아이템 활성화/비활성화&#x20;
  * model에서 저장된 menu\_flag를 가져옴&#x20;
  * menu\_flag == True 경우 메뉴 활성화&#x20;
  * menu\_flag == False 경우 메뉴 비활성화&#x20;

#### II. Input



#### III. Output



</details>

<details>

<summary>initData(): void</summary>

#### I. Description

* 새로운 파일을 불러올 시에 데이터 초기화 목적으로 사용&#x20;
* model에 있는 데이터 초기화&#x20;
  * 이미지 원본 데이터&#x20;
  * 이미지 수정 데이터&#x20;
  * 스택에 들어있는 주석 정보&#x20;
  * 주석 정보&#x20;
  * Label, Object List Widget&#x20;

#### II. Input



#### III. Output



</details>



<details>

<summary>saveJson(): void</summary>

#### I. Description

* 작업된 이미지를 json 파일로 저장
  * 이미지 데이터 불러오기
    * 이미지 데이터가 없을경우 return
  * 작업된 주석 정보를 불러온 후 Utils.ConvertAnnotation.denormalization() 함수에 주석정보, 이미지 가로 길이, 이미지 세로 길이를 입력하여 정규화 해제
  * 정규화 해제된 주석 정보 반환 받기&#x20;
  * Utils.ConvertAnnotation.dict2Json() 함수에 정규화 해제된 주석과 지정한 json 파일 경로를 입력하여 json 파일로 저장&#x20;
  * Resource/Image 폴더에 json 파일이 저장됨&#x20;

#### II. Input



#### III. Output



</details>



<details>

<summary>exit(): void</summary>

#### I. Description

* 프로그램 종료&#x20;

#### II. Input



#### III. Output



</details>



<details>

<summary>setGesture( hand_dir ): void</summary>

#### I. Description

* Action 클릭 시, 인자로 입력받은 손의 방향( hand\_dir )에 따라 Hand Gesture Annotation을 위한 틀을 생성하기 위한 메서드
  * hand\_dir == 'right'일 경우 엄지손가락이 왼쪽에서 시작
  * hand\_dir == 'left'일 경우 엄지손가락이 오른쪽에서 시작
* 0 \~ 20까지 21개 인덱스가 존재하며, 각 Index 별 좌표 정보를 Model에 추가&#x20;
* Draw Class의 addOjbect() 메서드를 호출해 Shape 정보를 Model에 추가

#### II. Input

* _**hand\_dir: String**_
  * 손 방

#### III. Output



</details>

<details>

<summary>setDraw( shape, draw ): void</summary>

#### I. Description

* 입력 파라미터에 따라 모양의 종류를 결정하고, 해당하는 모양 마다 Flag를 Set&#x20;
* Polygon의 경우 시작점을 클릭하기 전에 Draw가 끝나면 안되기 때문에 Keep Tracking 플래그를 Set&#x20;
* Dot의 경우 점이 하나만 필요 즉, 한 번의 클릭으로 Draw를 끝내야 하기 때문에 Action을 요청하자 마자 Tracking을 시작
* Hand Gesture의 경우 Draw 기능이 필요 없기 때문에 인자로 False로 전달받아 Draw 기능을 비활성화 한다.
* 나머지는 Canvas를 초기화 해준 뒤, 기본적으로 Draw Flag는 True로 Setting, 현재 그리기 모드 저장, 이전에 저장되어 있던 좌표를 비워주고, 상태바에 현재 모양을 출력해준다.

#### II. Input

* _**shape: String**_
  * 추가하고자 하는 도형의 모양
* _**draw: Bool**_
  * defalt = True
  * Draw Flag Setting

#### III. Output



</details>

<details>

<summary>setRetouch(): void</summary>

#### I. Description

* 각 Point의 좌표 수정을 위한 Action Setting 메서드
* On / Off 기능으로 활성화되어 있는 상태에서 Action을 요청받는다면 비활성화 시키고, 반대라면 활성화 시킨다.
* Model의 Retouch Flag 수정

#### II. Input



#### III. Output



</details>

<details>

<summary>setAuto(): void</summary>

#### I. Description

* 불러온 이미지에 대해 자동으로 Hand Gesture Points를 예측한 결과 Object를 추가하기 위한 Action과 연결된 메서드
* 원본 이미지를 불러와 Utils의 Auto Annotation 관련 메서드를 호출한다.
* 이미지에 추출된 좌표가 없다면 에러 다이얼로그를 띄운다.

#### II. Input



#### III. Output



</details>



<details>

<summary>undo(): void</summary>

#### I. Description

* 도형 그리기, 수정, Label/Object list의 상태 복원
  1. model에 있는 Undo\_flag를 가져와서 Undo\_flag가 False이면 return&#x20;
  2. model에 stack 형태로 저장되어 있는 주석 정보를 pop 하여 이전에 작업된 주석 정보로 되리기

#### II. Input



#### III. Output



</details>



<details>

<summary>setZoom(): void</summary>

#### I. Description

* 메뉴 아이템 zoom in / zoom out 클릭 시 이미지 확대/축소
  * 입력받은 zoom\_type을 model에 저장&#x20;
  * Zoom.resizeZoomInOut() 함수 호출
  * 이미지 출력&#x20;

#### II. Input



#### III. Output



</details>

<details>

<summary>keyPressEvent( event ): void</summary>

#### I. Description

* Ctrl 키 입력 시 Zoom Canvas 상태로 전환&#x20;

#### II. Input



#### III. Output



</details>

<details>

<summary>keyReleaseEvent( event ): void</summary>

#### I. Description

* Ctrl 키 해제 시 Draw Canvas로 전환&#x20;

#### II. Input



#### III. Output



</details>



<details>

<summary>contextMenuEvent( event  ): void</summary>

#### I. Description

* 오른쪽 마우스 클릭 시 context menu 출력&#x20;
* context menu
  * Polygon
  * Right hand gesture
  * Left hand gesture
  * Rectangle
  * Circle
  * Line
  * Dot
* 아이템 클릭 시 setDraw(), setGesture() 함수 호출&#x20;

#### II. Input



#### III. Output



</details>



<details>

<summary>objectClicked(): void</summary>

#### I. Description

* 삭제 기능을 위한 메서드로 Object List에 있는 Object를 클릭 시, 해당 Object의 Index를 Model에 저장하고 displaySeletedObject()를  호출해 어떤 Object가 선택되었는지 표시

#### II. Input



#### III. Output



</details>

<details>

<summary>objectDoubleClicked(): void</summary>

#### I. Description

* Object List에서 Object를 더블 클릭 시 삭제하기 위한 메서드
* Model로부터 선택된 Object의 Index 값을 불러와 Ojbect List에서 없앰과 동시에 deleteObject()를 호출해 Object를 삭제한다.
* 이후 Canvas에 변경사항을 반영한다.

#### II. Input



#### III. Output



</details>

<details>

<summary>deleteObject(): void</summary>

#### I. Description

* Model로부터 선택된 Object의 Index 값을 불러와 Annotation Info 안의 정보를 삭제하고 변경사항을 Model의 Scaled Image에 적용한다.

#### II. Input



#### III. Output



</details>

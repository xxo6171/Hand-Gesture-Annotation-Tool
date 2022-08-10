---
description: >-
  본 프로그램 HandAnnot의 핵심 기능을 포함하고 있는 클래스로, Mouse Event 처리를 통해 주석 정보 입력을 주로 담당하고 있는
  클래스입니다.
---

# Draw

<details>

<summary>init(): void</summary>

#### I. Description

* Draw Class 초기화 함수
* View( List Widget ), Model을 인자로 받아 멤버 변수로 초기화
* Draw 기능만을 위한 Canvas 선언

#### II. Input

* _**View: List\[ label\_list, object\_list ]**_
  * Object 추가를 위한 List Widgets
* _**Model: Model**_

#### III. Output



</details>



<details>

<summary>setCanvas(): void</summary>

#### I. Description

* Canvas에 Model 안에 있는 현재 Scaled Image를 출력하는 함수
* 입력 파라미터인 reset\_canvas Flag가 True이면, 원본 이미지를 불러와 주석 정보 적용 작업을 거친 이미지를 Scaled Image에 반영시킨 이후, 출력을 진행한다.

#### II. Input

* _**reset\_canvas: Bool**_
  * Default = True

#### III. Output



</details>



<details>

<summary>mousePressEvent( event ): void</summary>

#### I. Description

* Point Retouch 시작을 위한 이벤트
* Draw Flag 비활성화, Retouch Flag 활성화 시에만 작동
* 모델에서 불러온 Point Range에 따라 클릭했을 때, 변경하고자 하는 Point 범위를 결정
* 클릭 했을 때의 좌표가 현재 주석 정보에 있는 Point +- Range일 때, 해당 Point를 이동하고자 하는 Point로 설정한다.
* 좌표 수정은 플래그에 따라 mouseMoveEvent()에서 처리한다.

#### II. Input

* _**event: QMouseEvent**_

#### III. Output



</details>

<details>

<summary>mouseMoveEvent( event ): void</summary>

#### I. Description

* 마우스 포인터 이동 이벤트 처리
* Tracking On: 해당 위젯 범위에 마우스가 이동할 때마다 이벤트 처리 메서드\
  ( mouseMoveEvent ) 실행
* Tracking Off: 해당 위젯 범위에 마우스 Click & Drag 시 이벤트 처리 메서드\
  ( mouseMoveEvent ) 실행
* Tracking 된 좌표는 실시간으로 Model에 반영
* Draw Flag 활성화 시, 주석 정보 입력을 위한 draw() 메서드 호출
* Draw Flag 비활성화, Retouch Flag 활성화 시, 좌표 수정을 위한 movePoint() 메서드 호출

#### II. Input

* **event: **_**QMouseEvent**_

#### III. Output



</details>

<details>

<summary>mouseReleaseEvent( event ): void</summary>

#### I. Description

* 주석 정보( Polygon & Hand Gesture ) 입력을 위한 Event 처리 메서드
* Draw Flag가 활성화 되었을 때만 기능 작동
* Mouse Release 시 호출되는 메서드
* Create Menu 클릭 시 Draw Flag가 활성화 되며, 도형에 따라 클릭했을 때 프로그램 이벤트 처리가 조금씩 달라진다.
* Polygon: \
  &#x20;다각형을 그려나가다가 시작점을 클릭했을 때, 그리기 종료
  * Keep Tracking Flag로 제어
* Dot: \
  &#x20;한 번의 클릭으로 그리기 종료
  * Menu Action 클릭 시 바로 그리기 시작하는 방식으로 구현
* Others: \
  &#x20;두 번의 클릭만을 필요로 한다.
* 입력 작업이 끝나면 addObject() 메서드를 호출해 Object 추가 정보를 Model에 반영한다.

#### II. Input

* _**event: QMouseEvent**_

#### III. Output



</details>



<details>

<summary>setTracking( tracking ): void</summary>

#### I. Description

* Mouse Tracking 기능 활성화 / 비활성화
* 인자로 입력받은 Bool 값에 따라 Flag 및 Widget 내부 Tracking 여부를 결정

#### II. Input

* _**tracking: Bool**_

#### III. Output





</details>



<details>

<summary>draw(): void</summary>

#### I. Description

* 주석 정보 입력에 핵심이 되는 메서드
* 마우스 이동에 따라 주석 정보가 어떻게 그려질 것인지 Canvas에서 실시간으로 확인할 수 있도록 한다.
* Scaled Image를 불러와 도형 종류에 따라 그려지는 모습을 겹쳐 실시간으로 표시한다.
* Model.cur\_points에 들어가는 좌표들은 정규화된 형태이기 때문에 역 정규화 과정을 포함

#### II. Input



#### III. Output



</details>



<details>

<summary>addObject(): void</summary>

#### I. Description

* 주석 정보 추가를 위한 Dialog를 호출하고, 추가된 주석 정보를 Main Window에 적용

#### II. Input



#### III. Output



</details>



<details>

<summary>movePoint(): void</summary>

#### I. Description

* Point Retouch를 위한 메서드
* mousePressEvent() 메서드와 연계되어 선택된 Point의 좌표를 수정하기 위한 메서드
* mouseMoveEvent()에서 호출되며, 좌표는 정규화된 형태로 Model에 반영된다.
* Canvas에 실시간 반영된다.

#### II. Input



#### III. Output



</details>

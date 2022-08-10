---
description: 추가된 주석정보 Object를 반영하는 기능을 담당하고 있는 클래스로 다이얼로그 형태를 통해 Label을 설정하고 Model에 반영합니다.
---

# AddObjectDialog

![](../.gitbook/assets/image.png)

<details>

<summary>init( view, model ): void</summary>

#### I. Description

* 클래스 초기화 메서드
* List Widgets를 입력 받아 멤버 변수로 초기화
* Action Connect
* Dialog 내부 List Widget 초기화 메서드 호출

#### II. Input

* _**view: List\[ ObjectListWidget, LabelListWidget ]**_
* _**model: Model**_

#### III. Output



</details>



<details>

<summary>initListWidget(): void</summary>

#### I. Description

* Dialog 내 Label List 표시 위젯 초기화
* 현재 Model에 있는 Label List 목록을 Widget에 표시한다.

#### II. Input



#### III. Output



</details>



<details>

<summary>clickItem(): void</summary>

#### I. Description

* Dialog 내의 List Widget Item을 클릭하면 해당 목록의 텍스트를 Line Edit에 입력한다.

#### II. Input



#### III. Output



</details>

<details>

<summary>doubleClickItem(): void</summary>

#### I. Description

* 더블클릭 시 setLabel() 호출

#### II. Input



#### III. Output



</details>



<details>

<summary>setLabel(): void</summary>

#### I. Description

* 현재 Line Edit에 입력된 Label Name을 Model에 반영
* 중복 시 추가 입력 안함
* closeDialog() 메서드 호출

#### II. Input



#### III. Output



</details>

<details>

<summary>setObject(): void</summary>

#### I. Description

* Main Window에 있는 List Widgets에 변경사항을 반영
* Label Name, Object 추가

#### II. Input



#### III. Output



</details>



<details>

<summary>closeDialog(): void</summary>

#### I. Description

* Dialog 종료와 동시에 현재 설정된 도형의 주석 정보를 Model에 반영한다.
* setObject() 메서드를 호출

#### II. Input



#### III. Output



</details>

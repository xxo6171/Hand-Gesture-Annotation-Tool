---
description: Mediapipe Hands 모듈을 이용한 자동 손 좌표 찾기를 위한 Util
---

# AutoAnnotation

<details>

<summary>autoAnnotation( img ): hand_landmarks</summary>

#### I. Description

* img를 입력받아 Google의 Mediapipe Hand 모듈을 활용해 Hand Landmarks( 21개 )를 찾아 반환하는 메서드
* 좌표를 찾을 수 없는 경우 예측 값이 음수로 나타나게 되어 제대로 찾았는지 확인할 수 있다.
* 예측 값은 정규화된 수 \[0.0 \~ 1.0]로 나타난다.

#### II. Input

* img: ndArray
  * 이미지 배

#### III. Output

* **hand**_**landmarks: mediapipe hand**_** landmarks**

</details>

<details>

<summary>landmarksToList( landmarks ): pos_list</summary>

#### I. Description

* Mediapipe Hands를 통해 예측한 결과는 자체 데이터 포맷으로 나오게 되는데, 이를 사용 상의 편의성을 위해 List로 변환해주는 작업을 진행하는 메서드&#x20;
* Point를 찾지 못했을 경우 예측 좌표가 음수로 나오게 되는데, 이 경우 찾지 못한 좌표는 0.5, 0.5로 초기화해 차후 수정을 할 수 있도록 만들어 둔다.

#### II. Input

* **landmarks: **_**mediapipe hand**_** landmarks**

#### III. Output

* _**pos\_list: List\[\[x, y], ... ]**_

_****_

</details>

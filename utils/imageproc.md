---
description: opencv 함수를 이용하여 이미지 처리를 위한 Util
---

# ImageProc

<details>

<summary>loadImgData( filepath ): img, w, h, c</summary>

#### I. Description

* 입력받은 이미지 파일경로를 이용하여 cv2.imread() 함수로 이미지 읽기
  * 이미지를 읽은 후 img, width, height, channel 반환

#### II. Input

* _**filepath: String**_
  * 이미지 파일 경로

#### III. Output

* _**img: ndArray**_
  * 이미지 데이터
* _**width: integer**_
  * 이미지 가로 길이
* _**height: integer**_
  * 이미지 세로 길이
* _**channel: integer**_
  * 이미지 채널

</details>

<details>

<summary>resizeImgData( img, scaleRatio, interpolation ): img, w, h, c</summary>

#### I. Description

* 입력받은 이미지 데이터와 배율, 보간법을 이용하여 cv2.resize() 함수로 이미지 크기 조절
  * interpolation == 'LINEAR'의 경우 cv2.INTER\_LINEAR(쌍선형보간법)
  * interpolation == 'AREA'의 경우 cv2.INTER\_AREA(영역보간법)
  * resize된 image, width, height, channel 반환

#### II. Input

* _**img: ndArray**_
  * 이미지 데이터&#x20;

<!---->

* _**scaleRatio: float**_
  * 확대/축소에 따른 배율&#x20;

<!---->

* _**interpolation: String**_
  * 보간법
    * 'LINEAR': 이미지 확대&#x20;
    * 'AREA': 이미지 축소&#x20;

#### III. Output

* _**img: ndArray**_
  * resize된 이미지 데이터
* _**width: integer**_
  * resize된 이미지 가로 길이
* _**height: integer**_
  * resize된 이미지 세로 길이
* _**channel: integer**_
  * 이미지 채널

</details>

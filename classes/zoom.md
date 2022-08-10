# Zoom

<details>

<summary>init(): void</summary>

#### I. Description

* model 세팅
* canvas, stacked\_widget 바인딩

#### II. Input

#### III. Output



</details>

<details>

<summary>setCanvas(): void</summary>

#### I. Description

* Canvas에 Model 안에 있는 현재 Scaled Image를 출력하는 함수
* 원본 이미지를 불러와 주석 정보 적용 작업을 거친 이미지를 Scaled Image에 반영시킨 이후, 출력을 진행한다.

#### II. Input



#### III. Output



</details>

<details>

<summary>wheelEvent( event ): void</summary>

#### I. Description

* Ctrl + MouseWheel up/down 시 이미지 확대/축소
  * MouseWheel Up 시 확대
    * Zoom type=='In' 설정
  * MouseWheel Down 시 축소
    * Zoom type=='Out' 설정
  * resizeZoomInOut() 함수 호출

#### II. Input



#### III. Output



</details>

<details>

<summary>resizeZoomInOut(): void</summary>

#### I. Description

* model에 저장된 이미지 데이터와 배율, zoom\_type을 가져와서 Utils.ImageProc.resizeImgData 함수를 이용하여 이미지 크기 조절
  * zoom\_type == 'In'
    * 확대
    * 기존배율 \* 1.25
    * 최대 확대 배율 3.05로 고정
  * zoom\_type == 'Out'
    * 축소
    * 기존배율 \* 0.8
    * 최대 축소 배율 0.21로 고정
  * 확대/축소 작업 중 원본 크기 1로 나누어 떨어지지 않음
    * 0.99 < 배율 < 1.001 의 경우 배율 1로 설정
  * resize된 이미지 model에 저장
  * setCanvas() 함수로 이미지 출력

#### II. Input



#### III. Output



</details>

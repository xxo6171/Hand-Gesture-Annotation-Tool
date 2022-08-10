# Display



<details>

<summary>img2QPixmap( img, w, h, c ): qPixmap</summary>

#### I. Description

* ndArray 형식으로 불러온 Image 를 QPixmap 객체로 변경하기 위한 메서드

#### II. Input

* _**img: ndArray**_
* _**w: Integer**_
* _**h: Integer**_
* _**c: Integer**_

#### III. Output

* _**qPixmap: QPixmap**_

</details>

<details>

<summary>loadQImg( model ): qimg, annot_info, point_scale</summary>

#### I. Description

* Model의 정보를 이용해 주석 정보를 Image에 표현하기 위한 전처리 작업을 하는 메서드
* 원본 이미지를 img2QPixmap() 메서드를 통해 QPixmap으로 변환한 뒤, Scaled Image로 만들어준다.
* 추가로 주석정보는 원활한 출력을 위해 역정규화 시키고 각 Point의 범위와 함께 반환한다.

#### II. Input

* _**model: Model**_

#### III. Output

* _**qimg: QPixmap**_
* _**annot\_info: Dictionary**_
* _**point\_scale: Integer**_

</details>



<details>

<summary>setDisplayAnnotInfo( qimg, annot_info, point_scale): qimg</summary>

#### I. Description

* 입력받은 QPixmap 객체, 주석 정보, Point 범위를 이용해 QPixmap 객체에 현재 주석정보를 표현해주는 메서드
* 각 도형 별 Case로 나누어 색과 모양을 다르게 표현하며, 처리된 QPixmap 데이터를 반환한다.

#### II. Input

* _**qimg: QPixmap**_
* _**annot\_info: Dictionary**_
* _**point\_scale: Integer**_

#### III. Output

* _**qimg: QPixmap**_

</details>

<details>

<summary>displaySelectedObject( idx, qimg, denorm_annot ): qimg</summary>

#### I. Description

* 주석 정보에서 해당 인덱스에 해당하는 도형에 강조 표시를 하기 위한 메서드
* Object List Widget과 연계되는 메서드로, 삭제 이전에 어떤 도형을 삭제하게 되는지 가시적으로 확인하기 위한 메서드이다.

#### II. Input

* _**idx: Integer**_
* _**qimg: QPixmap**_
* _**denorm\_annot: Dictionary**_

#### III. Output

* _**qimg: QPixmap**_

</details>



<details>

<summary>displayImage( canvas, img, w, h ): void</summary>

#### I. Description

* canvas( QLabel )에 Image를 setting하는 메서드

#### II. Input

* _**canvas: QLabel**_
* _**w: Integer**_
* _**h: Integer**_

#### III. Output



</details>

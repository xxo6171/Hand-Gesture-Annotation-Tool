---
description: 프로그램 구동에 필요한 모든 데이터를 변수로 포함하고 있는 클래스로, 메서드는 코드로 보기 어렵지 않기 때문에 생략합니다.
---

# Model\_Method 작성 중단

<details>

<summary>init(): void</summary>

#### I. Description

* 프로그램 구현에 필요한 모든 데이터 정보 초기화
* None, \[], {}, False 등 Default 값
* initAnnotInfo() 호출

#### II. Input



#### III. Output



</details>

<details>

<summary>getImgData(): img, w, h ,c </summary>

#### I. Description

* 원본 이미지 데이터를 반환

#### II. Input



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

<summary>setImgData( img, w, h, c ): void</summary>

#### I. Description

* 원본 이미지 데이터 저장

#### II. Input

* _**img: ndArray**_
  * 이미지 데이터
* _**width: integer**_
  * 이미지 가로 길이
* _**height: integer**_
  * 이미지 세로 길이
* _**channel: integer**_
  * 이미지 채널

#### III. Output



</details>

<details>

<summary>getImgScaled(): img, w, h, c</summary>

#### I. Description

* Scaled Image와 width, height, channel Info를 반환받는 메서드

#### II. Input

* _**no\_img: Bool**_
  * 이미지가 필요 없는 부분에서 불필요하게 이미지를 반환받지 않기 위한 Flag

#### III. Output

* _**img\_scaled: ndArray**_
  * 플래그에 따라 img\_scaled는 제외 가능
* _**img\_scaled\_width: Integer**_
* _**img\_scaled\_height: Integer**_
* _**img\_scaled\_channel: Integer**_

</details>

<details>

<summary>setImgScaled( img, w, h, c ): void</summary>

#### I. Description

* Scaled Image를 초기화하는 메서드
* 입력 파라미터를 Model의 클래스 변수에 삽입
* 입력된 이미지가 None일 경우 None으로 초기화

#### II. Input

* _**img: ndArray**_
* _**width: Integer**_
* _**height: Interger**_
* _**channel: Integer**_

#### III. Output



</details>

<details>

<summary>getScaleRatio(): scale_ratio</summary>

#### I. Description

* 이미지 확대/축소 기능에 사용되는 이미지 배율을 반환

#### II. Input



#### III. Output

* _**ratio: Float**_
  * 이미지 배율

</details>

<details>

<summary>setScaleRatio( ratio ): void</summary>

#### I. Description

* 이미지 확대/축소 기능에 사용되는 이미지 배율을 저장

#### II. Input

* _**ratio: Float**_
  * 이미지 배율

#### III. Output



</details>

<details>

<summary>initLabelList(): void</summary>

#### I. Description

* label\_list의 내용을 초기화하는 메서드
* List.clear() 메서드 이용

#### II. Input



#### III. Output



</details>

<details>

<summary>getLabelList(): label_list</summary>

#### I. Description

* label\_list를 반환하는 메서드
* copy() 메서드를 이용해 Call-by-Value로 전달

#### II. Input



#### III. Output



</details>

<details>

<summary>setLabel( label ): void</summary>

#### I. Description

* 인자로 입력 받은 String을 label\_list에 추가하는 메서드
* List.append() 메서드 이용

#### II. Input



#### III. Output



</details>

<details>

<summary>initAnnotInfo(): void</summary>

#### I. Description

* 이미지 주석 정보를 초기화

#### II. Input



#### III. Output



</details>

<details>

<summary>getAnnotInfo(): annot_info</summary>

#### I. Description

* 이미지 주석 정보를 반환

#### II. Input



#### III. Output

* _**annot\_info: Dictionary**_
  * 이미지 주석 정보

</details>

<details>

<summary>setAnnotDict( dict ): void</summary>

#### I. Description

* 데이터가 모두 들어 있는 dict 형태의 이미지 주석 정보를 저장
* 이미지 파일에 json 파일이 존재할 때 json 안의 전체 정보 저장 목적

#### II. Input

* _**dict: Dictionary**_
  * 데이터가 모두 들어 있는 이미지 주석 정보 &#x20;

#### III. Output



</details>

<details>

<summary>setAnnotInfo( filepath, width, height): void</summary>

#### I. Description

* 이미지의 정보를 저장
  * 이미지 경로
  * 이미지 가로 길이
  * 이미지 세로 길이
* 이미지 파일에 json 파일이 존재하지 않을 때 초기 이미지의 정보 저장 목적

#### II. Input

* _**filepath: String**_
  * 이미지 파일 경로
* _**width: integer**_
  * 이미지 가로 길이
* _**height: integer**_
  * 이미지 세로 길이

#### III. Output



</details>

<details>

<summary>setCurShapeToDict(): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>resetCurPoints(): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>deleteShape( idx ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>addCurPoint( point, raw ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>getCurPoints(): cur_points_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setCurPoints( points ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>getCurLabel( label ): cur_label_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setCurLabel( label ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>getCurShapeType(): cur_shape_type_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setCurShapeType(shape_type): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>initAnnotStack(): void</summary>

#### I. Description

* 주석 정보 스택 초기화
* 새 파일을 불러올 때 스택 초기화 목적&#x20;

#### II. Input



#### III. Output



</details>

<details>

<summary>popAnnot(): annot.pop()</summary>

#### I. Description

* 주석 정보 스택에서 마지막에 위치한 요소의 주석 정보를 pop 하여 반환
* 되돌리기 기능을 실행할 때 popAnnot()을 이용하여 저장된 annot 리스트에서 마지막에 위치한 요소의 주석 정보를 꺼내어 반환 할 수 있음&#x20;

#### II. Input



#### III. Output

* _**annot.pop(): Dictionary**_
  * list 형태인 annot에 마지막 위치한 요소를 내보낸 주석 정보

</details>

<details>

<summary>pushAnnot( dict ): void</summary>

#### I. Description

* 주석 정보를 list 형태인 annot에 저장
* 되돌리기 기능을 위한 주석 정보 저장 목적

#### II. Input

* _**dict: Dictionary**_
  * 이미지 주석 정보

#### III. Output



</details>

<details>

<summary>getZoomType(): zoom_type</summary>

#### I. Description

* 이미지 확대/축소 기능에 사용되는 zoom\_type 반환

#### II. Input



#### III. Output

* _**zoom\_type: String**_
  * 확대/축소 타입

</details>

<details>

<summary>setZoomType( type ): void</summary>

#### I. Description

* 이미지 확대/축소 기능에 사용되는 확대/축소 타입을 저장
  * type == 'In' 경우 확대 준비 상태&#x20;
  * type == 'Out' 경우 축소 준비 상태&#x20;

#### II. Input

* _**type: String**_
  * 확대/축소 타입

#### III. Output



</details>

<details>

<summary>getUndoFlag(): undo_flag</summary>

#### I. Description

* 되돌리기 기능에 사용되는 undo\_flag를 반환

#### II. Input



#### III. Output

* undo\_flag: Bool
  * 되돌리기 기능에 사용되는 undo\_flag

</details>

<details>

<summary>setUndoFlag( flag ): void</summary>

#### I. Description

* 되돌리기 기능에 사용되는 undo\_flag를 저장
  * flag == True 경우 되돌리기 기능을 설정 준비 상태&#x20;
  * flag == False 경우 되돌리기 기능을 해제 준비 상태&#x20;

#### II. Input

* _**flag: Bool**_
  * 되돌리기 기능을 설정/해제하기 위한 flag

#### III. Output



</details>

<details>

<summary>getMenuFlag(): menu_flag</summary>

#### I. Description

* 메뉴 아이템 활성화/비활성화 기능에 사용되는 menu\_flag를 반환

#### II. Input



#### III. Output

* _**menu\_flag: Bool**_
  * 메뉴 아이템 활성화/비활성화 기능에 사용되는 menu\_flag

</details>

<details>

<summary>setMenuFlag( flag ): void</summary>

#### I. Description

* 메뉴 아이템 활성화/비활성화 기능에 사용되는 menu\_flag를 저장
  * flag == True 경우 메뉴 아이템 활성화
  * flag == False 경우 메뉴 아이템 비활성화

#### II. Input

* _**flag: Bool**_
  * 메뉴 아이템 활성화/비활성화 기능을 설정하기 위한 flag

#### III. Output



</details>

<details>

<summary>getDrawFlag(): draw_flag_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setDrawFlag( flag ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>getRetouchFlag(): retouch_flag_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setRetoushFlag( flag ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>isTracking(): tracking_flag_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setTracking( flag ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>isKeepTracking(): keep_tracking_flag_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setKeepTracking( flag ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>getPrePos(): pre_mouse<em>_</em>pos_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setPrePos( list ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>getClickPointRange(): click_point<em>_</em>range_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>getMovePoint(): move_point_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setMovePoint( point ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>getSelectedObjectIndex(): selected_object_idx_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

<details>

<summary>setSelectedObjectIndex( idx ): void_미완</summary>

#### I. Description



#### II. Input



#### III. Output



</details>

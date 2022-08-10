---
description: Annotation 정보를 변환하기 위한 메서드 Util
---

# ConvertAnnotation

<details>

<summary>dict2Json( dict, filepath ): void</summary>

#### I. Description

* 입력받은 주석 정보와 json 파일 경로를 이용하여 json.dump() 함수로 파일 경로에 맞게 json 파일 저장 &#x20;

#### II. Input

* _**dict: Dictionary**_
  * 주석 정보&#x20;
* _**filepath: String**_
  * 지정된 json 파일 경로&#x20;



#### III. Output



</details>

<details>

<summary>json2Dict( filepath ): annot_info</summary>

#### I. Description

* 입력받은 json 파일 경로를 이용하여 json 형태의 데이터를 json.load() 함수로 dict 형태의 데이터로 변환

#### II. Input

* _**filepath: String**_
  * json 파일 경로&#x20;

#### III. Output

* _**annot\_info: Dictionary**_
  * dict 형태로 변환된 주석 정보&#x20;

</details>



<details>

<summary>normalization( annotdict, w, h ): annot_dict</summary>

#### I. Description

* Annotation Info의 좌표를 정규화 시키는 메서드&#x20;
* annot\_dict 안의 Points들을 width, height로 각각 나누어 0과 1 사이의 숫자로 만든다.

#### II. Input

* _**annot\_dict: Dictionary**_
  * 주석 정보
* _**w: Integer**_
* _**h: Integer**_

#### III. Output

* _**annot\_dict: Dictionary**_
  * 정규화된 정보



</details>

<details>

<summary>denormalization( annot dict, w, h ): annot dict</summary>

#### I. Description

* Annotation Info의 좌표를 역정규화 시키는 메서드&#x20;
* annot\_dict 안의 Points들을 width, height로 각각 곱해 픽셀 값으로 만든다.

#### II. Input

* _**annot\_dict: Dictionary**_
  * 주석 정보
* _**w: Integer**_
* _**h: Integer**_

#### III. Output

* _**annot\_dict: Dictionary**_
  * 역정규화된 정보

</details>

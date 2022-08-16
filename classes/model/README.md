---
description: 프로그램 구동에 필요한 모든 데이터를 변수로 포함하고 있는 클래스로, 메서드는 코드로 보기 어렵지 않기 때문에 생략합니다.
---

# Model

* img\_origin: ndArray
* img\_origin\_width: Integer
* img\_origin\_height: Integer
* img\_origin\_channel: Integer



* img\_scaled: QPixmap
* img\_scaled\_width: Integer
* img\_scaled\_height: Integer
* img\_scaled\_channel: Integer



* scale\_ratio: Float
* top: Integer annot: List
* label\_list: List annot\_info: Dictionary



* cur\_points: List
* cur\_label: String
* cur\_shape\_type: String
* zoom\_type: String



* menu\_flag: Bool
* draw\_flag: Bool
* retouch\_flag: Bool
* tracking\_flag: Bool
* keep\_tracking\_flag: Bool
* undo\_flag: Bool



* pre\_mouse\_pos: List
* cur\_mouse\_pos: List
* click\_point\_range: Integer
* move\_point: List



* selected\_object\_idx: Integer

# Item 속성

지정된 인덱스의 구성을 위한 [**Config** 개체](../config/index) 를 검색합니다.

#### \[JavaScript\]

_doc_ = editor.Configs. **Item**( _Index_ );

#### \[VBScript\]

_doc_ = editor.Configs. **Item**( _Index_ )

## 매개 변수

_Index_

1부터 시작하는 정수로된 구성의 인덱스를 지정합니다.

## 예시

#### \[JavaScript\]

alert( "Name for the first configuration: " + editor.Configs.Item(1).Name );

#### \[VBScript\]

alert "Name for the first configuration: " & editor.Configs.Item(1).Name

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
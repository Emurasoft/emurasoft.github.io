# Item 속성 (Windows �÷���)

지정된 인덱스의 창을 위한 window 개체를 검색합니다.

#### \[JavaScript\]

_wnd_ = shell.windows. **Item**( _Index_ );

#### \[VBScript\]

_wnd_ = shell.windows. **Item**( _Index_ )

## 매개 변수

_Index_

창의 인덱스를 1로 시작하는 정수로 지정합니다.

## 예시

#### \[JavaScript\]

alert( "Name of the first window: " + shell.windows.Item(1).Caption );

#### \[VBScript\]

alert "Name of the first window: " + shell.windows.Item(1).Caption

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.

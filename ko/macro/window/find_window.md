# FindWindow 메서드 (Window ��ü)

클래스 이름 및/또는 창 제목으로 하위 [Window 개체](../window/index) 를 검색합니다.

#### \[JavaScript\]

wndChild = wnd. **FindWindow**( _strClass_, _strCaption_ );

#### \[VBScript\]

wndChild = wnd. **FindWindow**( _strClass_, _strCaption_ )

## 매개 변수

_strClass_

창의 클래스 이름을 지정합니다. 매개 변수가 비어있는 경우에는 모든 클래스 이름이 일치합니다.

_strCaption_

창 이름 (제목)을 지정합니다. 매개 변수가 비어있는 경우에는 모든 클래스 이름이 일치합니다.

## 예시

#### \[JavaScript\]

wnd = FindWindow( "EmEditorView", "" );

alert( wnd.Caption );

#### \[VBScript\]

wnd = FindWindow( "EmEditorView", "" )

alert wnd.Caption

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.

# EE\_TOOLBAR\_CLOSE

사용자 지정 도구 모음을 닫습니다. 이 메시지를 명시적으로 또는
[Editor\_ToolbarClose](../macro/editor_toolbarclose) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_TOOLBAR\_CLOSE

(UINT)wParam = nToolbarID

## 매개 변수

_nToolbarID_

닫을 도구 모음을 지정합니다. EE\_TOOLBAR\_OPEN 메시지로부터의 반환 값입니다.

## 반환 값

메시지가 성공하거나 도구 모음 상태가 변경된 경우, 반환 값은 TRUE입니다.
메시지가 실패하거나 도구 모음 상태가 변경되지 않은 경우, 반환 값은 FALSE입니다.

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.

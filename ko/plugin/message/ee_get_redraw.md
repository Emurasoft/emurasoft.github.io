# EE\_GET\_REDRAW

다시 그리려는 EmEditor의 변경을 허락하거나 다시 그리려는 EmEditor의 변경을 막는 flag를 검색합니다.
이 메시지를 명시적으로 보내거나
[Editor\_GetRedraw 인라인 함수](../macro/editor_getredraw) 를 사용할 수 있습니다.

EE\_GET\_REDRAW

wParam = (WPARAM) 0;

lParam = (LPARAM) 0;

## 매개 변수

> 없습니다.

## 반환 값

> 현재 flag가 다시 그리려는 EmEditor의 변경을 허락하거나 다시 그리려는 EmEditor의 변경을 막는 경우
> TRUE를 반환합니다. 그렇지 않은 경우, FALSE를 반환합니다.

## 버전

> EmEditor 버전 5 이상에서만 지원됩니다.
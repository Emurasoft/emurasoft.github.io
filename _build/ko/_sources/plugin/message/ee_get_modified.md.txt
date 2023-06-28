# EE\_GET\_MODIFIED

텍스트의 수정된 상태를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetModified](../macro/editor_getmodified) 인라인 함수를 사용 할 수 있습니다.

EE\_GET\_MODIFIED

wParam = 0;

lParam = 0;

## 매개 변수

> 없습니다.

## 반환 값

> 텍스트가 수정된 경우, 반환 값은 TRUE입니다.
> 텍스트가 수정되지 않은 경우, 반환 값은 FALSE입니다.
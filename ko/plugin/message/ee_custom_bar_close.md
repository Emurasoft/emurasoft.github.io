# EE\_CUSTOM\_BAR\_CLOSE

사용자 지정 표시줄을 닫습니다. 이 메시지를 명시적으로 보내거나 [Editor\_CustomBarClose](../macro/editor_custombarclose) 인라인 함수를
사용할 수 있습니다.

EE\_CUSTOM\_BAR\_CLOSE

wParam = nCustomBarID;

lParam = 0;

## 매개 변수

_nCustomBarID_

> 닫으려는 사용자 지정 표시줄을 지정합니다.
> 이것은 EE\_CUSTOM\_BAR\_OPEN 메시지로부터의 반환 값입니다.

## 반환 값

> 메시지가 성공한 경우, 반환 값은 TRUE입니다. 메시지가 실패한 경우, 반환 값은 FALSE입니다.

## 버전

> 엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.

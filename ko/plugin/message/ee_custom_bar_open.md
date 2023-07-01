# EE\_CUSTOM\_BAR\_OPEN

사용자 지정 표시줄을 엽니다. 이 메시지를 보내기 이전에 사용자 지정 표시줄이 이미 열려있는 경우,
EmEditor는 사용자 지정 표시줄을 닫고 새로운 사용자 지정 표시줄을 엽니다.
이 메시지를 명시적으로 보내거나 [Editor\_CustomBarOpen](../macro/editor_custombaropen) 인라인 함수를
사용할 수 있습니다.

EE\_CUSTOM\_BAR\_OPEN

wParam = 0;

lParam = (LPCTSTR) (LPCTSTR) pCustomBarInfo;

## 매개 변수

_pCustomBarInfo_

> [CUSTOM\_BAR\_INFO 구조](../structure/custom_bar_info) 에 대한 포인터 입니다.

## 반환 값

> 반환 값은 EE\_CUSTOM\_BAR\_CLOSE 메시지로 사용자 지정 표시줄을 닫을 때 필요한 사용자 지정 ID입니다.
> 메시지가 실패한 경우, 반환 값은 0입니다.

## 버전

> 엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.

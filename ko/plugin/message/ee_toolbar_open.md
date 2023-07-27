# EE\_TOOLBAR\_OPEN

사용자 지정 도구 모음을 엽니다. 이 메시지를 명시적으로 또는 [Editor\_ToolbarOpen](../macro/editor_toolbaropen) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_TOOLBAR\_OPEN

wParam = 0;

lParam = (LPARAM) (TOOLBAR\_INFO\*) pToolbarInfo;

## 매개 변수

_pToolbarInfo_

[TOOLBAR\_INFO 구조](../structure/toolbar_info) 에 대한 포인터 입니다.

## 반환 값

반환 값은 custom toolbar ID (사용자 지정 도구 모음 ID)입니다. 메시지가 실패한 경우,반환 값은 0입니다.

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.

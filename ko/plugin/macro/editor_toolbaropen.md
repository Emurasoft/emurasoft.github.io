# Editor\_ToolbarOpen

사용자 지정 도구 모음을 엽니다. 이 인라인 함수를 사용하거나 [EE\_TOOLBAR\_OPEN](../message/ee_toolbar_open)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_ToolbarOpen( HWND hwnd, TOOLBAR\_INFO\* pToolbarInfo );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pToolbarInfo_

> [TOOLBAR\_INFO 구조](../structure/toolbar_info) 에 대한 포인터 입니다.

## 반환 값

> 반환 값은 custom toolbar ID (사용자 지정 도구 모음 ID)입니다. 메시지가 실패한 경우,반환 값은 0입니다.

## 버전

> 엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
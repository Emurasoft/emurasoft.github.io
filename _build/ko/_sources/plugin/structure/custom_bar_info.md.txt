# CUSTOM\_BAR\_INFO

[Editor\_CustomBarOpen](../macro/editor_custombaropen) 인라인 함수
( [EE\_CUSTOM\_BAR\_OPEN](../message/ee_custom_bar_open) 메시지)에 의해 사용됩니다.

typedef struct \_CUSTOM\_BAR\_INFO {

size\_t cbSize;

HWND hwndCustomBar;

HWND hwndClient;

LPCTSTR pszTitle;

int iPos;

} CUSTOM\_BAR\_INFO;

## 멤버

_cbSize_

> \[입력\] 바이트로 나타낸 데이터 구조의 크기입니다. EE\_CUSTOM\_BAR\_OPEN 메시지를 보내기 이전에 이 멤버를 sizeof( CUSTOM\_BAR\_INFO )로 설정합니다.

_hwndCustomBar_

> \[출력\] EE\_CUSTOM\_BAR\_OPEN 메시지가 성공했을 때 사용자 지정 모음 창에 대한 핸들이 저장됩니다.

_hwndClient_

> \[입력\] 클라이언트 창에 대한 핸들입니다.

_pszTitle_

> \[입력\] 사용자 지정 모음 제목에 사용되는 문자열입니다.

_iPos_

> \[입력\] 사용자 지정 모음 초기 위치
>
> |     |     |
> | --- | --- |
> | 0 | 창의 왼쪽 |
> | 1 | 창의 상단 |
> | 2 | 창의 오른쪽 |
> | 3 | 창의 하단 |

## 버전

> 엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.
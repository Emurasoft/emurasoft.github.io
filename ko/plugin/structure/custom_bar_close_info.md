# CUSTOM\_BAR\_CLOSE\_INFO

[EVENT\_CUSTOM\_BAR\_CLOSED 이벤트](../event/index) 에 의해 사용됩니다.

typedef struct \_CUSTOM\_BAR\_CLOSE\_INFO {

UINT nID;

int iPos;

DWORD dwFlags;

} CUSTOM\_BAR\_CLOSE\_INFO;

## 멤버

_nID_

> \[입력\] custom bar ID (사용자 지정 모음 ID).

_iPos_

> \[입력\] 닫히기 바로 직전 사용자 지정 모음의 위치
>
> |     |     |
> | --- | --- |
> | 0 | 창의 왼쪽 |
> | 1 | 창의 상단 |
> | 2 | 창의 오른쪽 |
> | 3 | 창의 하단 |

_dwFlags_

> \[출력\] 사용자 지정 모음이 닫히게 된 원인.
>
> |     |     |
> | --- | --- |
> | 0 | 사용자 지정 모음이 사용자에 의해 닫힘. |
> | CLOSED\_FRAME\_WINDOW | 프레임 창이 닫힘. |
> | CLOSED\_ANOTHER\_CUSTOM\_BAR | 사용자 지정 모음이 또다른 사용자 지정 모음이 열림으로 인해 닫힘. |

## 버전

> 엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.
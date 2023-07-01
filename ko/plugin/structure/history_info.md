# HISTORY\_INFO

[EVENT\_HISTORY 이벤트](../event/index) 에 의해 사용됩니다.

typedef struct \_HISTORY\_INFO {

size\_t cbSize;

UINT nFlags;

POINT\_PTR ptTop;

POINT\_PTR ptBottom;

UINT nChar;

LPCWSTR pszString;

} HISTORY\_INFO;

## 멤버

_cbSize_

> 바이트로 나타낸 데이터 구조의 크기입니다. EVENT\_HISTORY 이벤트를 받기 이전에 이 멤버는 ( HISTORY\_INFO )이어야
> 합니다.

_nFlags_

> 다음의 값들의 결합을 지정합니다.
>
> |     |     |
> | --- | --- |
> | HISTORY\_INSERT\_CHAR | 문자가 삽입됩니다. |
> | HISTORY\_BACK\_SPACE | 문자를 삭제하기 위해 백스페이스 키를 누릅니다. |
> | HISTORY\_DELETE\_CHAR | 문자를 삭제하기 위해 Delete 키를 누릅니다. |
> | HISTORY\_INSERT\_STRING | 문자열이 삽입됩니다. |
> | HISTORY\_DELETE\_STRING | 문자열이 삭제됩니다. |
> | HISTORY\_INSERT\_TAB\_SEL | 선택 영역을 들여쓰기 위해 탭 키를 누릅니다. |
> | HISTORY\_MODIFIED | 문서가 수정됩니다. |
> | HISTORY\_COMBINED | 이 기록 이벤트는 이전의 이벤트들과 결합되어야 합니다. |
> | HISTORY\_CR\_ONLY | 삭제된 문자는 CR만 입니다. |
> | HISTORY\_LF\_ONLY | 삭제된 문자는 LF만 입니다. |
> | HISTORY\_SEL\_BOX | 삽입된 문자열을 수직 선택입니다. |
> | HISTORY\_INSIDE\_UNDO | 작업은 실행 취소 명령 내부입니다. |
> | HISTORY\_INSIDE\_REDO | 작업은 다시 실행 명령 내부입니다. |

_ptTop_

> 이 멤버는 이전 커서 위치를 포함하고 있습니다. nFlag 멤버가 HISTORY\_INSERT\_STRING을 포함하고 있는 경우, 이
> 멤버는 선택 영역의 시작 지점입니다.

_ptBottom_

> nFlag 멤버가 HISTORY\_INSERT\_STRING을 포함하고 있는 경우, 이 멤버는 선택 영역의 끝 지점입니다. 그렇지 않으면,
> 이 멤버는 무시됩니다.

_nChar_

> nFlag 멤버가 HISTORY\_BACK\_SPACE 또는 HISTORY\_DELETE\_CHAR를 포함하고 있는 경우, 이 멤버는 삭제된
> 문자를 포함하고 있습니다.

_pszString_

> nFlag 멤버가 HISTORY\_DELETE\_STRING를 포함하고 있는 경우, 이 멤버는 삭제된 문자열을 포함하고 있습니다.

## 버전

> EmEditor 버전 9 이상에서만 지원됩니다.

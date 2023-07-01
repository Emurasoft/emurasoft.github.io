# Editor\_InsertClip

클립보드 기록의 지정된 위치에 텍스트를 삽입합니다. 이 인라인 함수를 사용하거나 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_InsertClip( HWND hwnd, LPCWSTR pszText, UINT iPos, UINT nFlags );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pszText_

> 삽입될 텍스트를 지정합니다.

_iPos_

> 클립보드 기록 내 이전 위치를 지정합니다.

_nFlags_

> 삽입되거나 삭제될 클립보드의 유형을 지정합니다.
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 클립보드 유형은 일반 텍스트입니다. |
> | SEL\_TYPE\_LINE | 클립보드 유형은 텍스트의 줄입니다. |
> | SEL\_TYPE\_BOX | 클립보드 유형은 텍스트의 수직 선택입니다. |

## 반환 값

> 반환 값은 새로운 텍스트가 삽입되는 클립보드 기록 내 위치입니다. 메시지가 실패한 경우, 반환 값은 -1입니다.

## 버전

> EmEditor 버전 9 이상에서만 지원됩니다.

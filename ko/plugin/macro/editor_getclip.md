# Editor\_GetClip

클립보드 기록의 지정된 위치에 텍스트를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetClip( HWND hwnd, LPWSTR pszBuf, UINT cchBuf, UINT iPos, UINT\* pnFlags );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pszBuf_

> 텍스트를 수신할 버퍼를 지정합니다.

_cchBuf_

> 종료된 NULL 문자를 포함한 문자 내 버퍼 크기를 지정합니다.

_iPos_

> 클립보드 기록 내 위치를 지정합니다. (UINT) -1이 지정된 경우, 클립보드 기록에서 얻는것보다 실제 클립보드 내용이 검색됩니다.

_nFlags_

> 이 값은 실제 클립보드 유형으로 채워져 있습니다.
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 클립보드 유형은 일반 텍스트입니다. |
> | SEL\_TYPE\_LINE | 클립보드 유형은 텍스트의 줄입니다. |
> | SEL\_TYPE\_BOX | 클립보드 유형은 텍스트의 수직 선택입니다. |

## 반환 값

> 반환 값은 종료된 NULL을 포함한 텍스트를 수신하는데 필요한 문자 내 pszBuf 버퍼의 크기입니다. 메시지가 실패한 경우, 반환
> 값은 -1입니다.

## 버전

> EmEditor 버전 9 이상에서만 지원됩니다.

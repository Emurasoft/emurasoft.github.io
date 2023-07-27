# CLIP\_INFO

[EE\_CLIP\_HISTORY](../message/ee_clip_history) 메시지에 의해 사용됩니다.

typedef struct \_CLIP\_INFO {

size\_t cbSize;

LPWSTR pszBuf;

UINT cchBuf;

UINT iPos;

UINT nAction;

UINT nFlags;

} CLIP\_INFO;

## 멤버

_cbSize_

바이트로 나타낸 데이터 구조의 크기입니다. [EE\_CLIP\_HISTORY](../message/ee_clip_history) 메시지를 보내기 이전에 이 멤버를
sizeof( CLIP\_INFO )로 설정합니다.

_pszBuf_

텍스트를 수신할 버퍼 또는 삽입할 텍스트를 지정합니다.

_cchBuf_

종료된 NULL 문자를 포함한 문자 내 버퍼 크기를 지정합니다.

_iPos_

클립보드 기록 내 위치를 지정합니다. _nAction_ 이 CI\_GET\_CLIP를 지정한 동안 (UINT)-1이 지정된
경우, 클립보드 기록으로부터 얻는 대신 실제 클립보드 내용이 검색됩니다.

_nAction_

다음의 값들 중 하나를 지정합니다. 하지만, CI\_INSERT\_CLIP만 CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP과 결합될 수
있습니다.

|     |     |
| --- | --- |
| CI\_GET\_CLIP | 클립보드 기록의 지정된 위치에 텍스트를 검색합니다. |
| CI\_INSERT\_CLIP | 클립보드 기록의 지정된 위치에 텍스트를 삽입합니다. |
| CI\_REMOVE\_CLIP | 클립보드 기록의 지정된 위치에 텍스트를 제거합니다. |
| CI\_GET\_POS | 클립보드 기록의 현재 위치를 검색합니다. |
| CI\_SET\_POS | 클립보드 기록의 현재 위치를 설정합니다. |
| CI\_ROTATE\_CLIP | 클립보드 기록의 현재 위치를 순환합니다. |
| CI\_FLAG\_NO\_UPDATE\_REAL\_CLIP | 클립보드 기록에 의해 현재 실제 클립보드 내용이 대체되는 것을 막습니다. 이 값은 CI\_INSERT\_CLIP과 결합하여 <br> 사용될 수 있습니다. |

_nFlags_

nAction이 CI\_INSERT\_CLIP 또는 CI\_REMOVE\_CLIP 일 때, 이 값은 삽입되거나 삭제될 클립보드의 유형을 지정합니다. nAction이 CI\_GET\_CLIP
일 때, 이 값은 실제 클립보드 유형으로 채워져 있습니다. 그렇지 않으면, 이 값은 무시되며 0이 되어야 합니다. 이 값이 필요한 경우,
다음의 값들 중 하나가 됩니다.

|     |     |
| --- | --- |
| SEL\_TYPE\_CHAR | 클립보드 유형은 일반 텍스트입니다. |
| SEL\_TYPE\_LINE | 클립보드 유형은 텍스트의 줄입니다. |
| SEL\_TYPE\_BOX | 클립보드 유형은 텍스트의 수직 선택입니다. |

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.

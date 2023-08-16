# TOOLBAR\_INFO

Used by [Editor\_ToolbarOpen 인라인 함수](../macro/editor_toolbaropen)
( [EE\_TOOLBAR\_OPEN 메시지](../message/ee_toolbar_open))와 사용자 지정 도구 모음에 관련된
이벤트에 의해 사용됩니다.

```
typedef struct _TOOLBAR_INFO {
	size_t cbSize;
	HWND hwndRebar;
	HWND hwndClient;
	LPCTSTR pszTitle;
	UINT nMask;
	UINT nID;
	UINT nFlags;
	UINT fStyle;
	UINT cxMinChild;
	UINT cyMinChild;
	UINT cx;
	UINT cxIdeal;
	UINT nBand;
	WORD wPlugInCmdID;
} TOOLBAR_INFO;
```

## 멤버

_cbSize_

바이트로 나타낸 데이터 구조의 크기입니다. TOOLBAR\_INFO 메시지를 보내기 이전에 이 멤버를 sizeof(
TOOLBAR\_INFO )로 설정합니다.

_hwndRebar_

EE\_TOOLBAR\_OPEN 메시지 핸들러 내부에 도구 모음을 생성할 때, EmEditor는 rebar(크기 조정 막대) 창에 대한
핸들을 저장합니다.

_hwndClient_

클라이언트 도구 모음 창에 대한 핸들을 지정합니다.

_pszTitle_

도구 모음을 위한 제목 문자열을 지정합니다.

_nMask_

다음의 값들의 결합을 지정합니다.

|     |     |
| --- | --- |
| TIM\_REBAR | hwndRebar 매개 변수가 유효합니다. |
| TIM\_CLIENT | hwndClient 매개 변수가 유효합니다. |
| TIM\_TITLE | pszTitle 매개 변수가 유효합니다. |
| TIM\_ID | nID 매개 변수가 유효합니다. |
| TIM\_FLAGS | nFlags 매개 변수가 유효합니다. |
| TIM\_STYLE | fStyle 매개 변수가 유효합니다. |
| TIM\_MINCHILD | cxMinChild와 cyMinChild 매개 변수가 유효합니다. |
| TIM\_CX | cx 매개 변수가 유효합니다. |
| TIM\_CXIDEAL | cxIdeal 매개 변수가 유효합니다. |
| TIM\_BAND | nBand 매개 변수가 유효합니다. |
| TIM\_PLUG\_IN\_CMD\_ID | wPlugInCmdID 매개 변수가 유효합니다. |

_nID_

도구 모음에 대한 ID를 지정합니다.

_nFlags_

도구 모음이 닫히게 된 원인.

|     |     |
| --- | --- |
| 0 | 도구 모음이 사용자에 의해 닫혔습니다. |
| CLOSED\_FRAME\_WINDOW | 프레임 창이 닫혔습니다. |

_fStyle_

밴드 스타일을 지정하는 flags 입니다. 도구 모음을 숨기는 RBBS\_HIDDEN을 포함합니다. 이 매개 변수는
REBARBANDINFO 구조의 fStyle 매개 변수와 동일합니다.

_cxMinChild_

픽셀로 나타내는 자식 창의 최소 너비입니다. 이 매개 변수는 REBARBANDINFO 구조의 cxMinChild 매개 변수와
동일합니다.

_cyMinChild_

픽셀로 나타내는 자식 창의 최소 높이입니다. 이 매개 변수는 REBARBANDINFO 구조의 cyMinChild 매개 변수와
동일합니다.

_cx_

픽셀로 나타내는 밴드의 길이입니다. 이 매개 변수는 REBARBANDINFO 구조의 cx 매개 변수와 동일합니다.

_cxIdeal_

픽셀로 나타내는 밴드의 적합한 너비입니다. 이 매개 변수는 REBARBANDINFO 구조의 cxIdeal 매개 변수와 동일합니다.

_nBand_

밴드가 삽입될 위치의 0으로 시작하는 인덱스입니다. 이 매개 변수를 -1로 설정하는 경우, rebar(크기 조정 막대) 컨트롤은 마지막
위치에 새로운 밴드를 추가합니다.

_wPlugInCmdID_

플러그 인의 command ID입니다.

## 버전

EmEditor 버전 7 이상에서만 지원됩니다.

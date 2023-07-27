# 이벤트

|     |     |
| --- | --- |
|이벤트 |설명 |
| EVENT\_CARET\_MOVED | 커서 위치가 이동되었습니다. |
| EVENT\_CHANGE | 텍스트가 변경되었습니다. |
| EVENT\_CHAR | 문자가 삽입되었습니다. LOWORD (lParam)가 삽입된 유니코드 문자 코드를 나타냅니다. |
| EVENT\_CLOSE | EmEditor를 닫거나 플러그 인이 해제되기 직전에 호출됩니다.<br> 플러그 인은 리소스를 내보이고 DLL 파일이 삭제 가능하도록 해야합니다.<br> [OnEvents 기능](../exports/index) 의 첫번째 매개 변수 hwnd는 NULL입니다.<br> 이 이벤트는 플러그 인이 실제로 해제될 것을 이미하지는 않습니다. |
| EVENT\_CLOSE\_FRAME | EmEditor 프레임 창이 닫혔을 때 호출됩니다. (EmEditor 버전 5 이상에서만 지원됩니다.) |
| EVENT\_CONFIG\_CHANGED | 현재 구성 속성이 변경되었습니다. |
| EVENT\_CREATE | EmEditor가 시작되었거나 플러그 인이 로드된 후 즉시 호출됩니다.<br> LOWORD(lParam)가 플러그 인의 command ID를 나타냅니다. |
| EVENT\_CREATE\_FRAME | 새로운 EmEditor 프레임 창이 생성되면 호출됩니다.<br> 이 이벤트는 탭이 활성화되거나 비활성화 될 때에도 호출됩니다.<br> LOWORD(lParam)가 플러그 인의 command ID를 나타냅니다. (EmEditor 버전 5 이상에서만 지원됩니다.) |
| EVENT\_CUSTOM\_BAR\_CLOSED | 사용자 지정 표시줄이 닫혔을 때 호출됩니다.<br> EmEditor는 사용자 지정 표시줄이 닫혔을 때 클라이언트 창에 대해 DestroyWindow()를 호출합니다.<br> lParam은 [CUSTOM\_BAR\_CLOSED\_INFO 구조](../structure/custom_bar_close_info) 에 포인터를 나타냅니다.<br> (EmEditor 버전 6 이상에서만 지원됩니다.) |
| EVENT\_CUSTOM\_BAR\_CLOSING | 사용자 지정 표시줄이 닫혔을 때 호출됩니다.<br> lParam은 [CUSTOM\_BAR\_CLOSED\_INFO 구조](../structure/custom_bar_close_info) 에 포인터를 나타냅니다.<br> (EmEditor 버전 6 이상에서만 지원됩니다.) |
| EVENT\_DOC\_CLOSE | 문서가 닫히려고 할 때 호출됩니다. lParam은 문서를 닫기 위해 핸들(HEEDOC)을 나타냅니다.<br> (EmEditor 버전 5 이상에서만 지원됩니다.) |
| EVENT\_DOC\_SEL\_CHANGED | 활성 문서가 변경될 때 호출됩니다. (EmEditor 버전 5 이상에서만 지원됩니다.) |
| EVENT\_DROPPED | EmEditor 프레임 창에 파일을 끌어다 놓습니다. |
| EVENT\_FILE\_OPENED | 파일이 열려져 있습니다. |
| EVENT\_HISTORY | 텍스트가 변경될 때마다 호출됩니다.<br> lParam은 HISTORY\_INFO구조에 포인터를 나타냅니다. |
| EVENT\_IDLE | 대기 상태일 때 호출됩니다. (EmEditor 버전 6 이상에서만 지원됩니다.) |
| EVENT\_KILL\_FOCUS | 포커스를 놓쳤습니다. |
| EVENT\_LANGUAGE | UI 언어가 변경되었습니다. |
| EVENT\_MODIFIED | 수정된 상태가 변경되었습니다. |
| EVENT\_SAVING | 문서가 저장되려고 합니다. lParam은 저장되고 있는 문서에 핸들(HEEDOC)을 나타냅니다. |
| EVENT\_SCROLL | 스크롤 바 위치가 변경되었습니다. |
| EVENT\_SEL\_CHANGED | 텍스트의 선택 영역이 변경되었습니다. |
| EVENT\_SET\_FOCUS | 포커스가 설정되었습니다. |
| EVENT\_TAB\_MOVED | 탭이 이동되었을 때 호출됩니다. |
| EVENT\_TEMP\_SAVING | 사용자가 임시 문서를 저장하려고 할 때 호출됩니다.<br> 플러그 인은 파일 저장에 대한 책임이 있습니다.<br> lParam은 [TEMP\_INFO 구조](../structure/temp_info) 에 포인터를 나타냅니다. |
| EVENT\_TOOLBAR\_CLOSED | 사용자 지정 도구 모음이 닫혔을 때 호출됩니다.<br> EVENT\_CUSTOM\_BAR\_CLOSED 메시지와 다르게, EmEditor는 클라이언트 창을 소멸하지 않습니다.<br> lParam은 [TOOLBAR\_INFO 구조](../structure/toolbar_info) 에 포인터를 나타냅니다.<br> (EmEditor 버전 7 이상에서만 지원됩니다.) |
| EVENT\_TOOLBAR\_SHOW | 사용자 지정 도구 모음을 숨기거나 나타날 때 호출됩니다 (RBBS\_HIDDEN 스타일이 설정/해제될 때).<br> lParam은 [TOOLBAR\_INFO 구조](../structure/toolbar_info) 에 포인터를 나타냅니다.<br> (EmEditor 버전 7 이상에서만 지원됩니다.) |
| EVENT\_UI\_CHANGED | UI가 변경될 때 호출됩니다.<br> lParam은 다음 flag들의 결합을 나타냅니다:<br> UI\_CHANGED\_LANGUAGE 와 UI\_CHANGED\_TOOLBARS. |

이러한 이벤트들은 [OnEvents](../exports/index) 기능에 의해
nEvents 매개 변수로 사용됩니다.

이러한 상수는 [헤더 파일 (plugin.h)](https://download.emeditor.info/include/plugin.h) 에서 정의되었습니다.


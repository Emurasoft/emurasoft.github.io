# 내보내기 기능

|     |     |
| --- | --- |
| **함수** | **설명** |
| OnCommand( HWND hwnd ) | 메뉴 또는 도구 모음으로부터 플러그 인이 선택되었습니다. |
| QueryStatus( HWND hwnd, LPBOOL pbChecked ) | 명령이 활성화되었는지 여부와 플러그 인이 체크된 상태 인지<br> 여부에 대한 플러그 인의 상태를 조회합니다. |
| OnEvents( HWND hwnd, UINT nEvent, LPARAM lParam ) | 상태가 변경되면, 이 기능은 [Events](../event/index) 매개 변수로<br> 불려집니다. |
| GetMenuTextID() | 플러그 인 메뉴 항목 텍스트에 대한 resource ID를 검색합니다. |
| GetStatusMessageID() | \\n인 도구 모음 툴팁 텍스트와 결합된 상태 모음 텍스트에 대한 resource ID를 검색합니다. |
| GetBitmapID() | 도구 모음에 표시된 플러그 인에 대한 비트 맵 resource ID를 가져옵니다. |
| PlugInProc( HWND hwnd, UINT nMsg, WPARAM wParam, LPARAM lParam ) | 설정을 검색하거나 지정하기위해 [플러그 인 메시지](../plugin_message/index) 를 사용합니다. |

이러한 내보내기 기능은 명령에 의해 DEF 파일에 지정되어야 합니다.
컴파일 할 때 호출 방법으로 \_stdcall을 선택해야 합니다.


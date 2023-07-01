# Functions to Export

|     |     |
| --- | --- |
| OnCommand( HWND hwnd ) | The plug-in has been selected from a menu or a toolbar. |
| QueryStatus( HWND hwnd, LPBOOL pbChecked ) | Queries the status of the plug-in, whether the command is enabled and <br> whether the plug-in is a checked status. |
| OnEvents( HWND hwnd, UINT nEvent, LPARAM lParam ) | When a status is changed, this function is called with the<br> [Events](../event/index) parameter. |
| GetMenuTextID() | Retrieves a resource ID for the plug-in menu item text. |
| GetStatusMessageID() | Retrieves a resource ID for the status bar text combined with the tool <br> bar tool tip text with \\n. |
| GetBitmapID() | Obtains a bitmap resource ID for the plug-in displayed on a toolbar. |
| PlugInProc( HWND hwnd, UINT nMsg, WPARAM wParam, LPARAM lParam ) | Uses [Messages to Plug-ins](../plugin_message/index) to retrieve or set settings. |

These export functions must be defined in a DEF File by this order. When you
compile them, you need to select \_stdcall as a calling method. For details see plug-in samples in the EmEditor website library.


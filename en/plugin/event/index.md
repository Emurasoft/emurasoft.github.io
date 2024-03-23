# Events

|     |     |
| --- | --- |
| EVENT\_CARET\_MOVED | The cursor position has been moved. |
| EVENT\_CHANGE | The text has been altered. |
| EVENT\_CHAR | A character has been inserted. The LOWORD (lParam) represents the inserted Unicode character code. |
| EVENT\_CLOSE | Called immediately before closing EmEditor or the plug-in may be freed. A plug-in should release the resource and make the DLL file available to be removed. The first parameter hwnd of the [OnEvents function](../exports/index) will be NULL. This event does not mean that the plug-in will actually be freed. |
| EVENT\_CLOSE\_FRAME | Called when an EmEditor frame window is being closed. (Supported in EmEditor Version 5.00 or later) |
| EVENT\_CONFIG\_CHANGED | The property of the current configuration has been changed. |
| EVENT\_CREATE | Called immediately after starting EmEditor or the plug-in has been loaded. LOWORD(lParam) represents the command ID of the plug-in itself. |
| EVENT\_CREATE\_FRAME | Called when a new EmEditor frame window is created. This event is also called when the tab is enabled or disabled. LOWORD(lParam) represents the command ID of the plug-in itself. (Supported in EmEditor Version 5.00 or later) |
| EVENT\_CUSTOM\_BAR\_CLOSED | Called when a custom bar has been closed. EmEditor calls DestroyWindow() against the client window when the custom bar is closed. lParam represents a pointer to the [CUSTOM\_BAR\_CLOSED\_INFO structure](../structure/custom_bar_close_info). (Supported in EmEditor Version 6.00 or later) |
| EVENT\_CUSTOM\_BAR\_CLOSING | Called when a custom bar is being closed. lParam represents a pointer to the [CUSTOM\_BAR\_CLOSED\_INFO structure](../structure/custom_bar_close_info). (Supported in EmEditor Version 6.00 or later) |
| EVENT\_DOC\_CLOSE | Called when a document is about to close. lParam represents a handle (HEEDOC) to the closing document. (Supported in EmEditor Version 5.00 or later) |
| EVENT\_DOC\_SEL\_CHANGED | Called when an active document is changed. (Supported in EmEditor Version 5.00 or later) |
| EVENT\_DROPPED | A file has been dropped onto the EmEditor frame window. |
| EVENT\_FILE\_OPENED | A file has been opened. |
| EVENT\_HISTORY | Called each time when the text has been altered. lParam represents a pointer to the HISTORY\_INFO structure. |
| EVENT\_IDLE | Called when idle. (Supported in EmEditor Version 6.00 or later) |
| EVENT\_KILL\_FOCUS | The focus has been lost. |
| EVENT\_LANGUAGE | The UI language has been changed. |
| EVENT\_MODIFIED | The modified status has been changed. |
| EVENT\_SAVING | The document is about to be saved. lParam represents a handle (HEEDOC) to the document being saved. (Supported in EmEditor Version 8.00 or later) |
| EVENT\_SCROLL | A scroll bar position has been changed. |
| EVENT\_SEL\_CHANGED | The selection of the text has been changed. |
| EVENT\_SET\_FOCUS | The focus has been set. |
| EVENT\_TAB\_MOVED | Called when a tab has been moved. |
| EVENT\_TEMP\_SAVING | Called when a user is about to save a temporary document. The plug-in is responsible for saving the file. lParam represents a pointer to the [TEMP\_INFO structure](../structure/temp_info). |
| EVENT\_TOOLBAR\_CLOSED | Called when a custom toolbar has been closed. Unlike the EVENT\_CUSTOM\_BAR\_CLOSED message, EmEditor does not destroy the client window. lParam represents a pointer to the [TOOLBAR\_INFO structure](../structure/toolbar_info). (Supported in EmEditor Version 7.00 or later) |
| EVENT\_TOOLBAR\_SHOW | Called when a custom toolbar has been hidden or displayed (when the RBBS\_HIDDEN style is toggled). lParam represents a pointer to the [TOOLBAR\_INFO structure](../structure/toolbar_info). (Supported in EmEditor Version 7.00 or later) |
| EVENT\_UI\_CHANGED | Called when the UI changed. lParam represents a combination of the following flags: UI\_CHANGED\_LANGUAGE and UI\_CHANGED\_TOOLBARS. |

These events are used as the nEvents parameter by the
[OnEvents](../exports/index) function.

These constants are defined at the
header file (plugin.h).


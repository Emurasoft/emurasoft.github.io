# EP\_PRE\_TRANSLATE\_MSG

Called before each Windows message is translated.

EP\_PRE\_TRANSLATE\_MSG

hwnd = hwndView;

wParam = 0;

lParam = (LPARAM) (MSG\*) pMsg;

## Parameters

_hwndView_

The window handle to the EmEditor view.

_pMsg_

The pointer to the window message before translated.

## Return Values

If the return value is TRUE, the message is not be continued to be translated or dispatched. If the return value is FALSE, the message is continued to be translated or dispatched.

## Version

Supported on Version 6.00 or later.

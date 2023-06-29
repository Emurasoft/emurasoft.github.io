# Editor\_ToolbarClose

Closes a custom toolbar. You can use this inline function or explicitly send
the [EE\_TOOLBAR\_CLOSE](../message/ee_toolbar_close)
message.

Editor\_ToolbarClose( HWND hwnd, UINT nCustomRebarID );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nToolbarID_

> Specifies the toolbar to close. This is the return value from the EE\_TOOLBAR\_OPEN message.

## Return Values

> If the message succeeds and the toolbar state has been changed, the return value is TRUE. If the message fails or the toolbar state has not been changed, the return value is FALSE.

## Version

> Supported on EmEditor Professional Version 7.00 or later.
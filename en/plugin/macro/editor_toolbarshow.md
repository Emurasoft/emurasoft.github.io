# Editor\_ToolbarShow

Shows or hides a custom toolbar. You can use this inline function or explicitly send
the [EE\_TOOLBAR\_SHOW](../message/ee_toolbar_show)
message.

Editor\_ToolbarShow( HWND hwnd, UINT nCustomRebarID, BOOL bVisible );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nToolbarID_

Specifies the toolbar to close. This is the return value from the EE\_TOOLBAR\_OPEN message.

_bVisible_

Specifies TRUE if the toolbar should be visible, or FALSE if the toolbar should be hidden.

## Return Values

If the message succeeds and the toolbar state has been changed, the return value is TRUE. If the message fails or the toolbar state has not been changed, the return value is FALSE.

## Version

Supported on EmEditor Professional Version 7.00 or later.

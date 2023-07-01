# EE\_TOOLBAR\_SHOW

Shows or hides a custom toolbar. You can send this message explicitly or
by using the [Editor\_ToolbarShow](../macro/editor_toolbarshow) inline function.

EE\_TOOLBAR\_SHOW

(UINT)wParam = nToolbarID

(BOOL)lParam = bVisible

## Parameters

_nToolbarID_

> Specifies the toolbar to close. This is the return value from the EE\_TOOLBAR\_OPEN message.

_bVisible_

> Specifies TRUE if the toolbar should be visible, or FALSE if the toolbar should be hidden.

## Return Values

> If the message succeeds and the toolbar state has been changed, the return value is TRUE. If the message fails or the toolbar state has not been changed, the return value is FALSE.

## Version

> Supported on EmEditor Professional Version 7.00 or later.

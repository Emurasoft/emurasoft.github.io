# Editor\_ToolbarOpen

Opens a custom toolbar. You can use this inline function or explicitly send
the [EE\_TOOLBAR\_OPEN](../message/ee_toolbar_open)
message.

Editor\_ToolbarOpen( HWND hwnd, TOOLBAR\_INFO\* pToolbarInfo );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pToolbarInfo_

Pointer to the TOOLBAR\_INFO structure.

## Return Values

The return value is a custom toolbar ID. If the message fails, the return value is zero.

## Version

Supported on EmEditor Professional Version 7.00 or later.

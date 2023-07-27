# Editor\_CustomBarClose

Closes a custom bar. You can use this inline function or explicitly send the [EE\_CUSTOM\_BAR\_CLOSE](../message/ee_custom_bar_close) message.

Editor\_CustomBarClose( HWND hwnd, UINT nCustomBarID );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nCustomBarID_

Specifies the custom bar to close. This is the return value from the Editor\_CustomBarOpen inline function.

## Return Values

If the message succeeds, the return value is TRUE. If the message fails, the return value is FALSE.

## Version

Supported on EmEditor Professional Version 6.00 or later.

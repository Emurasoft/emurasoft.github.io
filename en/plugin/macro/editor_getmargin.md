# Editor\_GetMargin

Retrieves the margin size. You can use this inline function or explicitly send
the [EE\_GET\_MARGIN](../message/ee_get_margin)
message.

Editor\_Convert( HWND hwnd );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

## Return Values

Returns the currently selected margin size. If the normal line margin size
and the quoted line margin size are different, the larger margin will be
returned. If lines are wrapped by the window size, the return value will
depend on the current window size.

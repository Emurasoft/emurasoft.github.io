# Editor\_RotateClip

Rotates the current position in the Clipboard history. You can use this inline function or explicitly send the [EE\_CLIP\_HISTORY](../message/ee_clip_history)
message.

Editor\_RotateClip( HWND hwnd, int iDirection );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iDirection_

> Specifies the direction you want to rotate the current position in the Clipboard history.

## Return Values

> The return value is 1 is succeeded. If the message fails, the return value is -1.

## Version

> Supported on EmEditor Version 9.00 or later.
# Editor\_SetClipPos

Sets the current position in the Clipboard history. You can use this inline function or explicitly send the [EE\_CLIP\_HISTORY](../message/ee_clip_history)
message.

Editor\_SetClipPos( HWND hwnd, int iPos );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_iPos_

Specifies the new position in the Clipboard history.

## Return Values

Retrieves the current position in the Clipboard history. If the message fails, the return value is -1.

## Version

Supported on EmEditor Version 9.00 or later.

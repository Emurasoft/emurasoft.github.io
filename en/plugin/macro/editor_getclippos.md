# Editor\_GetClipPos

Retrieves the current position in the Clipboard history. You can use this inline function or explicitly send the [EE\_CLIP\_HISTORY](../message/ee_clip_history)
message.

Editor\_GetClipPos( HWND hwnd );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

## Return Values

> Retrieves the current position in the Clipboard history. If the message fails, the return value is -1.

## Version

> Supported on EmEditor Version 9.00 or later.
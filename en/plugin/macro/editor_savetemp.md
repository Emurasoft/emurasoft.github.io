# Editor\_SaveTemp

Saves the temporary text. You can use this inline function or explicitly send the [EE\_EDIT\_TEMP](../message/ee_edit_temp)
message.

Editor\_SaveTemp( HWND hwnd, UINT nEditID );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nEditID_

> Specifies the ID of the temporary text that you want to save.

## Return Values

> The return value is the ID of the new document.

## Version

> Supported on EmEditor Version 9.00 or later.

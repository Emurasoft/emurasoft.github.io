# Editor\_ActivateTemp

Opens existing temporary text as a new document. You can use this inline function or explicitly send the [EE\_EDIT\_TEMP](../message/ee_edit_temp)
message.

Editor\_ActivateTemp( HWND hwnd, UINT nEditID, POINT\_PTR\* pptInitialCaret = NULL );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nEditID_

> Specifies the ID of the temporary text that you want to activate.

_pptInitialCaret_

> Specifies the initial cursor position.

## Return Values

> The return value is the ID of the new document.

## Version

> Supported on EmEditor Version 9.00 or later.

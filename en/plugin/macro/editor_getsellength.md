# Editor_GetSelLength

Retrieves the length of the selected text. You can use this inline function or explicitly send the [EE_GET_SEL_LENGTH](../message/ee_get_sel_length) message.

nLen = Editor_GetSelLength( HWND hwnd );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

## Return Values

The return value is the length of the selected text. If the length is larger than LONG_MAX, the return value becomes LONG_MAX.

## Version

Supported in EmEditor Professional Version 26.1 or later.

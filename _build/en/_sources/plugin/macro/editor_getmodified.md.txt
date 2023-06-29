# Editor\_GetModified

Retrieves the modified state of the text. You can use this inline function or explicitly send the [EE\_GET\_MODIFIED](../message/ee_get_modified) message.

Editor\_GetModified( HWND hwnd );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

## Return Values

> If the text is modified, the return value is TRUE. If the text is not
> modified, the return value is FALSE.
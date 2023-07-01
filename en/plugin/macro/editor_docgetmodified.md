# Editor\_DocGetModified

Retrieves the modified state of the text of the specified document. You can use this inline function or explicitly send the [EE\_GET\_MODIFIED](../message/ee_get_modified) message.

Editor\_DocGetModified( HWND hwnd, int iDoc );

Editor\_DocGetModified( HWND hwnd, HEEDOC hDoc );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iDoc_

> Specifies the index of the target document. If -1 is specified, the currently active document will be targeted.

_hDoc_

> Specifies the handle to the target document. If NULL is specified, the currently active document will be targeted.

## Return Values

> If the text is modified, the return value is TRUE. If the text is not
> modified, the return value is FALSE.

## Version

> Supported on EmEditor Professional Version 5.00 or later.

# Editor\_SetModified

Changes the modified state of the text. You can use this inline function
or explicitly send the [EE\_SET\_MODIFIED](../message/ee_set_modified) message.

Editor\_SetModified( HWND hwnd, BOOL bModified );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_bModified_

> TRUE to change the state as modified, or FALSE to change the state as
> unmodified.

## Return Values

> The return value is not used.
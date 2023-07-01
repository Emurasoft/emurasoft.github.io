# Editor\_SetSelLength

Changes the character length of the selection. You can use this inline function or explicitly send the
[EE\_SET\_SEL\_LENGTH](../message/ee_set_sel_length)
message.

Editor\_SetSelLength( HWND hwnd, UINT nLen );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nLen_

> Specifies the character length of the selection. Returns are always two
> character length (CR+LF).

## Return Values

> The return value is not used.

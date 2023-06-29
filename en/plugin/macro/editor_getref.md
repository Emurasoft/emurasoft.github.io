# Editor\_GetRef

Retrieves the reference number of a specified plug-in. You can send this inline function or explicitly send the [EE\_GET\_REF](../message/ee_get_ref) message.

Editor\_GetRef( HWND hwnd, ATOM atom );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_atom_

> Specifies the atom of an specified plug-in file name.

## Return Values

> The return value is the reference number of a specified plug-in. If the
> return value is zero, the specified plug-in can be safely unloaded from
> EmEditor.
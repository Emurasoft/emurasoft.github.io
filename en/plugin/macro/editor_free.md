# Editor\_Free

Frees a specified plug-in. You can use this inline function or explicitly send
the [EE\_FREE](../message/ee_free) message.

Editor\_Free( HWND hwnd, ATOM atom );

## Parameters

_hwnd_

Specifies the character code by Unicode to be queried.

_atom_

Specifies the atom of an specified plug-in file name.

## Return Values

> If the plug-in is freed, the return value is TRUE. If the plug-in is not
> freed, the return value is FALSE.
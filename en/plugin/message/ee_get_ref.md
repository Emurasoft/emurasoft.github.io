# EE\_GET\_REF

Retrieves the reference number of a specified plug-in. You can send this
message explicitly or use the
[Editor\_GetRef](../macro/editor_getref) inline function.

EE\_GET\_REF

wParam = 0;

lParam = (LPARAM)(ATOM)atom;

## Parameters

_atom_

Specifies the atom of a specified plug-in file name.

## Return Values

The return value is the reference number of a specified plug-in. If the
return value is zero, the specified plug-in can be safely unloaded from
EmEditor.

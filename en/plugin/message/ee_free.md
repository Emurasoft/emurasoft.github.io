# EE\_FREE

Frees a specified plug-in. You can send this message explicitly or by using
the [Editor\_Free](../macro/editor_free) inline function.

```
EE_FREE
wParam = 0;
lParam = (LPARAM)(ATOM)atom;
```

## Parameters

_atom_

Specifies the atom of a specified plug-in file name.

## Return Values

If the plug-in is freed, the return value is TRUE. If the plug-in is not
freed, the return value is FALSE.

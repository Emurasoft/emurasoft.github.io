# EE\_SET\_OUTLINE\_LEVEL

Sets the outline level for the specified logical line. You can send this message
explicitly or use the [Editor\_SetOutlineLevel](../macro/editor_setoutlinelevel) inline function.

```
EE_SET_OUTLINE_LEVEL
wParam = (WPARAM) (INT_PTR) nLogicalLine;
lParam = (LPARAM) (int) nLevel;
```

## Parameters

_nLogicalLine_

Specifies a logical line.

_nLevel_

Specifies an outline level.

## Return Values

The return value is the old outline level for the specified logical line.
If an error occurs, the return value will be -1.

## Version

Supported on EmEditor Professional Version 6.00 or later.

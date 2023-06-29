# EE\_GET\_OUTLINE\_LEVEL

Retrieves the outline level for the specified logical line. You can send this message
explicitly or use the [Editor\_GetOutlineLevel](../macro/editor_getoutlinelevel) inline function.

EE\_GET\_OUTLINE\_LEVEL

wParam = (WPARAM) (INT\_PTR) nLogicalLine;

lParam = 0;

## Parameters

_nLogicalLine_

> Specifies a logical line.

## Return Values

> The return value is the outline level for the specified logical line. If an
> error occurs, the return value will be -1.

## Version

> Supported on EmEditor Professional Version 6.00 or later.
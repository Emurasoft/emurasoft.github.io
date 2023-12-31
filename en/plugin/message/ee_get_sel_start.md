# EE\_GET\_SEL\_START

Retrieves the starting character position of the selection. You can send this
message explicitly or use the
[Editor\_GetSelStart](../macro/editor_getselstart)
inline function.

```
EE_GET_SEL_START
wParam = (WPARAM) (int) nLogical;
lParam = (LPARAM) (POINT_PTR*) pptPos;
```

## Parameters

_nLogical_

Specifies one of the following values.

| Value | Meaning |
| --- | --- |
| POS\_VIEW | Display Coordinates |
| POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
| POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |

_pptPos_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that will receive the starting character
position of the selection.

## Return Values

The return value is not used.

# EE\_GET\_LINES

Retrieves the number of the lines for the specified document. You can send this message
explicitly or use the [Editor\_DocGetLines](../macro/editor_docgetlines) inline function or the [Editor\_GetLines](../macro/editor_getlines) inline function.

```
EE_GET_LINES
wParam = (WPARAM) MAKEWPARAM(nLogical, iDoc+1);
lParam = hDoc;
```

## Parameters

_nLogical_

Specifies one of the following Values.

| Value | Meaning |
| --- | --- |
| POS\_VIEW | Display Coordinates |
| POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
| POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |

_iDoc_

Specifies the index of the target document. A one-based index should be specified at the higher word of wParam. If 0 is specified at the higher word of wParam, the currently active document will
be targeted.

_hDoc_

Optionally, specifies the handle to the target document. iDoc must be zero if you specify this parameter.

## Return Values

Returns the number of the lines in EmEditor. If the last line is ended with
a return, the last line will be counted. If the text is empty, returns one.

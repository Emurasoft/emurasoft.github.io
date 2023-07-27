# EE\_SET\_SEL\_LENGTH

Changes the character length of the selection. You can send this message
explicitly or use the
[Editor\_SetSelLength](../macro/editor_setsellength)
inline function.

EE\_SET\_SEL\_LENGTH

wParam = (WPARAM) (UINT) nLen;

lParam = 0;

## Parameters

_nLen_

Specifies the character length of the selection. Returns are always two
character length (CR+LF).

## Return Values

The return value is not used.

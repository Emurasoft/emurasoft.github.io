# EE\_SET\_MODIFIED

Changes the modified state of the text. You can send this message explicitly
or by using the [Editor\_SetModified](../macro/editor_setmodified) inline function.

EE\_SET\_MODIFIED

wParam = (WPARAM) (BOOL) bModified;

lParam = 0;

## Parameters

_bModified_

TRUE to change the state as modified, or FALSE to change the state as
unmodified.

## Return Values

The return value is not used.

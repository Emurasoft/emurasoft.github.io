# EE\_GET\_MODIFIED

Retrieves the modified state of the text. You can send this message
explicitly or use the [Editor\_GetModified](../macro/editor_getmodified) inline function or [Editor\_DocGetModified](../macro/editor_docgetmodified) inline function..

EE\_GET\_MODIFIED

wParam = (WPARAM) MAKEWPARAM(0, iDoc+1);

lParam = hDoc;

## Parameters

_iDoc_

> Specifies the index of the target document. A one-based index should be specified at the higher word of wParam. If 0 is specified at the higher word of wParam, the currently active document will
> be targeted.

_hDoc_

> Optionally, specifies the handle to the target document. iDoc must be zero if you specify this parameter.

## Return Values

> If the text is modified, the return value is TRUE. If the text is not
> modified, the return value is FALSE.

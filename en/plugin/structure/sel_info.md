# SEL\_INFO

Used by
[Editor\_GetMultiSel](../macro/editor_getmultisel)
inline function ( [EE\_GET\_MULTI\_SEL](../../plugin/message/ee_get_multi_sel) message).

typedef struct \_SEL\_INFO {

size\_t cbSize;

POINT\_PTR ptStart;

POINT\_PTR ptEnd;

POINT\_PTR ptCaret;

} SET\_INFO;

## Fields

_cbSize_

> Must specify sizeof( SEL\_INFO ).

_ptStart_

> Specifies the starting position of the selection.

_ptEnd_

> Specifies the ending position of the selection.

_ptCaret_

> Specifies the cursor position of the selection.

## Version

> Supported on Version 13 or later.

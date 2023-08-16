# SEL\_INFO

Used by
[Editor\_GetMultiSel](../macro/editor_getmultisel)
inline function ( [EE\_GET\_MULTI\_SEL](../../plugin/message/ee_get_multi_sel) message).

```
typedef struct _SEL_INFO {
	size_t cbSize;
	POINT_PTR ptStart;
	POINT_PTR ptEnd;
	POINT_PTR ptCaret;
} SET_INFO;
```

## Fields

_cbSize_

Must specify sizeof( SEL\_INFO ).

_ptStart_

Specifies the starting position of the selection.

_ptEnd_

Specifies the ending position of the selection.

_ptCaret_

Specifies the cursor position of the selection.

## Version

Supported on Version 13 or later.

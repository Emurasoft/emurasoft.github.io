# HISTORY\_INFO

Used by [EVENT\_HISTORY event](../event/index).

```
typedef struct _HISTORY_INFO {
	size_t cbSize;
	UINT nFlags;
	POINT_PTR ptTop;
	POINT_PTR ptBottom;
	UINT nChar;
	LPCWSTR pszString;
} HISTORY_INFO;
```

## Members

_cbSize_

Size of this data structure, in bytes. This member should be sizeof( HISTORY\_INFO ) before receiving the EVENT\_HISTORY event.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| HISTORY\_INSERT\_CHAR | A character was inserted. |
| HISTORY\_BACK\_SPACE | The back space key was pressed to remove a character. |
| HISTORY\_DELETE\_CHAR | The Delete key was pressed to remove a character. |
| HISTORY\_INSERT\_STRING | A string was inserted. |
| HISTORY\_DELETE\_STRING | A string was deleted. |
| HISTORY\_INSERT\_TAB\_SEL | The Tab key was pressed to indent the selection. |
| HISTORY\_MODIFIED | The document was modified. |
| HISTORY\_COMBINED | This history event should be combined with earlier event(s). |
| HISTORY\_CR\_ONLY | The removed character was CR only. |
| HISTORY\_LF\_ONLY | The removed character was LF only. |
| HISTORY\_SEL\_BOX | The inserted string was a vertical selection. |
| HISTORY\_INSIDE\_UNDO | The operation was inside the Undo command. |
| HISTORY\_INSIDE\_REDO | The operation was inside the Redo command. |

_ptTop_

This member contains the previous cursor position. If the nFlags member contains HISTORY\_INSERT\_STRING, this member is the starting position of the selection.

_ptBottom_

If the nFlags member contains HISTORY\_INSERT\_STRING, this member is the ending position of the selection. Otherwise, this member is ignored.

_nChar_

If the nFlags member contains HISTORY\_BACK\_SPACE or HISTORY\_DELETE\_CHAR, this member contains the character removed.

_pszString_

If the nFlags member contains HISTORY\_DELETE\_STRING, this member contains the string removed.

## Version

Supported on Version 9.00 or later.

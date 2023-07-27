# SetActivePoint Method (Selection Object)

Sets the cursor position.

## 

### \[JavaScript\]

```
document.selection.SetActivePoint( nFlags, xPos, yPos [ [, bExtend ] , iSel ] );
```

### \[VBScript\]

```
document.selection.SetActivePoint nFlags, xPos, yPos [ [, bExtend ] , iSel ]
```

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eePosView | Specifies by the column position and the line number in view. |
| eePosLogical | Specifies by the number of characters and lines from the previous <br> newline characters (or the start of the document if the first line). |
| eePosLogicalA | Same as eePosLogical but counts a full-width character as 2. |
| eePosCellLogical | CSV cell unit in logical coordinates. |
| eePosCellView | CSV cell unit in view coordinates. |

_xPos_

Specifies the column number of the cursor position.

_yPos_

Specifies the line number of the cursor position.

_bExtend_

Optional. Determines whether to extend the current selection. If _bExtend_ is
true, then the active end of the selection moves to the location while the
anchor end remains where it is. Otherwise, both ends are moved to the
specified location.

_iSel_

Optional. Specifies the one-based index of the selection. If 0 is specified
or omitted, the normal selection is specified. If 1 or larger is specified, the _nFlags_ parameter must be eePosLogical.

## Version

Supported on EmEditor Professional Version 4.00 or later.

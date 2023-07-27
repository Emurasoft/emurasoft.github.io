# GetActivePointX Method (Selection Object)

Returns the column number of the cursor position.

## 

### \[JavaScript\]

```
xPos = document.selection.GetActivePointX( nFlags [, iSel ] );
```

### \[VBScript\]

```
xPos = document.selection.GetActivePointX( nFlags [, iSel ] )
```

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eePosView | Returns the column position. |
| eePosLogical | Returns the number of characters from the previous newline characters (or the <br> start of the document if the first line). |
| eePosLogicalA | Same as eePosLogical but counts a full-width character as 2. |
| eePosCell | CSV cell unit. |

_iSel_

Optional. Specifies the one-based index of the selection. If 0 is specified
or omitted, the normal selection is specified. If 1 or larger is specified, the _nFlags_ parameter must be eePosLogical.

## Version

Supported on EmEditor Professional Version 4.00 or later.

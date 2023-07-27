# GetAnchorPointX Method (Selection Object)

Returns the column number of the origin point of the selection.

## 

### \[JavaScript\]

```
xPos = document.selection.GetAnchorPointX( nFlags );
```

### \[VBScript\]

```
xPos = document.selection.GetAnchorPointX( nFlags )
```

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eePosView | Returns the column position. |
| eePosLogical | Returns the number of characters from the previous newline characters (or the <br> start of the document if the first line). |
| eePosLogicalA | Same as eePosLogical but counts a full-width character as 2. |
| eePosCell | CSV cell unit |

## Version

Supported on EmEditor Professional Version 4.03 or later.

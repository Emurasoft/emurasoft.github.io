# SetAnchorPoint Method (Selection Object)

Sets the origin point of the selection.

#### \[JavaScript\]

document.selection. **SetAnchorPoint**( _nFlags_, _xPos_, _yPos_
);

#### \[VBScript\]

document.selection. **SetAnchorPoint** _nFlags_, _xPos_, _yPos_

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

Specifies the column number of the origin point of the selection.

_yPos_

Specifies the line number of the origin point of the selection.

## Version

Supported on EmEditor Professional Version 4.03 or later.

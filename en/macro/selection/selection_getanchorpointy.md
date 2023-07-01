# GetAnchorPointY Method (Selection Object)

Returns the line number of the origin point of the selection.

#### \[JavaScript\]

yPos = document.selection. **GetAnchorPointY**( _nFlags_ );

#### \[VBScript\]

yPos = document.selection. **GetAnchorPointY**( _nFlags_ )

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eePosView | Returns the line number in view. |
| eePosLogical | Returns the logical line number, determined by the number of new <br> lines from the start of the document. |
| eePosCellLogical | CSV cell unit in logical coordinates. |
| eePosCellView | CSV cell unit in view coordinates. |

## Version

Supported on EmEditor Professional Version 4.03 or later.

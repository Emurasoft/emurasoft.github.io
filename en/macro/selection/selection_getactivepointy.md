# GetActivePointY Method (Selection Object)

Returns the line number of the cursor position.

## 

### \[JavaScript\]

```
yPos = document.selection.GetActivePointY( nFlags [, iSel ] );
```

### \[VBScript\]

```
yPos = document.selection.GetActivePointY( nFlags [, iSel ] )
```

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eePosView | Returns the line number in view. |
| eePosLogical | Returns the logical line number, determined by the number of new <br> lines from the start of the document. |
| eePosCellLogical | CSV cell unit in logical coordinates. |
| eePosCellView | CSV cell unit in view coordinates. |

_iSel_

Optional. Specifies the one-based index of the selection. If 0 is specified
or omitted, the normal selection is specified. If 1 or larger is specified, the _nFlags_ parameter must be eePosLogical.

## Version

Supported on EmEditor Professional Version 4.00 or later.

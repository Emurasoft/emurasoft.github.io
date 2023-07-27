# EndOfLine Method (Selection Object)

Moves the cursor to the end of the current line.

## 

### \[JavaScript\]

```
document.selection.EndOfLine( [ bExtend [, nFlags ] ] );
```

### \[VBScript\]

```
document.selection.EndOfLine [ bExtend [, nFlags ] ]
```

## Parameters

_bExtend_

Optional. Specifies whether the moved text is collapsed or not. The default
is false and the moved text is collapsed.

_nFlags_

Optional. Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeLineView | Specifies the view line. |
| eeLineLogical | Specifies the logical line. |

## Version

Supported on EmEditor Professional Version 4.00 or later.

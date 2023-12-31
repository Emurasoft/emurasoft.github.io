# StartOfLine Method (Selection Object)

Moves the cursor to the start of the line.

## 

### \[JavaScript\]

```
document.selection.StartOfLine( [ bExtend [, nFlags ] ]
);
```

### \[VBScript\]

```
document.selection.StartOfLine [ bExtend [, nFlags ] ]
```

## Parameters

_bExtend_

Optional. Specifies whether the moved text is collapsed or not. The default
is false and the moved text is collapsed.

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeLineView | Specifies display lines. |
| eeLineLogical | Specifies logical lines. |
| eeLineHomeText | Moves to the beginning of text except spaces. |

## Version

Supported on EmEditor Professional Version 4.00 or later.

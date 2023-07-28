# CharRight Method (Selection Object)

Moves the cursor the specified number of characters to the right.

## 

### \[JavaScript\]

```
document.selection.CharRight( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.CharRight [ bExtend [, nCount ] ]
```

## Parameters

_bExtend_

Optional. Specifies whether the moved text is collapsed or not. The default
is false and the moved text is collapsed.

_nCount_

Optional. Specifies the number of characters to move to the right. The
default is 1. If negative, the method acts like the [**CharLeft** \
Method](selection_charleft). If 0, the method acts like 1.

## Version

Supported on EmEditor Professional Version 4.00 or later.

# WordLeft Method (Selection Object)

Moves the cursor the specified number of words to the left.

## 

### \[JavaScript\]

```
document.selection.WordLeft( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.WordLeft [ bExtend [, nCount ] ]
```

## Parameters

_bExtend_

Optional. Specifies whether the moved text is collapsed or not. The default
is false and the moved text is collapsed.

_nCount_

Optional. Specifies the number of words to move to the left. The default is
1\. If negative, the method acts like the [**WordRight** Method](selection_wordright). If 0, the method acts like 1.

## Version

Supported on EmEditor Professional Version 4.00 or later.

# CharLeft Method

Moves the cursor the specified number of characters to the left.

#### \[JavaScript\]

document.selection. **CharLeft**( \[ _bExtend_ \[, _nCount_ \] \] );

#### \[VBScript\]

document.selection. **CharLeft** \[ _bExtend_ \[, _nCount_ \] \]

## Parameters

_bExtend_

Optional. Specifies whether the moved text is collapsed or not. The default
is false and the moved text is collapsed.

_nCount_

Optional. Specifies the number of characters to move to the left. The default
is 1. If negative, the method acts like the [**CharRight** \
Method](selection_charright). If 0, the method acts like 1.

## Version

Supported on EmEditor Professional Version 4.00 or later.
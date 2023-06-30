# LineDown Method (Selection Object)

Moves the cursor down a specified number of lines.

#### \[JavaScript\]

document.selection. **LineDown**( \[ _bExtend_ \[, _nCount_ \] \] );

#### \[VBScript\]

document.selection. **LineDown** \[ _bExtend_ \[, _nCount_ \] \]

## Parameters

_bExtend_

Optional. Specifies whether the moved text is collapsed or not. The default
is false and the moved text is collapsed.

_nCount_

Optional. Specifies the number of lines to move down. The default is 1. If
negative, the method acts like the [**LineUp** \
Method.](selection_lineup) If 0, the method acts like 1.

## Version

Supported on EmEditor Professional Version 4.00 or later.
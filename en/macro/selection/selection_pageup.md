# PageUp Method (Selection Object)

Moves the cursor the specified number of pages up in the document.

#### \[JavaScript\]

document.selection. **PageUp**( \[ _bExtend_ \[, _nCount_ \] \] );

#### \[VBScript\]

document.selection. **PageUp** \[ _bExtend_ \[, _nCount_ \] \]

## Parameters

_bExtend_

Optional. Specifies whether the moved text is collapsed or not. The default
is false and the moved text is collapsed.

_nCount_

Optional. Specifies the number of pages to move up. The default is 1. If
negative, the method acts like the [**PageDown** \
Method](selection_pagedown). If 0, the method acts like 1.

## Version

Supported on EmEditor Professional Version 4.00 or later.

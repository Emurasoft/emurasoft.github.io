# Delete Method (Selection Object)

Deletes the selected text. If the selection is empty, deletes the
specified number of characters to the right of the cursor.

#### \[JavaScript\]

document.selection. **Delete**( \[\[ _nCount_ \], _bComplete_ \] );

#### \[VBScript\]

document.selection. **Delete** \[\[ _nCount_ \], _bComplete_ \]

## Parameters

_nCount_

Optional. Specifies the number of characters to delete to the right of the cursor. The default is 1. If negative, the method acts like the [**DeleteLeft** Method](selection_deleteleft). If 0, the method acts like 1.

_bComplete_

Optional. Specifies whether to delete the selection completely in cell selection mode. If omitted, False is specified.

## Version

Supported on EmEditor Professional Version 4.00 or later.

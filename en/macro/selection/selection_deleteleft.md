# DeleteLeft Method (Selection Object)

Deletes the selected text. If the selection is empty, deletes the specified
number of characters to the left of the cursor.

## 

### \[JavaScript\]

```
document.selection.DeleteLeft( [ nCount ] );
```

### \[VBScript\]

```
document.selection.DeleteLeft [ nCount ]
```

## Parameters

_nCount_

Optional. Specifies the number of characters to delete to the left of the
cursor. The default is 1. If negative, the method acts like
the
[**Delete** \
Method.](selection_delete) If 0, the method acts like 1.

## Version

Supported on EmEditor Professional Version 4.00 or later.

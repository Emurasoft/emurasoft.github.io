# EE\_MANAGE\_DUPLICATES

Deletes or bookmarks duplicate lines. You can send this message explicitly or use
the [Editor\_ManageDuplicates](../macro/editor_manageduplicates) inline function.

```
EE_MANAGE_DUPLICATES
wParam = 0;
lParam = (LPARAM) (MANAGE_DUPLICATES_INFO*) pManageDuplicatesInfo;
```

## Parameters

_pManageDuplicatesInfo_

Pointer to the [MANAGE\_DUPLICATES\_INFO](../structure/manage_duplicates_info) structure.

## Return Value

Returns the HRESULT value. A zero or positive value means success while a negative value means failure.

## Version

Supported on EmEditor Professional Version 16.4 or later.

# EE\_SORT

Sorts the document. You can send this message explicitly or use
the [Editor\_Sort](../macro/editor_sort) inline function.

```
EE_SORT
wParam = 0;
lParam = (LPARAM) (SORT_INFO*) pSortInfo;
```

## Parameters

_pSortInfo_

Pointer to the [SORT\_INFO](../structure/sort_info) structure.

## Return Value

Returns the HRESULT value. A zero or positive value means success while a negative value means failure.

## Version

Supported on EmEditor Professional Version 16.4 or later.

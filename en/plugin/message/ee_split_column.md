# EE\_SPLIT\_COLUMN

Splits specified columns of the current CSV document. You can send this message explicitly or use the [Editor\_SplitColumn](../macro/editor_splitcolumn) inline function.

```
EE_SPLIT_COLUMN
wParam = (WPARAM)(SPLIT_COLUMN_INFO*)pInfo;
lParam = 0;
```

## Parameters

_pInfo_

Specifies the pointer to the [SPLIT\_COLUMN\_INFO](../structure/split_column_info) structure.

## Return Values

The return value is a negative value it it fails.

## Version

Supported on Version 19.9 or later.

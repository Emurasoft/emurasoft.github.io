# EE\_PIVOT\_TABLE

Creates a pivot table in the CSV document. You can send this message explicitly or use the [Editor\_PivotTable](../macro/editor_pivottable) inline function.

```
EE_PIVOT_TABLE
wParam = (WPARAM)(PIVOT_TABLE_INFO*)pInfo;
lParam = 0;
```

## Parameters

_pInfo_

Specifies the pointer to the [PIVOT\_TABLE\_INFO](../structure/pivot_table_info) structure.

## Return Values

The return value is a negative value if it fails.

## Version

Supported on Version 21.4 or later.

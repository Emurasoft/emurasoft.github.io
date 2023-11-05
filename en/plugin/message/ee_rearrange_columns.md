# EE\_REARRANGE\_COLUMNS

Rearranges CSV columns. You can send this message explicitly or use the [Editor\_RearrangeColumns](../macro/editor_rearrangecolumns) inline function.

```
EE_REARRANGE_COLUMNS
wParam = (WPARAM) (REARRANGE_COLULMNS_INFO*)pInfo;
lParam = 0;
```

## Parameters

_pInfo_

Specifies the pointer to the [REARRANGE\_COLUMNS\_INFO](../structure/rearrange_columns_info) structure.

## Return Values

If the message succeeds, the return value is zero. If the message fails,
the return value is nonzero.

## Version

Supported on Version 22.1 or later.

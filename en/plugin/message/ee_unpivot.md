# EE\_UNPIVOT

Converts columns into rows by flattening the CSV data. You can send this message explicitly or use the [Editor\_Unpivot](../macro/editor_unpivot) inline function.

```
EE_UNPIVOT
wParam = (WPARAM)(UNPIVOT*)pInfo;
lParam = 0;
```

## Parameters

_pInfo_

Specifies the pointer to the [UNPIVOT\_INFO](../structure/unpivot_info) structure.

## Return Values

The return value is a negative value if it fails.

## Version

Supported on Version 21.4 or later.

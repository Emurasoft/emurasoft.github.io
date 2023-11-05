# EE\_CONVERT\_CSV

Converts the CSV format of the current document. You can send this message explicitly or use the [Editor\_ConvertCsv](../macro/editor_convertcsv) inline function.

```
EE_CONVERT_CSV
wParam = (WPARAM)(CONVERT_CSV_INFO*)pInfo;
lParam = 0;
```

## Parameters

_pInfo_

Specifies the pointer to the [CONVERT\_CSV\_INFO](../structure/convert_csv_info) structure.

## Return Values

The return value is S\_OK if succeeds.

## Version

Supported on Version 19.8 or later.

# EE\_EXTRACT\_FREQUENT

Extracts frequently used strings into a new document. You can send this message
explicitly or use the [Editor\_ExtractFrequent](../macro/editor_extractfrequent) inline function.

EE\_EXTRACT\_FREQUENT

wParam = (WPARAM) (EXTRACT\_FREQUENT\_INFO\*) pInfo;

lParam = 0;

## Parameters

_pInfo_

Pointer to the [EXTRACT\_FREQUENT\_INFO structure](../structure/extract_frequent_info).

## Return Values

The return value is negative if an error occurs.

## Version

Supported on Version 21.9 or later.

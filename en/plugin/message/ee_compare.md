# EE\_COMPARE

Compares two files. You can send this message explicitly or use
the [Editor\_Compare](../macro/editor_compare) inline function.

```
EE_COMPARE
wParam = (WPARAM) (COMPARE_INFO*) pCompareInfo;
lParam = 0;
```

## Parameters

_pCompareInfo_

Pointer to the [COMPARE\_INFO](../structure/compare_info) structure.

## Return Value

The return value can be one of the following values. The return value is a negative value if an error occurs.

|     |     |
| --- | --- |
| E\_DOCUMENT\_1\_NOT\_FOUND | Cannot find the first document. |
| E\_DOCUMENT\_2\_NOT\_FOUND | Cannot find the second document. |
| E\_FAIL | Unspecified error. |
| E\_NOT\_MDI | Tabs must be enabled. |
| S\_DIFF | Two documents are NOT identical.. |
| S\_MATCHED | Two documents are identical. |
| S\_MATCHED\_IGNORED | Two documents are identical except for ignored places. |

## Version

Supported on EmEditor Professional Version 17.7 or later.

# EE\_INFO\_EX

Retrieves or sets the value of one of the information parameters used by
EmEditor. You can send this message explicitly or use the
[Editor\_DocInfoEx](../macro/editor_docinfoex) inline function.

```
EE_INFO_EX
wParam = (WPARAM)(INFO_EX_DATA*)pInfo;
lParam = 0;
```

## Parameters

_pInfo_

Pointer to a [**INFO\_EX\_DATA** structure](../structure/info_ex_data).

## Return Values

Depends on the parameter specified.

## Version

Supported in EmEditor Professional Version 21.8 or later.

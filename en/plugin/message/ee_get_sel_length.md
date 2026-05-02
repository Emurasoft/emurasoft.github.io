# EE_GET_SEL_LENGTH

Retrieves the length of the selected text. You can send this message explicitly or use the
[Editor_GetSelLength](../macro/editor_getsellength) inline function.

```
EE_GET_SEL_LENGTH
wParam = (WPARAM) (size_t) nMaxLen
lParam = (LPARAM)0
```

## Parameters

_nMaxLen_

Specifies the maximum length. If the length exceeds this value, this value is returned.

## Return Values

The return value is the length of the selected text.

## Version

Supported in EmEditor Professional Version 26.1 or later.

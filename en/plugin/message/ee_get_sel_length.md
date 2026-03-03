# EE_GET_SEL_LENGTH

Retrieves the length of the selected text. You can send this message explicitly or use the
[Editor_GetSelLength](../macro/editor_getsellength) inline function.

```
EE_GET_SEL_LENGTH
wParam = (WPARAM)0
lParam = (LPARAM)0
```

## Return Values

The return value is the length of the selected text. If the length is larger than LONG_MAX, the return value becomes LONG_MAX.

## Version

Supported in EmEditor Professional Version 26.1 or later.

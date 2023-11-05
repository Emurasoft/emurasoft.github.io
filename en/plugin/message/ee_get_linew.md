# EE\_GET\_LINEW

Retrieves the Unicode text on the specified line. You can send this message
explicitly or use the
[Editor\_GetLineW](../macro/editor_getlinew) inline function.

```
EE_GET_LINEW
wParam = (WPARAM) (GET_LINE_INFO*) pGetLineInfo;
lParam = (LPARAM) (LPWSTR) szString;
```

## Parameters

_pGetLineInfo_

Pointer to the [GET\_LINE\_INFO](../structure/get_line_info) structure.

_szString_

Pointer to the buffer that will receive the text.

## Return Values

If _pGetLineInfo->cch_ is zero, the return value is the required
size, in words, for a buffer that can receive the text. If _pGetLineInfo->cch_ is not zero, the
return value is not used.

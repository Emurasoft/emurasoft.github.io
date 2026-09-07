# EE\_GET\_TEXTW

Retrieves the document text. If the document contains more than `0x7ffffffe` UTF-16 code units, the text is truncated to that length. You can send this message explicitly or
by using the [Editor\_GetTextW](../macro/editor_gettextw) inline function.

```
EE_GET_TEXTW
wParam = (WPARAM) (UINT) nBufferSize;
lParam = (LPARAM) (LPWSTR) szBuffer;
```

## Parameters

_nBufferSize_

The capacity of the buffer, in `WCHAR` elements, including space for the terminating null character.

_szBuffer_

A pointer to the buffer that receives the document text.

## Return Values

Returns the required buffer size, in `WCHAR` elements, including the terminating null character.

If the document contains more than `0x7ffffffe` UTF-16 code units, the return value is `0x7fffffff`. Returns zero if an error occurs.

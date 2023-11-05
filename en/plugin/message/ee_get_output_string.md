# EE\_GET\_OUTPUT\_STRING

Retrieves the text in the output bar. You can send this message explicitly or by using the [Editor\_GetOutputString](../macro/editor_getoutputstring) inline function.

```
EE_GET_OUTPUT_STRING
wParam = (WPARAM) (UINT) cchBuf;
lParam = (LPARAM) (LPWSTR) pBuf;
```

## Parameters

_cchBuf_

Specifies the size of the buffer in characters including the terminating NULL character.

_pBuf_

Specifies the pointer to the buffer that receives the text.

## Return Values

The return value is the size of the buffer in characters including the terminating NULL character needed to receive the text.

## Version

Supported on EmEditor Version 9.00 or later.

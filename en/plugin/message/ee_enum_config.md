# EE\_ENUM\_CONFIG

Enumerates available configurations. You can send this message
explicitly or use the [Editor\_EnumConfig](../macro/editor_enumconfig) inline function.

```
EE_ENUM_CONFIG
wParam = (WPARAM) (size_t) cchBuf;
lParam = (LPARAM) (LPWSTR) pBuf;
```

## Parameters

_cchBuf_

Specifies the size of the buffer in characters. Note that two null characters will be added at the end of the list of configurations. If 0 is specified, this message returns the size necessary to retrieve the list of configurations.

_pBuf_

Specifies the pointer to the buffer to retrieve the list of configurations. In this buffer, the list of available configurations each separated by a null character will be retrieved. Two null characters will be added at the end of the list of
configurations. If 0 is specified, pBuf can be NULL.

## Return Values

The return value is the size necessary to retrieve the list of configurations.

## Version

Supported on Version 6.00 or later.

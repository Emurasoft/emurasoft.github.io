# Editor\_EnumConfig

Enumerates available configurations. You can use this inline function or explicitly send the [EE\_ENUM\_CONFIG](../message/ee_enum_config) message.

Editor\_EnumConfig( HWND hwnd, LPWSTR pBuf, size\_t cchBuf );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_cchBuf_

> Specifies the size of the buffer in characters. Note that two null characters will be added at the end of the list of configurations. If 0 is specified, this message returns the size necessary to retrieve the list of configurations.

_pBuf_

> Specifies the pointer to the buffer to retrieve the list of configurations. In this buffer, the list of available configurations each separated by a null character will be retrieved. Two null characters will be added at the end of the list of
> configurations. If 0 is specified, pBuf can be NULL.

## Return Values

> The return value is the size necessary to retrieve the list of configurations.

## Version

> Supported on Version 6.00 or later.

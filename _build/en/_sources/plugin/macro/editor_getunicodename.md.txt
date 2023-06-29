# Editor\_GetUnicodeName

Retrieves the Unicode name of the specified character or string. You can use this inline function or explicitly send the [EE\_GET\_UNICODE\_NAME](../message/ee_get_unicode_name) message.

int Editor\_GetUnicodeName( HWND hwnd, LPWSTR pBuf, int cchBuf, LPCWSTR pstrSrc, int cchSrc );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pBuf_

> Specifies the pointer to the buffer to retrieve the Unicode name.

_cchBuf_

> Specifies the size of the buffer in characters including the terminating NULL.

_pstrSrc_

> Specifies the source character or string.

_cchSrc_

> Specifies the number of characters specified in _pstrSrc_.

## Return Values

> If _cchBuf_ field of the UNICODE\_NAME\_INFO structure is zero, the return value is the required size, in characters,
> for a buffer that can receive the text.

## Version

> Supported on Version 19.1 or later.
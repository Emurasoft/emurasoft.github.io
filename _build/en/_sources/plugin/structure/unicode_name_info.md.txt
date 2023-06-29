# UNICODE\_NAME\_INFO

Used by
[EE\_GET\_UNICODE\_NAME message](../message/ee_get_unicode_name).

typedef struct \_UNICODE\_NAME\_INFO {

UINT cbSize;

int cchBuf;

LPWSTR pBuf;

LPCWSTR pszSrc;

int cchSrc;

} UNICODE\_NAME\_INFO;

## Fields

_cbSize_

> Specifies sizeof( UNICODE\_NAME\_INFO ).

_cchBuf_

> Specifies the size of the buffer in characters including the terminating NULL.

_pBuf_

> Specifies the pointer to the buffer to retrieve the Unicode name.

_pstrSrc_

> Specifies the source character or string.

_cchSrc_

> Specifies the number of characters specified in _pstrSrc_.

## Version

> Supported on Version 19.1 or later.
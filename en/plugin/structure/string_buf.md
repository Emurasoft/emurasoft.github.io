# STRING\_BUF

Used by [EE\_INFO message](../message/ee_info).

typedef struct \_STRING\_BUF {

LPWSTR pBuf;

UINT cchBuf;

} STRING\_BUF;

## Members

_pBuf_

Specifies a buffer to retrieve a string.

_cchBuf_

Specifies the size of the buffer in characters.

## Version

Supported on Version 20.6 or later.

# ACTIVE\_STRING\_INFO

Used by [EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) message.

typedef struct \_ACTIVE\_STRING\_INFO {

UINT cbSize;

LPWSTR pBuf;

UINT cchBuf;

UINT nFlags;

} ACTIVE\_STRING\_INFO;

## Members

_cbSize_

> Size of this data structure, in bytes. Set this member to sizeof( ACTIVE\_STRING\_INFO ) before sending the [EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) message.

_pBuf_

> Specifies the buffer to receive the active string.

_cchBuf_

> Specifies the size of the buffer in characters.

_nFlags_

> Currently not used.

## Version

> Supported on Version 16.9 or later.

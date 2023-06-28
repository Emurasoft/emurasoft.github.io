# UNICODE\_NAME\_INFO

用於 [EE\_GET\_UNICODE\_NAME 消息](../message/ee_get_unicode_name)。

typedef struct \_UNICODE\_NAME\_INFO {

UINT cbSize;

int cchBuf;

LPWSTR pBuf;

LPCWSTR pszSrc;

int cchSrc;

} UNICODE\_NAME\_INFO;

## 欄位

_cbSize_

> 指定這個結構的大小，sizeof( UNICODE\_NAME\_INFO )。

_cchBuf_

> 以字節為單位指定緩衝區大小，包括終止空字元。

_pBuf_

> 指定指針指向的能檢索 Unicode 名的緩衝區。

_pstrSrc_

> 指定源字元或字串。

_cchSrc_

> 指定在 _pstrSrc_ 中指定的字元數。

## 版本

> 支持 EmEditor Professional 19.1 或之後的版本。
# UNICODE\_NAME\_INFO

用于 [EE\_GET\_UNICODE\_NAME 消息](../message/ee_get_unicode_name)。

typedef struct \_UNICODE\_NAME\_INFO {

UINT cbSize;

int cchBuf;

LPWSTR pBuf;

LPCWSTR pszSrc;

int cchSrc;

} UNICODE\_NAME\_INFO;

## 字段

_cbSize_

指定这个结构的大小，sizeof( UNICODE\_NAME\_INFO )。

_cchBuf_

以字节为单位指定缓冲区大小，包括终止空字符。

_pBuf_

指定指针指向的能检索 Unicode 名的缓冲区。

_pstrSrc_

指定源字符或字符串。

_cchSrc_

指定在 _pstrSrc_ 中指定的字符数。

## 版本

支持 EmEditor Professional 19.1 或之后的版本。

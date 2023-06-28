# UNICODE\_NAME\_INFO

[EE\_GET\_UNICODE\_NAME メッセージ](../message/ee_get_unicode_name) で使用します。

typedef struct \_UNICODE\_NAME\_INFO {

UINT cbSize;

int cchBuf;

LPWSTR pBuf;

LPCWSTR pszSrc;

int cchSrc;

} UNICODE\_NAME\_INFO;

## フィールド

_cbSize_

> このデータ構造体のサイズ、sizeof( UNICODE\_NAME\_INFO )を指定します。

_cchBuf_

> 終端 NULL 文字を含めた文字のバッファのサイズを指定します。

_pBuf_

> Unicode名を取得するバッファを指定します。

_pstrSrc_

> ソース文字または文字列を指定します。

_cchSrc_

> _pstrSrc_ で指定された文字数を指定します。

## バージョン

> Version 19.1 以上で利用できます。
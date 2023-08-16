# ACTIVE\_STRING\_INFO

[EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) メッセージで使用します。

typedef struct \_ACTIVE\_STRING\_INFO {

UINT cbSize;

LPWSTR pBuf;

UINT cchBuf;

UINT nFlags;

} ACTIVE\_STRING\_INFO;

## フィールド

_cbSize_

このデータ構造体のサイズ、sizeof( ACTIVE\_STRING\_INFO ) を指定します。

_pBuf_

アクティブな文字列を取得するバッファを指定します。

_cchBuf_

バッファのサイズを文字単位で指定します。

_nFlags_

現在、使用されていません。

## バージョン

Version 16.9 以上で利用できます。

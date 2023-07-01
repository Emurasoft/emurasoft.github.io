# EE\_GET\_LINEW

指定する行のUnicodeテキストを取得します。このメッセージを直接送るか、または
[Editor\_GetLineW インライン関数](../macro/editor_getlinew) を使うことができます。

EE\_GET\_LINEW

wParam = (WPARAM) (GET\_LINE\_INFO\*) pGetLineInfo;

lParam = (LPARAM) (LPWSTR) szString;

## パラメータ

_pGetLineInfo_

> [GET\_LINE\_INFO 構造体](../structure/get_line_info) へのポインタを指定します。

_szString_

> テキストを取得するバッファへのポインタを指定します。

## 戻り値

> _pGetLineInfo->cch_ に 0 を指定した場合、バッファに必要なサイズをバイト単位で返します。 _pGetLineInfo->cch_
> が 0　以外の場合は利用されません。

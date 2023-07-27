# EE\_GET\_CELL

指定するセルのUnicodeテキストを取得します。このメッセージを直接送るか、または
[Editor\_GetCell インライン関数](../macro/editor_getcell) を使うことができます。

EE\_GET\_CELL

wParam = (WPARAM) (GET\_CELL\_INFO\*) pGetCellInfo;

lParam = (LPARAM) (LPWSTR) szString;

## パラメータ

_pGetLineInfo_

[GET\_CELL\_INFO 構造体](../structure/get_cell_info) へのポインタを指定します。

_szString_

テキストを取得するバッファへのポインタを指定します。

## 戻り値

_pGetLineInfo->cch_ に 0 を指定した場合、バッファに必要なサイズをバイト単位で返します。 _pGetLineInfo->cch_
が 0　以外の場合は利用されません。 _pGetLineInfo->cch_ に -1 を指定した場合、列の数を返します。

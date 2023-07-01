# Editor\_GetCell

指定するセルのUnicodeテキストを取得します。このインライン関数を使うか、または [EE\_GET\_CELL](../message/ee_get_cell) メッセージを直接送ることができます。

Editor\_GetCell( HWND hwnd, GET\_CELL\_INFO\* pGetCellInfo, LPWSTR szString );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pGetLineInfo_

> [GET\_CELL\_INFO 構造体](../structure/get_cell_info) へのポインタを指定します。

_szString_

> テキストを取得するバッファへのポインタを指定します。

## 戻り値

> _pGetLineInfo->cch_ に 0 を指定した場合、バッファに必要なサイズを文字単位で返します。 _pGetLineInfo->cch_
> が 0　以外の場合は利用されません。 _pGetLineInfo->cch_ に -1 を指定した場合、列の数を返します。

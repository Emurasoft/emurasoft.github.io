# EE\_SET\_CELL

CSV モードで指定するセルに文字列を設定します。このメッセージを直接送るか、または
[Editor\_SetCell インライン関数](../macro/editor_setcell) を使うことができます。

EE\_SET\_CELL

wParam = (WPARAM) (GET\_CELL\_INFO\*) pGetCellInfo;

lParam = (LPARAM) (LPWSTR) szString;

## パラメータ

_pGetCellInfo_

[GET\_CELL\_INFO 構造体](../structure/get_cell_info) へのポインタを指定します。

_szString_

設定する文字列を指定します。

## 戻り値

成功すると 0 または正の値を返します。失敗すると負の値を返します。

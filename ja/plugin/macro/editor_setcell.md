# Editor\_SetCell

CSV モードで指定するセルに文字列を設定します。このインライン関数を使うか、または [EE\_SET\_CELL](../message/ee_set_cell) メッセージを直接送ることができます。

Editor\_SetCell( HWND hwnd, GET\_CELL\_INFO\* pGetCellInfo, LPCWSTR szString );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pGetCellInfo_

[GET\_CELL\_INFO 構造体](../structure/get_cell_info) へのポインタを指定します。

_szString_

設定する文字列を指定します。

## 戻り値

成功すると 0 または正の値を返します。失敗すると負の値を返します。

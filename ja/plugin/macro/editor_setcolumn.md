# Editor\_SetColumn

CSV モードで指定する列に文字列を設定または挿入します。このインライン関数を使うか、または [EE\_SET\_COLUMN](../message/ee_set_column) メッセージを直接送ることができます。

Editor\_SetColumn( HWND hwnd, COLUMN\_STRUCT\* pColumnStruct );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pGetLineInfo_

[COLUMN\_STRUCT 構造体](../structure/column_struct) へのポインタを指定します。

## 戻り値

成功すると 0 または正の値を返します。失敗すると負の値を返します。

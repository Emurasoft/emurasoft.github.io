# EE\_SET\_COLUMN

CSV モードで指定する列に文字列を設定または挿入します。このメッセージを直接送るか、または
[Editor\_SetColumn](../macro/editor_setcolumn) インライン関数を使うことができます。

EE\_SET\_COLUMN

wParam = (WPARAM)0;

lParam = (LPARAM)(SET\_COLUMN\_INFO\*) pColumnStruct;

## パラメータ

_pColumnStruct_

[COLUMN\_STRUCT](../structure/column_struct) 構造体へのポインタを指定します。

## 戻り値

成功すると 0 または正の値を返します。失敗すると負の値を返します。

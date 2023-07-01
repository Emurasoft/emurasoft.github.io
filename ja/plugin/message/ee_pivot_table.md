# EE\_PIVOT\_TABLE

CSV 文書のピボット テーブルを作成します。このメッセージを直接送るか、または [Editor\_PivotTable インライン関数](../macro/editor_pivottable) を使うことができます。

EE\_PIVOT\_TABLE

wParam = (WPARAM)(PIVOT\_TABLE\_INFO\*)pInfo;

lParam = 0;

## パラメータ

_pInfo_

> [PIVOT\_TABLE\_INFO 構造体](../structure/pivot_table_info) へのポインタを指定します。

## 戻り値

> 失敗すると負の値を返します。

## バージョン

> Version 21.4 以上で利用できます。

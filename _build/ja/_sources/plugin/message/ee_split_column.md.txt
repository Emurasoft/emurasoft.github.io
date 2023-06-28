# EE\_SPLIT\_COLUMN

現在の CSV 文書の指定された列を分割します。このメッセージを直接送るか、または [Editor\_SplitColumn インライン関数](../macro/editor_splitcolumn) を使うことができます。

EE\_SPLIT\_COLUMN

wParam = (WPARAM)(SPLIT\_COLUMN\_INFO\*)pInfo;

lParam = 0;

## パラメータ

_pInfo_

> [SPLIT\_COLUMN\_INFO 構造体](../structure/split_column_info) へのポインタを指定します。

## 戻り値

> 失敗すると負の値を返します。

## バージョン

> Version 19.9 以上で利用できます。
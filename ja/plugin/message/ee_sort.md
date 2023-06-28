# EE\_SORT

文書を並べ替えます。このメッセージを直接送るか、または
[Editor\_Sort インライン関数](../macro/editor_sort) を使うことができます。

EE\_SORT

wParam = 0;

lParam = (LPARAM) (SORT\_INFO\*) pSortInfo;

## パラメータ

_pSortInfo_

> [SORT\_INFO 構造体](../structure/sort_info) へのポインタを指定します。

## 戻り値

> 戻り値は HRESULT 値になります。0 以上の整数は成功を意味し、0 未満の整数は失敗を意味します。

## バージョン

> Version 16.4 以上で利用できます。
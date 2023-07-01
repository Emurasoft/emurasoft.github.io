# EE\_REARRANGE\_COLUMNS

CSV 列を再配置します。このメッセージを直接送るか、または [Editor\_RearrangeColumns インライン関数](../macro/editor_rearrangecolumns) を使うことができます。

EE\_REARRANGE\_COLUMNS

wParam = (WPARAM) (REARRANGE\_COLULMNS\_INFO\*)pInfo;

lParam = 0;

## パラメータ

_pInfo_

> [REARRANGE\_COLUMNS\_INFO 構造体](../structure/rearrange_columns_info) へのポインタを指定します。

## 戻り値

> 成功すると 0 を返します。失敗すると 0 以外を返します。

## バージョン

> Version 22.1 以上で利用できます。

# EE\_GET\_PAGE\_SIZE

1ページのサイズを取得します。このメッセージを直接送るか、または [Editor\_GetPageSize インライン関数](../macro/editor_getpagesize) を使うことができます。

EE\_GET\_PAGE\_SIZE

wParam = 0;

lParam = (LPARAM) (SIZE\_PTR\*) psizePage;

## パラメータ

_psizePage_

1ページに表示できる行数と桁数を表す [SIZE\_PTR 構造体](../structure/size_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。

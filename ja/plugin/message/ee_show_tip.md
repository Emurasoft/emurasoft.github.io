# EE\_SHOW\_TIP

ツールチップの表示/非表示を切り替えます。このメッセージを直接送るか、または
[Editor\_ShowTip インライン関数](../macro/editor_showtip) を使うことができます。

EE\_SHOW\_TIP

wParam = (WPARAM) 0;

lParam = (LPARAM) (TIP\_INFO\*) pTipInfo;

## Parameters

_nFlags_

[TIP\_INFO 構造体](../structure/tip_info) へのポインタを指定します。

## 戻り値

戻り値は利用されません。

## バージョン

EmEditor Professional Version 16.9 以上で利用できます。

# EE\_GET\_REDRAW

ウィンドウの再描画を行うかどうかのフラグを取得します。このメッセージを直接送るか、または [Editor\_GetRedraw インライン関数](../macro/editor_getredraw) を使うことができます。

EE\_GET\_REDRAW

wParam = (WPARAM)0;

lParam = (LPARAM)0;

## パラメータ

パラメータは利用されません。

## 戻り値

再描画を行う状態では TRUE を、そうでなければ FALSE を返します。

## バージョン

Version 5.00 以上で利用できます。

# EP\_PRE\_TRANSLATE\_MSG

Windows メッセージを変換する前に呼び出されます。

EP\_PRE\_TRANSLATE\_MSG

hwnd = hwndView;

wParam = 0;

lParam = (LPARAM) (MSG\*) pMsg;

## パラメータ

_hwndView_

EmEditor ビューのウィンドウ ハンドルが格納されています。

_pMsg_

変換前の Windows メッセージへのポインタが格納されています。

## 戻り値

プラグインでメッセージを処理した場合は TRUE を返すと、メッセージの処理が継続されません。FALSE を返すとメッセージの処理が継続されます。

## バージョン

Version 6.00 以上で利用できます。

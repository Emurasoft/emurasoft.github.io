# Editor\_GetRedraw

ウィンドウの再描画を行うかどうかフラグを取得します。このインライン関数を使うか、または [EE\_GET\_REDRAW メッセージ](../message/ee_get_redraw) を直接送ることができます。

Editor\_GetRedraw( HWND hwnd );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

## 戻り値

> 再描画を行う状態では TRUE を、そうでなければ FALSE を返します。

## バージョン

> Version 5.00 以上で利用できます。
# Editor\_CustomBarClose

カスタム バーを閉じます。このインライン関数を使うか、または [EE\_CUSTOM\_BAR\_CLOSE メッセージ](../message/ee_custom_bar_close) を直接送ることができます。

Editor\_CustomBarClose( HWND hwnd, UINT nCustomBarID );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_nCustomBarID_

> カスタム バー ID を指定します。この値は、Editor\_CustomBarOpen インライン関数を送ったときの戻り値です。

## 戻り値

> 戻り値は利用されません。

## バージョン

> Version 6.00 以上で利用できます。

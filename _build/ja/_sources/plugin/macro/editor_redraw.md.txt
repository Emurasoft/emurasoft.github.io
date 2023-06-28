# Editor\_Redraw

ウィンドウの再描画を行うかどうかを指定します。このインライン関数を使うか、または [EE\_REDRAW メッセージ](../message/ee_redraw) を直接送ることができます。

Editor\_Redraw( HWND hwnd, BOOL bRedraw );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_bRedraw_

> FALSE を指定すると、それ以降、再び TRUE を指定して呼び出すまで、ウィンドウの再描画を行わなくなります。

## 戻り値

> 戻り値は利用されません。
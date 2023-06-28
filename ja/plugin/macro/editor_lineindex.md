# Editor\_LineIndex

指定した行番号のシリアル位置を返します。このインライン関数を使うか、または [EE\_LINE\_INDEX メッセージ](../message/ee_line_index) を直接送ることができます。

Editor\_LineIndex( HWND hwnd, BOOL bLogical, UINT\_PTR yLine );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_bLogical_

> 論理座標を指定する場合は TRUE を、表示座標を指定する場合は FALSE を指定します。

_yLine_

> 行番号を指定します。このパラメータに (UINT)(-1) を指定すると、現在行 (カーソル位置の行) の番号を指定することになります。

## 戻り値

> シリアル位置を返します。
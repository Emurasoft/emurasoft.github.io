# Editor\_LogicalToSerial

論理座標をシリアル位置に変換します。このインライン関数を使うか、または [EE\_LOGICAL\_TO\_SERIAL メッセージ](../message/ee_logical_to_serial) を直接送ることができます。

Editor\_LogicalToSerial( HWND hwnd, POINT\_PTR\* pptLogical );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pptLogical_

> 論理座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> シリアル位置を返します。

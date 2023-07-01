# Editor\_SerialToLogical

シリアル位置を論理座標に変換します。このインライン関数を使うか、または [EE\_SERIAL\_TO\_LOGICAL メッセージ](../message/ee_serial_to_logical) を直接送ることができます。

Editor\_SerialToLogical( HWND hwnd, UINT nSerial, POINT\_PTR\* pptLogical );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nSerial_

> シリアル位置を指定します。

_pptLogical_

> 論理座標を格納するための [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。

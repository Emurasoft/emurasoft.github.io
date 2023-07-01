# Editor\_ViewToDev

表示座標をデバイス座標 (クライアント座標) に変換します。このインライン関数を使うか、または
[EE\_VIEW\_TO\_DEV メッセージ](../message/ee_view_to_dev) を直接送ることができます。

Editor\_ViewToDev( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptDev );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pptView_

> 表示座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_pptDev_

> デバイス座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。指定した値が無効の場合、または指定した値が画面の長方形よりも離れている場合、この構造体の x または y の値は LONG\_PTR\_MIN または LONG\_PTR\_MAX になることがあります。

## 戻り値

> 戻り値は利用されません。

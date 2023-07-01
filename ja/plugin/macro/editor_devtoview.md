# Editor\_DevToView

デバイス座標 (クライアント座標) を表示座標に変換します。このインライン関数を使うか、または
[EE\_DEV\_TO\_VIEW](../message/ee_dev_to_view) メッセージを直接送ることができます。

Editor\_DevToView( HWND hwnd, POINT\_PTR\* pptDev, POINT\_PTR\* pptView );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pptDev_

> デバイス座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_pptView_

> 表示座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。

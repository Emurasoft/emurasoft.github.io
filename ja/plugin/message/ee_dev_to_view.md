# EE\_DEV\_TO\_VIEW

デバイス座標 (クライアント座標) を表示座標に変換します。このメッセージを直接送るか、または
[Editor\_DevToView インライン関数](../macro/editor_devtoview) を使うことができます。

EE\_DEV\_TO\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptDev;

lParam = (LPARAM) (POINT\_PTR\*) pptView;

## パラメータ

_pptDev_

デバイス座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_pptView_

表示座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。

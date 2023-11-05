# EE\_VIEW\_TO\_DEV

表示座標をデバイス座標 (クライアント座標) に変換します。このメッセージを直接送るか、または
[Editor\_ViewToDev インライン関数](../macro/editor_viewtodev) を使うことができます。

```
EE_VIEW_TO_DEV
wParam = (WPARAM) (POINT_PTR*) pptView;
lParam = (LPARAM) (POINT_PTR*) pptDev;
```

## パラメータ

_pptView_

表示座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_pptDev_

デバイス座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。指定した値が無効の場合、または指定した値が画面の長方形よりも離れている場合、この構造体の x または y の値は LONG\_PTR\_MIN または LONG\_PTR\_MAX になることがあります。

## 戻り値

戻り値は利用されません。

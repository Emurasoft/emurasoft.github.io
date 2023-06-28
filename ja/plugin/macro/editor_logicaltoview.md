# Editor\_LogicalToView

論理座標を表示座標に変換します。このインライン関数を使うか、または [EE\_LOGICAL\_TO\_VIEW メッセージ](../message/ee_logical_to_view) を直接送ることができます。

Editor\_LogicalToView( HWND hwnd, POINT\_PTR\* pptLogical, POINT\_PTR\* pptView );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pptLogical_

> 論理座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_pptView_

> 表示座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。
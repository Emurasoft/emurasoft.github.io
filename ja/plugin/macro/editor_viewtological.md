# Editor\_ViewToLogical

表示座標を論理座標に変換します。このインライン関数を使うか、または [EE\_VIEW\_TO\_LOGICAL メッセージ](../message/ee_view_to_logical) を直接送ることができます。

Editor\_ViewToLogical( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptLogical );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pptView_

> 表示座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_pptLogical_

> 論理座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。
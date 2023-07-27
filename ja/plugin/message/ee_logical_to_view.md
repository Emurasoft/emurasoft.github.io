# EE\_LOGICAL\_TO\_VIEW

論理座標を表示座標に変換します。このメッセージを直接送るか、または [Editor\_LogicalToView インライン関数](../macro/editor_logicaltoview) を使うことができます。

EE\_LOGICAL\_TO\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptView;

## パラメータ

_pptLogical_

論理座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_pptView_

表示座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。

# EE\_VIEW\_TO\_LOGICAL

表示座標を論理座標に変換します。このメッセージを直接送るか、または [Editor\_ViewToLogical インライン関数](../macro/editor_viewtological) を使うことができます。

EE\_VIEW\_TO\_LOGICAL

wParam = (WPARAM) (POINT\_PTR\*) pptView;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical;

## パラメータ

_pptView_

表示座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

_pptLogical_

論理座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。

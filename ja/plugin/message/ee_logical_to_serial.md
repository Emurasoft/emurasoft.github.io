# EE\_LOGICAL\_TO\_SERIAL

論理座標をシリアル位置に変換します。このメッセージを直接送るか、または
[Editor\_LogicalToSerial インライン関数](../macro/editor_logicaltoserial) を使うことができます。

EE\_LOGICAL\_TO\_SERIAL

wParam = 0;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical

## パラメータ

_pptLogical_

論理座標を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

シリアル位置を返します。

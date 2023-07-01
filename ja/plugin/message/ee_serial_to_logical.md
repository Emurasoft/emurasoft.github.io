# EE\_SERIAL\_TO\_LOGICAL

シリアル位置を論理座標に変換します。このメッセージを直接送るか、または
[Editor\_SerialToLogical  インライン関数](../macro/editor_serialtological) を使うことができます。

EE\_SERIAL\_TO\_LOGICAL

wParam = (WPARAM) (UINT\_PTR) nSerial;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical;

## パラメータ

_nSerial_

> シリアル位置を指定します。

_pptLogical_

> 論理座標を格納するための [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。

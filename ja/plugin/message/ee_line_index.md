# EE\_LINE\_INDEX

指定した行番号のシリアル位置を返します。このメッセージを直接送るか、または [Editor\_LineIndex インライン関数](../macro/editor_lineindex) を使うことができます。

EE\_LINE\_INDEX

wParam = (WPARAM) (BOOL) bLogical;

lParam = (LPARAM) (UINT\_PTR) yLine;

## パラメータ

_bLogical_

論理座標を指定する場合は TRUE を、表示座標を指定する場合は FALSE を指定します。

_yLine_

行番号を指定します。このパラメータに (UINT)(-1) を指定すると、現在行 (カーソル位置の行) の番号を指定することになります。

## 戻り値

シリアル位置を返します。

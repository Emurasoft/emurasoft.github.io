# EE\_SET\_SEL\_VIEW

選択テキストの開始位置と終了位置を設定します。このメッセージを直接送るか、または
[Editor\_SetSelView インライン関数](../macro/editor_setselview) を使うことができます。

EE\_SET\_SEL\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptSelStart;

lParam = (LPARAM) (POINT\_PTR\*) pptSelEnd;

## パラメータ

_pptSelStart_

> 選択テキストの開始位置を表す [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。位置は表示座標になります。

_pptSelEnd_

> 選択テキストの終了位置を表す [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。位置は表示座標になります。

## 戻り値

> 戻り値は利用されません。

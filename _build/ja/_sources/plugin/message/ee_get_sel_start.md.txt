# EE\_GET\_SEL\_START

選択テキストの開始位置を取得します。このメッセージを直接送るか、または [Editor\_GetSelStart インライン関数](../macro/editor_getselstart) を使うことができます。

EE\_GET\_SEL\_START

wParam = (WPARAM) (int) nLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## パラメータ

_nLogical_

> 次のうちのいずれかを指定します。
>
> | 定数 | 説明 |
> | --- | --- |
> | POS\_VIEW | 表示座標 |
> | POS\_LOGICAL\_A | 論理座標 (2バイト文字を 2 と数えます) |
> | POS\_LOGICAL\_W | 論理座標 (2バイト文字を 1 と数えます) |

_pptPos_

> 選択テキストの開始位置を格納するための [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

> 戻り値は利用されません。
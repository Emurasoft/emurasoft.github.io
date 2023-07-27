# EE\_GET\_SEL\_END

選択テキストの終了位置を取得します。このメッセージを直接送るか、または [Editor\_GetSelEnd インライン関数](../macro/editor_getselend) を使うことができます。

EE\_GET\_SEL\_END

wParam = (WPARAM) (int) nLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## パラメータ

_nLogical_

次のうちのいずれかを指定します。

| 定数 | 説明 |
| --- | --- |
| POS\_VIEW | 表示座標 |
| POS\_LOGICAL\_A | 論理座標 (2バイト文字を 2 と数えます) |
| POS\_LOGICAL\_W | 論理座標 (2バイト文字を 1 と数えます) |

_pptPos_

選択テキストの終了位置を表す POINT\_PTR 構造体へのポインタを指定します。

## 戻り値

戻り値は利用されません。

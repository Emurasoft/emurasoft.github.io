# EE\_SET\_ANCHOR\_POS

選択範囲の開始位置を設定します。このメッセージを直接送るか、または [Editor\_SetAnchorPos インライン関数](../macro/editor_setanchorpos) を使うことができます。

EE\_SET\_ANCHOR\_POS

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
| POS\_CELL | CSV セル単位 |

_pptPos_

選択範囲の開始位置を指定した [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。

## バージョン

Version 4.03 以上で利用できます。

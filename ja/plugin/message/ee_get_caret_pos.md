# EE\_GET\_CARET\_POS

カーソル位置を取得します。このメッセージを直接送るか、または [Editor\_GetCaretPos インライン関数](../macro/editor_getcaretpos) を使うことができます。

```
EE_GET_CARET_POS
wParam = (WPARAM) (int) nLogical;
lParam = (LPARAM) (POINT_PTR*) pptPos;
```

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

カーソル位置を格納するための [POINT\_PTR 構造体](../structure/point_ptr) へのポインタを指定します。

## 戻り値

戻り値は利用されません。

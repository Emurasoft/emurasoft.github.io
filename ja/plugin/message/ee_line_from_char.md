# EE\_LINE\_FROM\_CHAR

指定したシリアル位置の行番号を返します。このメッセージを直接送るか、または
[Editor\_LineFromChar インライン関数](../macro/editor_linefromchar) を使うことができます。

```
EE_LINE_FROM_CHAR
wParam = (WPARAM) (int) nLogical;
lParam = (LPARAM) (UINT_PTR) nSerialIndex;
```

## パラメータ

_nLogical_

次のうちのいずれかを指定します。

| 定数 | 説明 |
| --- | --- |
| POS\_VIEW | 表示座標 |
| POS\_LOGICAL\_A | 論理座標 (2バイト文字を 2 と数えます) |
| POS\_LOGICAL\_W | 論理座標 (2バイト文字を 1 と数えます) |

_nSerialIndex_

シリアル位置を指定します。このパラメータに (UINT\_PTR)(-1) を指定すると、EE\_LINE\_EROM\_CHAR は、現在行 (カーソル位置の行) の行番号を返します。

## 戻り値

行番号を返します。

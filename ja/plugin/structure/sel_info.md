# SEL\_INFO

[EE\_GET\_MULTI\_SEL](../message/ee_get_attr) メッセージ ( [Editor\_GetMultiSel](../macro/editor_getmultisel)
インライン関数) で使用します。

```
typedef struct _SEL_INFO {
	size_t cbSize;
	POINT_PTR ptStart;
	POINT_PTR ptEnd;
	POINT_PTR ptCaret;
} SET_INFO;
```

## フィールド

_cbSize_

sizeof( SEL\_INFO ) を指定する必要があります。

_ptStart_

選択開始位置を指定します。

_ptEnd_

選択終了位置を指定します。

_ptEnd_

カーソル位置を指定します。

## バージョン

Version 13 以上で利用できます。

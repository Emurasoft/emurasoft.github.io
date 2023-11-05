# EE\_GET\_MARGIN

检索边距大小。你能明确地发送该消息或用 [Editor\_GetMargin](../macro/editor_getmargin)
内联函数。

```
EE_GET_MARGIN
wParam = 0;
lParam = 0;
```

## 参数

无。

## 返回值

返回当前被选取的边距大小。如果标准行边距大小以及引用行边距大小不同，更大的边距值会被返回。如果换行方式是按窗口大小换行，返回值取决于当前窗口大小。

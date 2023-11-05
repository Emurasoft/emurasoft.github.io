# EE\_GET\_MARGIN

檢索邊距大小。您能明確地發送該消息或用 [Editor\_GetMargin](../macro/editor_getmargin)
內嵌函式。

```
EE_GET_MARGIN
wParam = 0;
lParam = 0;
```

## 參數

無。

## 返回值

返回當前被選取的邊距大小。如果標準行邊距大小以及引用行邊距大小不同，更大的邊距值會被返回。如果換行方式是按視窗大小換行，返回值取決于當前視窗大小。

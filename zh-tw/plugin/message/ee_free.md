# EE\_FREE

釋放一個指定的外掛程式。您能明確地發送該消息或用 [Editor\_Free](../macro/editor_free) 內嵌函式。

```
EE_FREE
wParam = 0;
lParam = (LPARAM)(ATOM)atom;
```

## 參數

_atom_

指定一個指定外掛程式檔案名的 atom。

## 返回值

如果外掛程式被釋放，返回值是 TRUE。如果外掛程式沒有被釋放，返回值是 FALSE。

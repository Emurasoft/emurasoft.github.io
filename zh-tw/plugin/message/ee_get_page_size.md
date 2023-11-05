# EE\_GET\_PAGE\_SIZE

檢索頁面大小。您能明確地發送該消息或用
[Editor\_GetPageSize](../macro/editor_getpagesize)
內嵌函式。

```
EE_GET_PAGE_SIZE
wParam = 0;
lParam = (LPARAM) (SIZE_PTR*) psizePage;
```

## 參數

_psizePage_

指針指向一個會接收頁面大小的 [SIZE\_PTR 結構](../structure/size_ptr)。頁面大小是一組由在當前 EmEditor 視窗大小中可以顯示的行數以及列數構成的數字。

## 返回值

不使用返回值。

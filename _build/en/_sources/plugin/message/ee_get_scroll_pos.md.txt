# EE\_GET\_SCROLL\_POS

檢索滾動條的當前光標位置。您能明確地發送該消息或用
[Editor\_GetScrollPos](../macro/editor_getscrollpos)
內嵌函式。

EE\_GET\_SCROLL\_POS

wParam = 0;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## 參數

_pptPos_

> 指針指向一個會接收滾動條位置的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

> 不使用返回值。
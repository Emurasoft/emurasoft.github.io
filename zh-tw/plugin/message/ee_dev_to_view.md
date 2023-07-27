# EE\_DEV\_TO\_VIEW

轉換指定位置的設備 (客戶端) 坐標來顯示坐標。您能明確地發送該消息或用
[Editor\_DevToView](../macro/editor_devtoview) 內嵌函式。

EE\_DEV\_TO\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptDev;

lParam = (LPARAM) (POINT\_PTR\*) pptView;

## 參數

_pptDev_

指針指向一個指定要被轉換的設備坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

_pptView_

指針指向一個 [POINT\_PTR 結構](../structure/point_ptr) 來接收轉換后的顯示坐標。

## 返回值

不使用返回值。

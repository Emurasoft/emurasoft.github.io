# EE\_VIEW\_TO\_DEV

把顯示指定位置的顯示坐標轉換為設備 (客戶端) 坐標。您能明確地發送該消息或用
[Editor\_ViewToDev](../macro/editor_viewtodev) 內嵌函式。

EE\_VIEW\_TO\_DEV

wParam = (WPARAM) (POINT\_PTR\*) pptView;

lParam = (LPARAM) (POINT\_PTR\*) pptDev;

## 參數

_pptView_

> 指針指向一個指定要被轉換的顯示坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

_pptDev_

> 指針指向一個要接收轉換后的設備坐標的 [POINT\_PTR 結構](../structure/point_ptr)。這個結構的 x 或 y 值可能會變為 LONG\_PTR\_MIN 或 LONG\_PTR\_MAX，當指定位置無效或指定位置離屏幕矩形太遠。

## 返回值

> 不使用返回值。

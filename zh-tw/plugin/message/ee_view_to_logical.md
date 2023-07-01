# EE\_VIEW\_TO\_LOGICAL

把一個指定位置的顯示坐標轉換為邏輯坐標。您能明確地發送該消息或用
[Editor\_ViewToLogical](../macro/editor_viewtological)
內嵌函式。

EE\_VIEW\_TO\_LOGICAL

wParam = (WPARAM) (POINT\_PTR\*) pptView;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical;

## 參數

_pptView_

> 指針指向一個指定要被轉換的顯示坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

_pptLogical_

> 指針指向一個要接收轉換后的顯示坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

> 不使用返回值。

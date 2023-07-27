# EE\_LOGICAL\_TO\_VIEW

把邏輯坐標轉換為顯示坐標。您能明確地發送該消息或用
[Editor\_LogicalToView](../macro/editor_logicaltoview)
內嵌函式。

EE\_LOGICAL\_TO\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptView;

## 參數

_pptLogical_

指針指向一個指定要被轉換的邏輯坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

_pptView_

指針指向一個 [POINT\_PTR 結構](../structure/point_ptr) 來接收一個轉換后的顯示坐標。

## 返回值

不使用返回值。

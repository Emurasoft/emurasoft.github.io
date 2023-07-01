# Editor\_LogicalToView

把邏輯坐標轉換為顯示坐標。您能直接用該內嵌函式或明確地發送 [EE\_LOGICAL\_TO\_VIEW](../message/ee_logical_to_view) 消息。

Editor\_LogicalToView( HWND hwnd, POINT\_PTR\* pptLogical, POINT\_PTR\* pptView );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pptLogical_

> 指標至一個指定要被轉換的邏輯坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

_pptView_

> 指標至一個要接收轉換后的顯示坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

> 不使用返回值。

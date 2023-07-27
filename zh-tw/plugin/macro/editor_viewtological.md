# Editor\_ViewToLogical

把一個指定位置的顯示坐標轉換為邏輯坐標。您能直接用該內嵌函式或明確地發送
[EE\_VIEW\_TO\_LOGICAL](../message/ee_view_to_logical)
消息。

Editor\_ViewToLogical( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptLogical );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pptView_

指標至一個用來指定要轉換的顯示坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

_pptLogical_

指標至一個要接收轉換后的邏輯坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

不使用返回值。

# Editor\_ViewToDev

把顯示指定位置的顯示坐標轉換為設備 (客戶端) 坐標。您能直接用該內嵌函式或明確地發送
[EE\_VIEW\_TO\_DEV](../message/ee_view_to_dev) 消息。

Editor\_ViewToDev( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptDev );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pptView_

> 指標至一個指定要被轉換的顯示坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

_pptDev_

> 指標至一個要接收轉換后的設備坐標的 [POINT\_PTR 結構](../structure/point_ptr)。這個結構的 x 或 y 值可能會變為 LONG\_PTR\_MIN 或 LONG\_PTR\_MAX，當指定位置無效或指定位置離屏幕矩形太遠。

## 返回值

> 不使用返回值。
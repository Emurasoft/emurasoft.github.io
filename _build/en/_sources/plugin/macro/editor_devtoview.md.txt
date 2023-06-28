# Editor\_DevToView

轉換指定位置的設備 (客戶端) 坐標來顯示坐標。您能直接用該內嵌函式或明確地發送
[EE\_DEV\_TO\_VIEW](../message/ee_dev_to_view) 消息。

Editor\_DevToView( HWND hwnd, POINT\_PTR\* pptDev, POINT\_PTR\* pptView );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pptDev_

> 指標至一個指定要被轉換的設備坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

_pptView_

> 指標至一個 [POINT\_PTR 結構](../structure/point_ptr) 來接收轉換后的顯示坐標。

## 返回值

> 不使用返回值。
# Editor\_SerialToLogical

把序列位置轉換為邏輯坐標。序列位置是以零為初始值的整個文字起始處的字元的索引。
您能直接用該內嵌函式或明確地發送
[EE\_SERIAL\_TO\_LOGICAL](../message/ee_serial_to_logical)
消息。

Editor\_SerialToLogical( HWND hwnd, UINT nSerial, POINT\_PTR\* pptLogical );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nSerial_

指定一個要被轉換的序列位置。

_pptLogical_

指標至一個將接收轉換后的邏輯坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

返回序列位置。

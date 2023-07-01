# Editor\_LogicalToSerial

把邏輯坐標轉換為序列位置。序列位置是以零為初始值的整個文字起始處的字元的索引。
您能直接用該內嵌函式或明確地發送
[EE\_LOGICAL\_TO\_SERIAL](../message/ee_logical_to_serial)
消息。

Editor\_LogicalToSerial( HWND hwnd, POINT\_PTR\* pptLogical );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pptLogical_

> 指標至一個指定要被轉換的邏輯坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

> 返回序列位置。

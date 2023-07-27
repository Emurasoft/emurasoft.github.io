# Editor\_GetColumn

在 CSV 模式中設置一欄文字。你能用該內嵌函式或明確地發送
[EE\_GET\_COLUMN](../message/ee_get_column) 消息。

Editor\_GetColumn( HWND hwnd, COLUMN\_STRUCT\* pColumnStruct );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pColumnStruct_

指針指向 [COLUMN\_STRUCT](../structure/column_struct) 結構。

## 返回值

返回值是緩衝區的大小，包括如果成功檢索文字所需的終止 NULL 的字元數，或者如果失敗的負值。返回值可以大于檢索文字的確切大小。

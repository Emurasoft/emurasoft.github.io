# Editor\_LineIndex

檢索在 EmEditor 中一個指定行的第一個字元的字元索引。一個字元索引是以零為初始值的編輯控件起始處的字元的索引。您能直接用該內嵌函式或明確地發送 [EE\_LINE\_INDEX](../message/ee_line_index)
消息。

Editor\_LineIndex( HWND hwnd, BOOL bLogical, int yLine );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_bLogical_

指定 TRUE，如果行號是按邏輯坐標標示。指定 FALSE，如果行號是按顯示坐標標示。

_yLine_

指定從零開始的行號。-1 代表目前的行 (游標所在行) 的行號。

## 返回值

返回值是在 _yLine_ 參數中指定的行的字元索引。

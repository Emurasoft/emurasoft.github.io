# Editor\_RearrangeColumns

重排 CSV 列。你能直接用该内联函数或明确地发送 [EE\_REARRANGE\_COLUMNS](../message/ee_rearrange_columns) 消息。

Editor\_RearrangeColumns( HWND hwnd, UINT nColumnArraySize, const INT\* piColumn );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nSize_

指定在 _piColumn_ 参数中指定的列数。

_piColumn_

指定一个整数数组，指示要重新排列的列的顺序。例如，"0, 2, 4" 表示结果将包括原始 CSV 文档的第一列、第三列和第五列。

## 返回值

如果消息成功，则返回值为零。如果消息失败，则返回值非零。

## 版本

支持 EmEditor Professional v22.1 或之后的版本。

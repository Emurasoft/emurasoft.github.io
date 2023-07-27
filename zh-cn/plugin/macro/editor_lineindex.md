# Editor\_LineIndex

检索在 EmEditor 中一个指定行的第一个字符的字符索引。一个字符索引是以零为初始值的编辑控件起始处的字符的索引。你能直接用该内联函数或明确地发送 [EE\_LINE\_INDEX](../message/ee_line_index)
消息。

Editor\_LineIndex( HWND hwnd, BOOL bLogical, int yLine );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_bLogical_

指定 TRUE，如果行号是按逻辑坐标标示。指定 FALSE，如果行号是按显示坐标标示。

_yLine_

指定从零开始的行号。-1 代表当前行（光标所在行）的行号。

## 返回值

返回值是在 _yLine_ 参数中指定的行的字符索引。

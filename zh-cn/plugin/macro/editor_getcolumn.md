# Editor\_GetColumn

在 CSV 模式中获取一列文本。你能用该内联函数或明确地发送 [EE\_GET\_COLUMN](../message/ee_get_column) 消息。

Editor\_GetColumn( HWND hwnd, COLUMN\_STRUCT\* pColumnStruct );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pColumnStruct_

指针指向 [COLUMN\_STRUCT](../structure/column_struct) 结构。

## 返回值

返回值是缓冲区的大小，包括如果成功检索文本所需的终止 NULL 的字符数，或者如果失败的负值。返回值可以大于检索文本的确切大小。

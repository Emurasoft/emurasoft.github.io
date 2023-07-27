# Editor\_SetCell

在指定的单元格中设置文本。你能用该内联函数或明确地发送
[EE\_SET\_CELL](../message/ee_set_cell) 消息。

Editor\_SetCell( HWND hwnd, GET\_CELL\_INFO\* pGetCellInfo, LPCWSTR szString );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pGetCellInfo_

指针指向 [GET\_CELL\_INFO](../structure/get_cell_info) 结构。

_szString_

指定要设置的字符串。

## 返回值

如果成功，返回值为零或正数值，如果失败，返回负数值。

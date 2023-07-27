# Editor\_LogicalToSerial

把逻辑坐标转换为序列位置。序列位置是以零为初始值的整个文本起始处的字符的索引。
你能直接用该内联函数或明确地发送
[EE\_LOGICAL\_TO\_SERIAL](../message/ee_logical_to_serial)
消息。

Editor\_LogicalToSerial( HWND hwnd, POINT\_PTR\* pptLogical );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pptLogical_

指针指向一个指定要被转换的逻辑坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

返回序列位置。

# Editor\_SerialToLogical

把序列位置转换为逻辑坐标。序列位置是以零为初始值的整个文本起始处的字符的索引。
你能直接用该内联函数或明确地发送
[EE\_SERIAL\_TO\_LOGICAL](../message/ee_serial_to_logical)
消息。

Editor\_SerialToLogical( HWND hwnd, UINT nSerial, POINT\_PTR\* pptLogical );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nSerial_

> 指定一个要被转换的序列位置。

_pptLogical_

> 指针指向一个将接收转换后的逻辑坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

> 返回序列位置。

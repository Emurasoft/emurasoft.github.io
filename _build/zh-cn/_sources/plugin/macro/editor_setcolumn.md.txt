# Editor\_SetColumn

设置一列文本。你能用该内联函数或明确地发送
[EE\_SET\_COLUMN](../message/ee_set_column) 消息。

Editor\_SetColumn( HWND hwnd, SET\_COLUMN\_INFO\* pSetColumnInfo );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pSetLineInfo_

> 指针指向 [COLUMN\_STRUCT](../structure/column_struct) 结构。

## 返回值

> 如果成功，返回值为零或正数值，如果失败，返回负数值。
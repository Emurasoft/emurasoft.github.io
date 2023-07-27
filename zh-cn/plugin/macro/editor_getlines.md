# Editor\_GetLines

检索当前文档的行数。你能直接用该内联函数或明确地发送 [EE\_GET\_LINES](../message/ee_get_lines) 消息。

Editor\_GetLines( HWND hwnd, int nLogical );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nLogical_

指定下列值之一。

| 值 | 含义 |
| --- | --- |
| POS\_VIEW | 显示坐标 |
| POS\_LOGICAL\_A | 逻辑坐标（把双字节字符计为两个） |
| POS\_LOGICAL\_W | 逻辑坐标（把双字节字符计为一个） |

## 返回值

返回在 EmEditor 中的行数。如果最后的一行以回车结尾，那么最后的一行也会被算在内。如果文本为空，返回 1。

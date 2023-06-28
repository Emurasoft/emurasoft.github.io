# Editor\_GetSelEnd

检索选区的结尾字符位置。你能直接用该内联函数或明确地发送 [EE\_GET\_SEL\_END](../message/ee_get_sel_end) 消息。

Editor\_GetSelEnd( HWND hwnd, int nLogical, POINT\_PTR\* pptPos );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nLogical_

> 指定下列值之一。
>
> | 值 | 含义 |
> | --- | --- |
> | POS\_VIEW | 显示坐标 |
> | POS\_LOGICAL\_A | 逻辑坐标（把双字节字符计为两个） |
> | POS\_LOGICAL\_W | 逻辑坐标（把双字节字符计为一个） |

_pptPos_

> 指针指向一个会接收选区的结尾字符位置的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

> 不使用返回值。
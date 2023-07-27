# Editor\_GetPageSize

检索页面大小。你能直接用该内联函数或明确地发送
[EE\_GET\_PAGE\_SIZE](../message/ee_get_page_size)
消息。

Editor\_GetPageSize( HWND hwnd, SIZE\_PTR\* psizePage );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_psizePage_

指针指向一个会接收页面大小的 [SIZE\_PTR 结构](../structure/size_ptr)。页面大小是一组由在当前 EmEditor 窗口大小中可以显示的行数以及列数构成的数字。

## 返回值

不使用返回值。

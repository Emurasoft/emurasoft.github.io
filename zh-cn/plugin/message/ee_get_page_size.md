# EE\_GET\_PAGE\_SIZE

检索页面大小。你能明确地发送该消息或用
[Editor\_GetPageSize](../macro/editor_getpagesize)
内联函数。

EE\_GET\_PAGE\_SIZE

wParam = 0;

lParam = (LPARAM) (SIZE\_PTR\*) psizePage;

## 参数

_psizePage_

> 指针指向一个会接收页面大小的 [SIZE\_PTR 结构](../structure/size_ptr)。页面大小是一组由在当前 EmEditor 窗口大小中可以显示的行数以及列数构成的数字。

## 返回值

> 不使用返回值。
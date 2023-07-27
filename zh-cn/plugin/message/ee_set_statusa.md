# EE\_SET\_STATUSA

在状态栏上显示一条 ANSI 消息。你能明确地发送该消息或用 [Editor\_SetStatusA](../macro/editor_setstatusa) 内联函数。

EE\_SET\_STATUSA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szStatus;

## 参数

_szStatus_

指定要显示在状态栏上的消息文本。

## 返回值

不使用返回值。

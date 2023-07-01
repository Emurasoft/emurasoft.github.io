# EE\_GET\_CONFIGA

检索所选取的配置名称为 ANSI 字符串。你能明确地发送该消息或用
[Editor\_GetConfigA](../macro/editor_getconfiga) 内联函数。

EE\_GET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPSTR) szConfigName;

## 参数

_szConfigName_

> 指定会接收配置名称的一个缓冲区。缓冲区大小必须至少是 MAX\_CONFIG\_NAME 所标示的字节数。

## 返回值

> 不使用返回值。

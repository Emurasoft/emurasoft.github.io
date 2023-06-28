# EE\_SET\_CONFIGA

变更为一个用 ANSI 字符串指定的配置。你能明确地发送该消息或用
[Editor\_SetConfigA](../macro/editor_setconfiga)
内联函数。

EE\_SET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szConfigName;

## 参数

_szConfigName_

> 用 ANSI 字符串指定一个配置。

## 返回值

> 不使用返回值。
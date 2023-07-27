# EE\_SET\_CONFIGA

變更為一個用 ANSI 字符串指定的配置。您能明確地發送該消息或用
[Editor\_SetConfigA](../macro/editor_setconfiga)
內嵌函式。

EE\_SET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szConfigName;

## 參數

_szConfigName_

用 ANSI 字符串指定一個配置。

## 返回值

不使用返回值。

# EE\_LOAD\_CONFIGA

重新載入由一個 ANSI 字符串指定名稱的配置。您能明確地發送該消息或用
[Editor\_LoadConfigA](../macro/editor_loadconfiga)
內嵌函式。

EE\_LOAD\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szConfigName;

## 參數

_szConfigName_

指定要重新載入的配置名稱。

## 返回值

不使用返回值。

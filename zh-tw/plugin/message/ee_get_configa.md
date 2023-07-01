# EE\_GET\_CONFIGA

檢索所選取的配置名稱為 ANSI 字符串。您能明確地發送該消息或用
[Editor\_GetConfigA](../macro/editor_getconfiga) 內嵌函式。

EE\_GET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPSTR) szConfigName;

## 參數

_szConfigName_

> 指定會接收配置名稱的一個緩沖區。緩沖區大小必須至少是 MAX\_CONFIG\_NAME 所標示的位元數。

## 返回值

> 不使用返回值。

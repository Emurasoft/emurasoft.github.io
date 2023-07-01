# EE\_LOAD\_CONFIGW

重新載入由一個 Unicode 字符串指定名稱的配置。您能明確地發送該消息或用
[Editor\_LoadConfigW](../macro/editor_loadconfigw)
內嵌函式。

EE\_LOAD\_CONFIGW

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szConfigName;

## 參數

_szConfigName_

> 指定要重新載入的配置名稱。

## 返回值

> 不使用返回值。

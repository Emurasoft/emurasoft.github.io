# EE\_SET\_CONFIGW

變更為一個用 Unicode 字符串指定的配置。您能明確地發送該消息或用
[Editor\_SetConfigW](../macro/editor_setconfigw)
內嵌函式。

EE\_SET\_CONFIGW

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szConfigName;

## 參數

_szConfigName_

> 用 Unicode 字符串指定一個配置。

## 返回值

> 不使用返回值。
# EE\_LOAD\_CONFIGW

重新载入由一个 Unicode 字符串指定名称的配置。你能明确地发送该消息或用
[Editor\_LoadConfigW](../macro/editor_loadconfigw)
内联函数。

EE\_LOAD\_CONFIGW

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szConfigName;

## 参数

_szConfigName_

指定要重新载入的配置名称。

## 返回值

不使用返回值。

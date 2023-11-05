# EE\_LOAD\_CONFIGA

重新载入由一个 ANSI 字符串指定名称的配置。你能明确地发送该消息或用
[Editor\_LoadConfigA](../macro/editor_loadconfiga)
内联函数。

```
EE_LOAD_CONFIGA
wParam = 0;
lParam = (LPARAM) (LPCSTR) szConfigName;
```

## 参数

_szConfigName_

指定要重新载入的配置名称。

## 返回值

不使用返回值。

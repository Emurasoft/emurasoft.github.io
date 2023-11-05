# EE\_SET\_CONFIGW

变更为一个用 Unicode 字符串指定的配置。你能明确地发送该消息或用
[Editor\_SetConfigW](../macro/editor_setconfigw)
内联函数。

```
EE_SET_CONFIGW
wParam = 0;
lParam = (LPARAM) (LPCWSTR) szConfigName;
```

## 参数

_szConfigName_

用 Unicode 字符串指定一个配置。

## 返回值

不使用返回值。

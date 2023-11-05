# EE\_RELEASE

递减插件的引用号。你能明确地发送该消息或用 [Editor\_Release](../macro/editor_release) 内联函数。

```
EE_RELEASE
wParam = 0;
lParam = (LPARAM)(HINSTANCE)hInstance;
```

## 参数

_hInstance_

指定插件的实例句柄。

## 返回值

返回值是递减之后的插件的引用号。如果返回值小于或等于零，指定的插件能安全地从 EmEditor 上卸载。

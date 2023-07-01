# Editor\_Release

递减插件的引用号。你能直接用该内联函数或明确地发送 [EE\_RELEASE](../message/ee_release) 消息。

Editor\_Release( HWND hwnd, HINSTANCE hInstance );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_hInstance_

> 指定插件的实例句柄。

## 返回值

> 递减之后的返回值是插件的引用号。如果返回值小于或等于零，指定的插件可以安全地从 EmEditor 上被卸载。

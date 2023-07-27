# Editor\_AddRef

递增插件的引用号。你能直接用该内联函数或明确地发送 [EE\_ADD\_REF](../message/ee_add_ref) 消息。

Editor\_AddRef( HWND hwnd, HINSTANCE hInstance );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_hInstance_

为插件指定实例句柄。

## 返回值

返回值是递增后的插件引用号。如果返回值小于或等于零，指定的插件能从 EmEditor 上安全地卸载。

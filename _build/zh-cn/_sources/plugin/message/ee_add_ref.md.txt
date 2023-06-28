# EE\_ADD\_REF

递增插件的引用号。你可以明确地发送该消息或用 [Editor\_AddRef](../macro/editor_addref) 内联函数。

EE\_ADD\_REF

wParam = 0;

lParam = (LPARAM)(HINSTANCE)hInstance;

## 参数

_hInstance_

> 指定插件的实例句柄。

## 返回值

> 返回值是插件在递增后的引用号。如果返回值被零小或等于零的话，指定的插件能安全地从 EmEditor 上被卸载。
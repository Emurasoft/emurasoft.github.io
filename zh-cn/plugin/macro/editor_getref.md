# Editor\_GetRef

检索一个指定插件的引用号。你能直接用该内联函数或明确地发送 [EE\_GET\_REF](../message/ee_get_ref) 消息。

Editor\_GetRef( HWND hwnd, ATOM atom );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_atom_

指定一个指定插件文件名的 atom。

## 返回值

返回值是一个指定插件的引用号。如果返回值为零，指定的插件能从 EmEditor 上安全卸载。

# EE\_GET\_REF

检索一个指定插件的引用号。你能明确地发送该消息或用
[Editor\_GetRef](../macro/editor_getref) 内联函数。

EE\_GET\_REF

wParam = 0;

lParam = (LPARAM)(ATOM)atom;

## 参数

_atom_

> 指定一个指定插件文件名的 atom。

## 返回值

> 返回值是一个指定插件的引用号。如果返回值为零，指定的插件能从 EmEditor 上安全卸载。

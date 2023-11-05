# EE\_FREE

释放一个指定的插件。你能明确地发送该消息或用 [Editor\_Free](../macro/editor_free) 内联函数。

```
EE_FREE
wParam = 0;
lParam = (LPARAM)(ATOM)atom;
```

## 参数

_atom_

指定一个指定插件文件名的 atom。

## 返回值

如果插件被释放，返回值是 TRUE。如果插件没有被释放，返回值是 FALSE。

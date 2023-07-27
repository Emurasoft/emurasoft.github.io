# Editor\_Free

释放一个指定的插件。你能直接用该内联函数或明确地发送 [EE\_FREE](../message/ee_free) 消息。

Editor\_Free( HWND hwnd, ATOM atom );

## 参数

_hwnd_

通过被查询的 Unicode 指定字符代码。S

_atom_

指定一个指定插件文件名的 atom。

## 返回值

如果插件被释放，返回值是 TRUE。如果插件没有被释放，返回值是 FALSE。

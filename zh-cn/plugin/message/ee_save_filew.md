# EE\_SAVE\_FILEW

保存文本到一个指定的文件中。文件名称被指定为一个 Unicode 字符串。你能明确地发送该消息或用
[Editor\_SaveFileW](../macro/editor_savefilew) 内联函数。

EE\_SAVE\_FILEW

wParam = (WPARAM) (BOOL) bReplace;

lParam = (LPARAM) (LPWSTR) szFileName;

## 参数

_bReplace_

指定 TRUE 如果文本用一个指定的名称保存，并且 EmEditor 保留该文件名。另外，显示在 EmEditor 窗口上的标题也会被改变。指定 FALSE 如果保存了该文本的副本，并且 EmEditor 所保留的文件名称将不会被改变。

_szFileName_

以字节为单位指定一个完整的路径文件名称。

## 返回值

如果消息成功，返回值不是零。如果消息不成功，返回值是零。

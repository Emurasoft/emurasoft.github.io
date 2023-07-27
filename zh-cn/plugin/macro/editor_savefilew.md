# Editor\_SaveFileW

保存文本到一个指定的文件中。文件名称被指定为一个 Unicode 字符串。你能直接用该内联函数或明确地发送
[EE\_SAVE\_FILEW](../message/ee_save_filew) 消息。

Editor\_SaveFileW( HWND hwnd, BOOL bReplace, LPWSTR szFileName );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_bReplace_

指定 TRUE 如果文本用一个指定的名称保存，并且 EmEditor 保留该文件名。另外，显示在 EmEditor 窗口上的标题也会被改变。指定 FALSE 如果保存了该文本的副本，并且 EmEditor 所保留的文件名称将不会被改变。

_szFileName_

以字节为单位指定一个完整的路径文件名称。

## 返回值

如果消息成功，返回值不是零。如果消息不成功，返回值是零。

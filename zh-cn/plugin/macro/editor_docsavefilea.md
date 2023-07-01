# Editor\_DocSaveFileA

保存指定文档中的文本到另一个指定的文件中。你能直接用该内联函数或明确地发送
[EE\_SAVE\_FILEA](../message/ee_save_filea) 消息。

Editor\_DocSaveFileA( HWND hwnd, int iDoc, BOOL bReplace, LPSTR szFileName );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_iDoc_

> 指定从零开始的目标文档的索引。如果指定值为 -1，当前活动文档会被设为目标文档。

_bReplace_

> 指定 TRUE 如果文本用一个指定的名称保存，并且 EmEditor 保留该文件名。另外，显示在 EmEditor 窗口上的标题也会被改变。指定 FALSE 如果保存了该文本的副本，并且 EmEditor 所保留的文件名称将不会被改变。

_szFileName_

> 用字节指定一个完整的路径文件名称。

## 返回值

> 如果消息成功，返回值不是零。如果消息不成功，返回值是零。

## 支持版本

> 支持 EmEditor 5.00 或之后的版本。

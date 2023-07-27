# EE\_LOAD\_FILEA

把一个指定文件载入到 EmEditor 中。文件名称由一个 ANSI 字符串指定。你能明确地发送该消息或用
[Editor\_LoadFileA](../macro/editor_loadfilea) 内联函数。

EE\_LOAD\_FILEA

wParam = (WPARAM) (LOAD\_FILE\_INFO\*) pLoadFileInfo;

lParam = (LPARAM) (LPCSTR) szFileName;

## 参数

_pLoadFileInfo_

指针指向一个 [LOAD\_FILE\_INFO](../structure/load_file_info) 结构。如果该参数为空 (NULL)，EE\_LOAD\_FILEA 会通过属性中预设的方式打开一个文件。

_szFileName_

用字节指定一个完整路径文件名称。如果指定了一个不存在的文件，EE\_LOAD\_FILEA 会失败。

## 返回值

如果命令被启用，返回值就不是零。如果命令没有被启用，返回值是零。

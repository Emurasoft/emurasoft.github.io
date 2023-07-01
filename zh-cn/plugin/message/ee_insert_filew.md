# EE\_INSERT\_FILEW

在光标处插入指定文件内容。文件名用一个 Unicode 字符串指定。你能明确地发送该消息或用
[Editor\_InsertFileW](../macro/editor_insertfilew) 内联函数。

EE\_INSERT\_FILEW

wParam = (WPARAM) (LOAD\_FILE\_INFO\*) pLoadFileInfo;

lParam = (LPARAM) (LPCWSTR) szFileName;

## 参数

_pLoadFileInfo_

> 指针指向一个 [LOAD\_FILE\_INFO](../structure/load_file_info) 结构。如果该参数为空，EE\_INSERT\_FILEW 会通过属性中预设的方式打开一个文件。

_szFileName_

> 指定一个完整路径文件名称。如果指定了一个不存在的文件，EE\_INSERT\_FILEW 会失败。

## 返回值

> 如果命令成功，返回值就不是零。如果命令不成功，返回值是零。

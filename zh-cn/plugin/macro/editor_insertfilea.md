# Editor\_InsertFileA

在光标处插入指定文件内容。文件名用一个 ANSI 字符串指定。你能直接用该内联函数或明确地发送
[EE\_INSERT\_FILEA 消息](../message/ee_insert_filea)。

Editor\_InsertFileA( HWND hwnd, LOAD\_FILE\_INFO\* pLoadFileInfo, LPCSTR
szFileName );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pLoadFileInfo_

指针指向一个 [LOAD\_FILE\_INFO](../structure/load_file_info) 结构。如果该参数为空，Editor\_InsertFileA 会通过属性中预设的方式打开一个文件。

_szFileName_

指定一个完整路径的文件名称。如果指定了一个不存在的文件，Editor\_InsertFileA 会失败。

## 返回值

如果命令成功，返回值就不是零。如果命令不成功，返回值是零。

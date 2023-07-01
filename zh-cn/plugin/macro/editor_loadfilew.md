# Editor\_LoadFileW

把一个指定文件载入到 EmEditor 中。文件名称由一个 Unicode 字符串指定。你能直接用该内联函数或明确地发送
[EE\_LOAD\_FILEW](../message/ee_load_filew) 消息。

Editor\_LoadFileW( HWND hwnd, LOAD\_FILE\_INFO\* pLoadFileInfo, LPCWSTR szFileName
);

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pLoadFileInfo_

> 指针指向一个 [LOAD\_FILE\_INFO](../structure/load_file_info) 结构。如果该参数为空 (NULL)，Editor\_LoadFileW 会通过属性中预设的方式打开一个文件。

_szFileName_

> 用字节指定一个完整路径文件名称。如果指定了一个不存在的文件，Editor\_LoadFileW 会失败。

## 返回值

> 如果命令被启用，返回值就不是零。如果命令没有被启用，返回值是零。

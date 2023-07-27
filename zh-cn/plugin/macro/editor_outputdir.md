# Editor\_OutputDir

为输出栏设置当前目录。你能直接用该内联函数或明确地发送 [EE\_OUTPUT\_DIR](../message/ee_output_dir) 消息。

Editor\_OutputDir( HWND hwnd, LPCWSTR szCurrDir );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_szCurrDir_

指定当前目录。该信息是必需的如果文本含有一个只能从当前目录上跳转的、可点击的相对路径。

## 返回值

不使用返回值。

## 支持版本

支持 EmEditor 7.00 或之后的版本。

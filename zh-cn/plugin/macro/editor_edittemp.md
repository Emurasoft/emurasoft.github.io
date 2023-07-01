# Editor\_EditTemp

把临时文本作为一个新文档打开。你能直接用该内联函数或明确地发送 [EE\_EDIT\_TEMP](../message/ee_edit_temp)
消息。

Editor\_EditTemp( HWND hwnd, LPCWSTR pszTempText, LPCWSTR pszTitle, LPCWSTR pszIconPath, LPCWSTR pszConfig, UINT nEncoding, POINT\_PTR\* pptInitialCaret = NULL, UINT nFlags = 0 );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pszTempText_

> 指定你想要作为一个新文档打开的内存上的临时文本。

_pszTitle_

> 指定新文档的标题。

_pszIconPath_

> 指定你想要用作新文档的图标的路径和文件名称。

_pszConfig_

> 指定新文档应使用的配置名称。

_nEncoding_

> 指定文件的编码。

_pptInitialCaret_

> 指定初始光标位置。

_nFlags_

> 这个值必须是 0。

## 返回值

> 返回值是新文档的 ID。

## 支持版本

> 支持 EmEditor 9.00 或之后的版本。

# Editor\_EditTemp

把临时文本作为一个新文档打开。你能直接用该内联函数或明确地发送 [EE\_EDIT\_TEMP](../message/ee_edit_temp)
消息。

Editor\_EditTemp( HWND hwnd, LPCWSTR pszTempText, LPCWSTR pszTitle, LPCWSTR pszIconPath, LPCWSTR pszConfig, UINT nEncoding, const POINT\_PTR\* pptInitialCaret = NULL, UINT nFlags = 0 );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pszTempText_

指定你想要作为一个新文档打开的内存上的临时文本。

_pszTitle_

指定新文档的标题。

_pszIconPath_

指定你想要用作新文档的图标的路径和文件名称。

_pszConfig_

指定新文档应使用的配置名称。

_nEncoding_

指定文件的编码。

_pptInitialCaret_

指定初始光标位置。

_nFlags_

指定以下值之一。

|     |     |
| --- | --- |
| TEMP\_INFO\_OPEN | 打开一个临时文本。 |
| TEMP\_INFO\_NO\_ID | 打开一个临时文本文件，不设置 ID。使用此标志打开的文档可以在用户选择 **“文件”** 菜单中的 **“另存为”** 时保存到文件中。 |

## 返回值

返回值是新文档的 ID。

## 支持版本

支持 EmEditor 9.00 或之后的版本。

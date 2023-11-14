# Editor\_RunMacro

运行一个宏。你能直接用该内联函数或明确地发送 [EE\_RUN\_MACRO](../message/ee_run_macro)
消息。

Editor\_RunMacro( HWND _hwnd_, UINT _nFlags_, UINT _nDefMacroLang_, LPCWSTR _pszMacroFile_, LPCWSTR _pszText_, const POINT\_PTR\* _pptOrgPos_, POINT\_PTR\* _pptCodePos_, POINT\_PTR\* _pptErrorPos_, HGLOBAL\* _phstrResult_ );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nFlags_

指定下列值之一。

|     |     |
| --- | --- |
| RUN\_FILE | pszMacroFile 参数有效。 |
| RUN\_TEXT | pszText parameter 参数有效。 |

_nDefMacroLang_

指定下列值的组合。

|     |     |
| --- | --- |
| MACRO\_LANG\_JSCRIPT | 该宏是 JScript。 |
| MACRO\_LANG\_V8 | 该宏是 V8。 |
| MACRO\_LANG\_VBSCRIPT | 该宏是 VBScript。 |
| MACRO\_LANG\_UNKNOWN | 该宏语言未知。 |
| MACRO\_SYNC\_ONLY | 同步执行宏。 |

_pszMacroFile_

指定你想要运行的宏文件的路径以及名称。

_pszText_

在内存上指定你想要运行的一段宏文本。

_pptOrgPos_

指定宏的原始位置。

_pptCodePos_

指定宏的代码位置。

_pptErrorPos_

接收宏的错误位置。

_phstrResult_

接收句柄来输出宏返回的字符串。调用方负责使用 GlobalFree 函数来释放该句柄。

## 返回值

返回值是下列值之一。

|     |     |
| --- | --- |
| S\_OK | 成功。 |
| S\_FALSE | 存在一个宏错误，如语法错误。 |
| S\_EDIT\_TEMP | 存在一个宏错误，但无法打开源代码来编辑因为源代码不是一个文本文件。调用方应当用被按照 ptErrorPos 参数提供的信息设置的光标位置来打开源文件。 |
| E\_FAIL | 存在一个严重错误。 |

## 支持版本

支持 EmEditor 9.00 或之后的版本。

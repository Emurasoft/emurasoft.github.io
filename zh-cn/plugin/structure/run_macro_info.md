# RUN\_MACRO\_INFO

用于 [EE\_RUN\_MACRO](../message/ee_run_macro) 消息。

```
typedef struct _RUN_MACRO_INFO {
	size_t cbSize;
	LPCWSTR pszMacroFile;
	LPCWSTR pszText;
	UINT nFlags;
	int nDefMacroLang;
	POINT_PTR ptOrgPos;
	POINT_PTR ptCodePos;
	POINT_PTR ptErrorPos;
	HGLOBAL hstrResult;
} RUN_MACRO_INFO;
```

## 成员

_cbSize_

以字节为单位的数据结构大小。在发送 EE\_RUN\_MACRO 消息之前，把该成员设为 sizeof( RUN\_MACRO\_INFO )。

_pszMacroFile_

指定你想要运行的宏文件的路径以及文件名称。

_pszText_

在内存上指定你想要运行的一段宏文本。

_nFlags_

指定下列值之一。

|     |     |
| --- | --- |
| RUN\_FILE | pszMacroFile 参数有效。 |
| RUN\_TEXT | pszText 参数有效。 |

_nDefMacroLang_

指定下列值的组合。

|     |     |
| --- | --- |
| MACRO\_LANG\_JSCRIPT | 该宏是 JScript。 |
| MACRO\_LANG\_V8 | 该宏是 V8。 |
| MACRO\_LANG\_VBSCRIPT | 该宏是 VBScript。 |
| MACRO\_LANG\_UNKNOWN | 该宏语言未知。 |
| MACRO\_SYNC\_ONLY | 同步执行宏。 |

_ptOrgPos_

指定宏的原始位置。

_ptCodePos_

指定宏的代码位置。

_ptErrorPos_

接收宏的错误位置。

_hstrResult_

输出。接收句柄到宏所返回的输出字符串中。调用方负责使用 GlobalFree 函数来释放该句柄。

## 版本

支持 EmEditor 9.00 或之后的版本。

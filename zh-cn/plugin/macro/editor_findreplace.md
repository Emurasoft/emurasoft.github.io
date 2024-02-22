# Editor\_FindReplace

搜索或替换一个字符串。你能直接用该内联函数或明确地发送 [EE\_FIND\_REPLACE](../message/ee_find_replace) 消息。

HRESULT Editor\_FindReplace( HWND hwnd, UINT64 nFlags, LPCWSTR pszFind, LPCWSTR pszReplace, UINT64\* pnCount, UINT64\* pnMatchedLines );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nFlags_

\[in\] 指定一个下列值的组合。

| 值 | 含义 |
| --- | --- |
| FLAG\_FIND\_AROUND | 移动到文本的开始/结束处。 |
| FLAG\_FIND\_BOOKMARK | 在有匹配的字符串的行上设置书签。 |
| FLAG\_FIND\_CASE | 区分大小写。 |
| FLAG\_FIND\_COUNT | 计算匹配字符串的出现次数。 |
| FLAG\_FIND\_EMBEDDED\_NL | 匹配 CSV 文档中的嵌入式换行符，不匹配其他换行符。 |
| FLAG\_FIND\_ESCAPE | 使用转义序列。 |
| FLAG\_FIND\_EXTRACT | 把匹配的行提取到一个新的文档中。 |
| FLAG\_FIND\_FUZZY | 使用模糊匹配。 |
| FLAG\_FIND\_NEXT | 从光标处往下搜索字符串。如果没有设置该标志，则往上搜索字符串。 |
| FLAG\_FIND\_NO\_OVERLAP | 查找下一个或上一个匹配项时，不匹配重叠字符串。 |
| FLAG\_FIND\_NO\_PROMPT | 禁止显示对话框即使没有找到任何字符串。 |
| FLAG\_FIND\_ONLY\_WORD | 匹配整个单词。 |
| FLAG\_FIND\_OPEN\_DOC | 在同一个框架窗口中，搜索所有打开的文档。 |
| FLAG\_FIND\_REG\_EXP | 使用正则表达式。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作为正则表达式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作为正则表达式引擎。 |
| FLAG\_FIND\_SAVE\_HISTORY | 为重复搜索保存搜索过的字符串。 |
| FLAG\_FIND\_SELECT\_ALL | 选择所有匹配的字符串。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 区分 CR 和 LF 。 |
| FLAG\_FIND\_SEL\_ONLY | 仅搜索选区。 |
| FLAG\_REPLACE\_ALL | 替换所有匹配结果。 |
| FLAG\_REPLACE\_SEL\_ONLY | 当被用 FLAG\_REPLACE\_ALL 指定时，仅在选区中替换。 |

_pszFind_

\[in\] 指定要搜索的字符串。

_pszReplace_

\[in\] 指定要替换的字符串。如果不替换的话，这个值必须是 NULL 。

_pnCount_

\[out\] 指定指针指向接收匹配次数的值，当 nFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT 或 FLAG\_FIND\_FILTER。

_pnMatchedLines_

\[out\] 指定指针指向接收匹配行数的值当 nFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT 或 FLAG\_FIND\_FILTER。

## 返回值

如果找到搜索字符串，返回 S\_OK。如果找不到则返回 S\_FALSE。如果发生错误，返回值是负数。如果一个用户取消搜索，负数值包含 E\_ABORT，如果发生严重错误，返回 E\_FAIL。

## 版本

支持 Version 15.7 或之后的版本。

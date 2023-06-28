# Editor\_BatchFindReplace

搜索或替换多个字符串。你能直接用该内联函数或明确地发送 [EE\_FIND\_REPLACE](../message/ee_find_replace) 消息。

HRESULT Editor\_BatchFindReplace( HWND hwnd, FIND\_REPLACE\_INFO\* pBatchArray, UINT nBatchCount, UINT64 nBatchFlags, UINT64\* pnTotalCount );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pBatchArray_

> 指针指向 [FIND\_REPLACE\_INFO 结构](../structure/find_replace_info)。

_nBatchCount_

> 指定在 _pBatchArray_ 参数中指定的 FIND\_REPLACE\_INFO 结构的数量。

_nBatchFlags_

> \[in\] 指定一个下列值的组合。
>
> | 值 | 含义 |
> | --- | --- |
> | FLAG\_FIND\_AROUND | 移动到文本的开始/结束处。 |
> | FLAG\_FIND\_BOL | 正则表达式 ‘^’ 可匹配选取部分的开头。 |
> | FLAG\_FIND\_BOOKMARK | 在有匹配的字符串的行上设置书签。 |
> | FLAG\_FIND\_COUNT | 计算匹配字符串的出现次数。 |
> | FLAG\_FIND\_COUNT\_FREQUENCY | 根据提取结果创建一个常用字符串表。必须与 FLAG\_FIND\_EXTRACT 和 FLAG\_FIND\_OUTPUT\_DISPLAY 结合使用。必须启用窗口标签页。 |
> | FLAG\_FIND\_EMBEDDED\_NL | 在 CSV 文档中只匹配嵌入式换行，不匹配其他换行。 |
> | FLAG\_FIND\_EOL | 正则表达式 ‘$’ 可匹配选取部分的末尾。 |
> | FLAG\_FIND\_EXTRACT | 把匹配的行提取到一个新文档中。 |
> | FLAG\_FIND\_FUZZY | 使用模糊匹配。 |
> | FLAG\_FIND\_LOOKAROUND | 只在选区内进行正则表达式搜索时用前后断言。 |
> | FLAG\_FIND\_NEXT | 从光标处往下搜索字符串。如果没有设置该标志，则往上搜索字符串。 |
> | FLAG\_FIND\_NO\_PROMPT | 即使未找到任何字符串，也禁止显示对话框。 |
> | FLAG\_FIND\_OPEN\_DOC | 在同一个框架窗口中搜索所有打开的文档。 |
> | FLAG\_FIND\_OUTPUT | 在输出栏中以列表形式显示提取结果。 必须与 FLAG\_FIND\_EXTRACT 结合使用。 |
> | FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作为正则表达式引擎。 |
> | FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作为正则表达式引擎。 |
> | FLAG\_FIND\_SAVE\_HISTORY | 为重复搜索保存搜索过的字符串。 |
> | FLAG\_FIND\_SEPARATE\_CRLF | 区分 CR 和 LF 。 |
> | FLAG\_FIND\_SEL\_ONLY | 仅在选区内搜索。 |
> | FLAG\_REPLACE\_ALL | 替换所有匹配结果。 |
> | FLAG\_REPLACE\_SEL\_ONLY | 当与 FLAG\_REPLACE\_ALL 一起指定时，仅替换选区中的内容。 |

_pnTotalCount_

> \[out\] 指定一个指向变量的指针，当 nBatchFlags 包含 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT 或 FLAG\_FIND\_FILTER 时，该变量将接收出现的次数。

## 返回值

> 如果找到了搜索的字符串，则返回 S\_OK；如果找不到，则返回 S\_FALSE。如果发生错误，返回值是负值。如果用户取消搜索，则负值包括 E\_ABORT；如果发生严重错误，则负值包括E\_FAIL。

## 版本

> 指定 Version 19.9 或之后的版本。
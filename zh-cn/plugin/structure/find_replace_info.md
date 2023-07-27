# FIND\_REPLACE\_INFO

用于 [EE\_FIND\_REPLACE 消息](../message/ee_find_replace) 中。

typedef struct \_FIND\_REPLACE\_INFO {

UINT cbSize;

UINT64 nFlags;

LPCWSTR pszFind;

LPCWSTR pszReplace;

UINT64 nCount;

UINT64 nMatchedLines;

} FIND\_REPLACE\_INFO;

## 构成

_cbSize_

\[in\] 这个数据结构的大小，以字节为单位。在发送 EE\_FIND\_REPLACE 消息之前，把这个构成设为 sizeof( FIND\_REPLACE\_INFO )。

_nFlags_

\[in\] 指定一个下列值的组合。

| 值 | 含义 |
| --- | --- |
| FLAG\_FIND\_AROUND | 移动到文本的开始/结束处。 |
| FLAG\_FIND\_BOL | 正则表达式 ‘^’ 可匹配选取部分的开头。 |
| FLAG\_FIND\_BOOKMARK | 在有匹配的字符串的行上设置书签。 |
| FLAG\_FIND\_CASE | 区分大小写。 |
| FLAG\_FIND\_COUNT | 计算匹配字符串的出现次数。 |
| FLAG\_FIND\_COUNT\_FREQUENCY | 根据提取结果创建一个常用字符串表。必须与 FLAG\_FIND\_EXTRACT 和 FLAG\_FIND\_OUTPUT\_DISPLAY 合用。必须启用窗口标签页。 |
| FLAG\_FIND\_EMBEDDED\_NL | 匹配 CSV 文档中的嵌入式换行符，不匹配其他换行符。 |
| FLAG\_FIND\_EOL | 正则表达式 ‘$’ 可匹配选取部分的末尾。 |
| FLAG\_FIND\_ESCAPE | 使用转义序列。 |
| FLAG\_FIND\_EXTRACT | 把匹配的行提取到一个新的文档中。 |
| FLAG\_FIND\_FUZZY | 使用模糊匹配。 |
| FLAG\_FIND\_LOOKAROUND | 只在选区内进行正则表达式搜索时用前后断言。 |
| FLAG\_FIND\_NEXT | 从光标处往下搜索字符串。如果没有设置该标志，则往上搜索字符串。 |
| FLAG\_FIND\_NO\_PROMPT | 禁止显示对话框即使没有找到任何字符串。 |
| FLAG\_FIND\_NUMBER\_RANGE | 匹配数字范围。此标志不能与FLAG\_FIND\_ESCAPE或FLAG\_FIND\_REG\_EXP组合使用。 |
| FLAG\_FIND\_ONLY\_WORD | 匹配整个单词。 |
| FLAG\_FIND\_OPEN\_DOC | 在同一个框架窗口中，搜索所有打开的文档。 |
| FLAG\_FIND\_OUTPUT | 将提取结果显示为输出栏中的列表。必须与 FLAG\_FIND\_EXTRACT 结合使用。 |
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

_nCount_

\[out\] 返回匹配次数当 nFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT，FLAG\_FIND\_FILTER，或 FLAG\_REPLACE\_ALL。

_nMatchedLines_

\[out\] 返回收匹配行数当 nFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT，FLAG\_FIND\_FILTER，或 FLAG\_REPLACE\_ALL。。

## 版本

支持 Version 15.7 或之后的版本。

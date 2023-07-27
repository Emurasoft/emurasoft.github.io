# Editor\_Filter

用指定的字符串以及设定来筛选文档。你能用这个内联函数或明确地发送 [EE\_FILTER](../message/ee_filter) 消息。

Editor\_Filter( HWND hwnd, LPCWSTR szFilter, int iColumn, UINT nFlags,
INT\_PTR xBegin, INT\_PTR xEnd );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_szFilter_

指定一个要搜索的字符串。

_iColumn_

指定你想要搜索的文本的列索引，或指定 -1 如果你想要搜索整行。

_nFlags_

你能指定一个下列值的组合。

|     |     |
| --- | --- |
| FLAG\_FIND\_BOOKMARKED\_ONLY | 仅匹配书签行。此标志不能与 FLAG\_FIND\_UNBOOKMARKED\_ONLY 合用。 |
| FLAG\_FIND\_CASE | 大小写需符合。 |
| FLAG\_FIND\_CONTINUE | 指定下次调用的 EE\_FILTER 消息不清除筛选记录。此筛选在调用这个消息后不会马上应用。当你想要进行多个级别的筛选时，可以使用这个标志。它与 FLAG\_FIND\_KEEP\_PREVIOUS 标志相同，但由于实际的筛选不会在每次调用消息时被应用，这个方法更适用于多个筛选级别。 |
| FLAG\_FIND\_CR\_LF | 匹配换行符为 CR 和 LF 的行。此标志必须与 FLAG\_FIND\_MATCH\_NL 合用。 |
| FLAG\_FIND\_CR\_ONLY | 匹配换行符为仅 CR 的行。此标志必须与 FLAG\_FIND\_MATCH\_NL 合用。 |
| FLAG\_FIND\_ESCAPE | 使用转义序列。 |
| FLAG\_FIND\_FUZZY | 使用模糊匹配。 |
| FLAG\_FIND\_KEEP\_PREVIOUS | 指定 EE\_FILTER 消息不会在应用新筛选前清除已存在的筛选记录。你可以在你要进行多个级别的筛选时，使用这个标志。 |
| FLAG\_FIND\_LOGICAL\_OR | 指定一个逻辑或运算 (logical OR) 到之前的层级上在多层级筛选的情况下。 |
| FLAG\_FIND\_LF\_ONLY | 匹配换行符为仅 LF 的行。此标志必须与 FLAG\_FIND\_MATCH\_NL 合用。 |
| FLAG\_FIND\_LINK\_FILE | 指定 _pszFilter_ 是链接文件的文件路径，该链接文件包含多个由换行符分隔的搜索字符串。如果一行中包含制表符，则搜索字符串是第一个不包含制表符的字符串。 _pszFilter_ 可能是 EmEditor 安装路径的相对路径。它可能包含环境变量，例如 %USERPROFILE%。 |
| FLAG\_FIND\_MATCH\_NL | 匹配指定的换行符。此标志应与 FLAG\_FIND\_CR\_LF，FLAG\_FIND\_CR\_ONLY，FLAG\_FIND\_LF\_ONLY，和/或 FLAG\_FIND\_NL\_OTHERS 合用。 |
| FLAG\_FIND\_NEGATIVE | 显示筛选工具栏并排除与指定字符串匹配的行。 |
| FLAG\_FIND\_NL\_OTHERS | 匹配没有换行符的行。这些行包括文件的最后一行以及非常长的，继续到下一行而没有换行符行。此标志必须与 FLAG\_FIND\_MATCH\_NL 合用。 |
| FLAG\_FIND\_NUMBER\_RANGE | 匹配数字范围。此标志不能与 FLAG\_FIND\_ESCAPE 或 FLAG\_FIND\_REG\_EXP 合用。 |
| FLAG\_FIND\_ONLY\_WORD | 整个单词需匹配。 |
| FLAG\_FIND\_REG\_EXP | 使用一个正则表达式。 |
| FLAG\_FIND\_REMOVE\_LAST | 删除前一次添加的筛选级别。 |
| FLAG\_FIND\_UNBOOKMARKED\_ONLY | 仅匹配未标记书签的行。此标志不能与 FLAG\_FIND\_BOOKMARKED\_ONLY 合用。 |
| FLAG\_FIND\_WHOLE\_STRING | 匹配整个字符串。 |

_xBegin_

指定你想要搜索的文本的列开始的索引（用逻辑字符数）；你也可以指定 -1 如果你想要把文本的最后一部分作为 _xEnd_。

_xEnd_

指定你想要搜索的文本的列结束的索引（用逻辑字符数）；你也可以指定 -1 如果你想要搜索所有剩下的文本。

## 返回值

返回值是与指定字符串相匹配的行数。如果指定的字符串是一个空字符串，返回值是 -1。如果指定的是 FLAG\_FIND\_CONTINUE，返回值是 0。

## 版本

支持 EmEditor Professional 14.7 或之后的版本。

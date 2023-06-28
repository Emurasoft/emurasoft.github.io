# EE\_REPLACEA

替换一个 ANSI 字符串。你能明确地发送该消息或用
[Editor\_ReplaceA](../macro/editor_replacea) 内联函数。

EE\_REPLACEA

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCSTR) szFindReplace;

## 参数

_nFlags_

> 你能指定一个下列值的组合。
>
> | 值 | 含义 |
> | --- | --- |
> | FLAG\_FIND\_CASE | 区分大小写。 |
> | FLAG\_FIND\_CLOSE | 搜索完成后关闭对话框。 |
> | FLAG\_FIND\_ESCAPE | 使用转义序列。 |
> | FLAG\_FIND\_NO\_PROMPT | 禁止显示对话框即使没有找到字符串。 |
> | FLAG\_FIND\_ONLY\_WORD | 匹配整个单词。 |
> | FLAG\_FIND\_REG\_EXP | 使用正则表达式。 |
> | FLAG\_FIND\_SAVE\_HISTORY | 为重复搜索保存搜索过的字符串。 |
> | FLAG\_REPLACE\_ALL | 替换所有匹配结果。 |
> | FLAG\_REPLACE\_SEL\_ONLY | 当被用 FLAG\_REPLACE\_ALL 指定时，仅在选区中替换。 |

_szFindReplace_

> 指定一个要搜索的字符串和一个用来替换的字符串。你必须按照先指定要搜索的字符串，然后指定用来替换的字符串这个顺序，另外，两者之间必须插入空字符 ('\\0')。

## 返回值

> 如果消息成功，返回值不是零。如果消息不成功，返回值是零。
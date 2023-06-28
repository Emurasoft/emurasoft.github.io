# EE\_FINDW

搜索一个 Unicode 字符串。你能明确地发送该消息或用
the [Editor\_FindW](../macro/editor_findw) 内联函数。

EE\_FINDW

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szFind;

## 参数

_nFlags_

> 你能指定一个下列值的组合。
>
> | 值 | 含义 |
> | --- | --- |
> | FLAG\_FIND\_AROUND | 移动到文本的开始/结束处。 |
> | FLAG\_FIND\_BOOKMARK | 在有匹配的字符串的行上设置书签。 |
> | FLAG\_FIND\_CASE | 区分大小写。 |
> | FLAG\_FIND\_CLOSE | 搜索完成后关闭该对话框。 |
> | FLAG\_FIND\_COUNT | 计算匹配字符串的出现次数。 |
> | FLAG\_FIND\_EMBEDDED\_NL | 匹配 CSV 文档中的嵌入式换行符，不匹配其他换行符。 |
> | FLAG\_FIND\_ESCAPE | 使用转义序列。 |
> | FLAG\_FIND\_NEXT | 从光标处往下搜索字符串。如果没有设置该标志，则往上搜索字符串。 |
> | FLAG\_FIND\_NO\_PROMPT | 禁止显示对话框即使没有找到任何字符串。 |
> | FLAG\_FIND\_ONLY\_WORD | 匹配整个单词。 |
> | FLAG\_FIND\_REG\_EXP | 使用正则表达式。 |
> | FLAG\_FIND\_SAVE\_HISTORY | 为重复搜索保存搜索过的字符串。 |
> | FLAG\_FIND\_SELECT\_ALL | 选择所有匹配的字符串。 |

_szFind_

> 指定一个要搜索的字符串。

## 返回值

> 如果消息成功，返回值为非零值。如果消息不成功，返回值为零。
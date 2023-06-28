# Editor\_EnumHighlight

列举高亮的字符串。你能直接用该内联函数或明确地发送 [EE\_ENUM\_HIGHLIGHT](../message/ee_enum_highlight) 消息。

Editor\_EnumHighlight( HWND hwnd, LPWSTR pBuf, size\_t cchBuf );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_cchBuf_

> 用字符数指定缓冲区大小。要注意的是两个空字符会被添加到高亮字符串列表末尾。如果指定的数值为 0，该消息会返回需要检索高亮字符串列表的大小。

_pBuf_

> 指定指针指向缓冲区来检索高亮字符串列表。在这个缓冲区内，由一个空字符分隔的可用的高亮字符串列表会被检索。两个空字符会被添加到高亮字符串列表末尾。如果指定的数值为 0，pBuf 是空 (NULL)。
>
> The first character of each string represents the color and a combination of the following values.
>
> |     |     |
> | --- | --- |
> | 从 0 到 9 | 颜色。用 HIGHLIGHT\_COLOR\_MASK 作为掩码。 |
> | HIGHLIGHT\_WORD | 全词匹配时高亮 |
> | HIGHLIGHT\_RIGHT\_SIDE | 高亮到选定单词右侧。 |
> | HIGHLIGHT\_INSIDE\_TAG | 仅在标记内。 |
> | HIGHLIGHT\_REG\_EXP | 正则表达式。 |
> | HIGHLIGHT\_CASE | 匹配大小写。 |
> | HIGHLIGHT\_RIGHT\_ALL | 高亮单词与其右侧区域。 |

## 返回值

> 返回值是检索高亮字符串列表的必需大小。

## 支持版本

> 支持 EmEditor 7.00 或之后的版本。
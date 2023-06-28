# HISTORY\_INFO

用于 [EVENT\_HISTORY 时间](../event/index) 中。

typedef struct \_HISTORY\_INFO {

size\_t cbSize;

UINT nFlags;

POINT\_PTR ptTop;

POINT\_PTR ptBottom;

UINT nChar;

LPCWSTR pszString;

} HISTORY\_INFO;

## 成员

_cbSize_

> 以字节为单位的数据结构大小。在接收 EVENT\_HISTORY 之前，把该成员设为 sizeof( HISTORY\_INFO )。

_nFlags_

> 指定一个下列值的组合。
>
> |     |     |
> | --- | --- |
> | HISTORY\_INSERT\_CHAR | 插入了一个字符。 |
> | HISTORY\_BACK\_SPACE | 按了后退键来移除字符。 |
> | HISTORY\_DELETE\_CHAR | 按下删除键来移除字符。 |
> | HISTORY\_INSERT\_STRING | 插入了一个字符串。 |
> | HISTORY\_DELETE\_STRING | 删除了一个字符串。 |
> | HISTORY\_INSERT\_TAB\_SEL | 按了 Tab 键来缩进选区。 |
> | HISTORY\_MODIFIED | 文档被修改。 |
> | HISTORY\_COMBINED | 历史记录事件应与更早之前的事件合并。 |
> | HISTORY\_CR\_ONLY | 被移除的字符是仅 CR。 |
> | HISTORY\_LF\_ONLY | 被移除的字符是仅 LF。 |
> | HISTORY\_SEL\_BOX | 插入的字符串是一个垂直选取。 |
> | HISTORY\_INSIDE\_UNDO | 该操作被包含在撤消命令里。 |
> | HISTORY\_INSIDE\_REDO | 该操作被包含在重做命令里。 |

_ptTop_

> 这个成员包含之前的光标位置。如果 nFlags 成员包含 HISTORY\_INSERT\_STRING，这个成员是选区的起始位置。

_ptBottom_

> 如果 nFlags 成员包含 HISTORY\_INSERT\_STRING，那么该成员是选区的结尾位置。不然，忽略这个成员。

_nChar_

> 如果 nFlags 包含 HISTORY\_BACK\_SPACE 或 HISTORY\_DELETE\_CHAR，这个成员包含被移除的字符。

_pszString_

> 如果 nFlags 成员包含 HISTORY\_DELETE\_STRING，该成员包含被移除的字符串。

## 版本

> 支持 EmEditor 9.00 或之后的版本。
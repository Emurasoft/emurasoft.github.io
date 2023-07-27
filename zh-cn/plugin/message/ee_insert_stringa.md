# EE\_INSERT\_STRINGA

把一个 ANSI 字符串插入到当前光标位置处。你能明确地发送该消息或用
[Editor\_InsertStringA 宏](../macro/editor_insertstringa)， [Editor\_InsertA 宏](../macro/editor_inserta)，或
[Editor\_OverwriteA](../macro/editor_overwritea) 内联函数。

EE\_INSERT\_STRINGA

wParam = nInsertType;

lParam = (LPARAM) (LPCSTR) szString;

## 参数

_nInsertType_

指定一个下列值的组合。

|     |     |
| --- | --- |
| OVERWRITE\_PER\_PROP | 插入或改写取决于当前“插入/改写”状态。 |
| OVERWRITE\_INSERT | 总是插入，不改写已存在的字符串。 |
| OVERWRITE\_OVERWRITE | 总是改写已存在的字符串。 |
| KEEP\_SOURCE\_RETURN\_TYPE | 保持在 szString 指定的换行方式（仅 CR，仅 LF，或 CR 和 LF）。 |
| KEEP\_DEST\_RETURN\_TYPE | 保持目标的换行方式（仅 CR，仅 LF，或 CR 和 LF）。 |

_szString_

指定要被插入的字符串。

## 返回值

不使用返回值。

## 支持版本

KEEP\_SOURCE\_RETURN\_TYPE 和 KEEP\_DEST\_RETURN\_TYPE 标志都在 EmEditor 7.00 或之后的版本上支持。

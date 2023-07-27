# EE\_INSERT\_STRINGW

把一个 Unicode 字符串插入到当前光标位置处。你能明确地发送该消息或用
[Editor\_InsertStringW 内联函数](../macro/editor_insertstringw)， [Editor\_InsertW 内联函数](../macro/editor_insertw)，或
[Editor\_OverwriteW](../macro/editor_overwritew) 内联函数。

EE\_INSERT\_STRINGW

wParam = nInsertType;

lParam = (LPARAM) (LPCWSTR) szString;

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

# EE\_INSERT\_STRINGA

把一個 ANSI 字符串插入到當前光標位置處。您能明確地發送該消息或用
[Editor\_InsertStringA 巨集](../macro/editor_insertstringa)， [Editor\_InsertA 巨集](../macro/editor_inserta)，或
[Editor\_OverwriteA](../macro/editor_overwritea) 內嵌函式。

EE\_INSERT\_STRINGA

wParam = nInsertType;

lParam = (LPARAM) (LPCSTR) szString;

## 參數

_nInsertType_

> 從如下值中指定一個組合。
>
> |     |     |
> | --- | --- |
> | OVERWRITE\_PER\_PROP | 插入或改寫取決于當前「插入/改寫」狀態。 |
> | OVERWRITE\_INSERT | 總是插入，不改寫已存在的字符串。 |
> | OVERWRITE\_OVERWRITE | 總是改寫已存在的字符串。 |
> | KEEP\_SOURCE\_RETURN\_TYPE | 保持在 szString 指定的換行方式 (僅 CR，僅 LF，或 CR 和 LF) 。 |
> | KEEP\_DEST\_RETURN\_TYPE | 保持目標的換行方式 (僅 CR，僅 LF，或 CR 和 LF) 。 |

_szString_

> 指定要被插入的字符串。

## 返回值

> 不使用返回值。

## 支持版本

> KEEP\_SOURCE\_RETURN\_TYPE 和 KEEP\_DEST\_RETURN\_TYPE 標志都在 EmEditor 7.00 或之後的版本上支持。
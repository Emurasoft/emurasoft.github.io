# EE\_INSERT\_STRINGW

把一個 Unicode 字符串插入到當前光標位置處。您能明確地發送該消息或用
[Editor\_InsertStringW 內嵌函式](../macro/editor_insertstringw)， [Editor\_InsertW 內嵌函式](../macro/editor_insertw)，或
[Editor\_OverwriteW](../macro/editor_overwritew) 內嵌函式。

```
EE_INSERT_STRINGW
wParam = nInsertType;
lParam = (LPARAM) (LPCWSTR) szString;
```

## 參數

_nInsertType_

從如下值中指定一個組合。

|     |     |
| --- | --- |
| OVERWRITE\_PER\_PROP | 插入或改寫取決于當前「插入/改寫」狀態。 |
| OVERWRITE\_INSERT | 總是插入，不改寫已存在的字符串。 |
| OVERWRITE\_OVERWRITE | 總是改寫已存在的字符串。 |
| KEEP\_SOURCE\_RETURN\_TYPE | 保持在 szString 指定的換行方式 (僅 CR，僅 LF，或 CR 和 LF) 。 |
| KEEP\_DEST\_RETURN\_TYPE | 保持目標的換行方式 (僅 CR，僅 LF，或 CR 和 LF) 。 |

_szString_

指定要被插入的字符串。

## 返回值

不使用返回值。

## 支持版本

KEEP\_SOURCE\_RETURN\_TYPE 和 KEEP\_DEST\_RETURN\_TYPE 標志都在 EmEditor 7.00 或之後的版本上支持。

# EE\_LINE\_FROM\_CHAR

檢索包含指定字符索引 (序列位置) 的行的索引。一個字符索引是以零為初始值的整個文本起始處的字符的索引。您能明確地發送該消息或用
[Editor\_LineFromChar](../macro/editor_linefromchar)
內嵌函式。

EE\_LINE\_FROM\_CHAR

wParam = (WPARAM) (int) nLogical;

lParam = (LPARAM) (UINT) nSerialIndex;

## 參數

_nLogical_

指定下列值之一。

| 值 | 含義 |
| --- | --- |
| POS\_VIEW | 顯示坐標 |
| POS\_LOGICAL\_A | 邏輯坐標 (把雙位元字符計為兩個) |
| POS\_LOGICAL\_W | 邏輯坐標 (把雙位元字符計為一個) |

_nSerialIndex_

指定被包含在要被檢索的行號中的字符的字符索引。如果參數是 -1，EE\_LINE\_FROM\_CHAR 檢索當前行 (光標所在行) 的行號。

## 返回值

返回值是從零開始的、包含由 _nSerialIndex_ 指定的字符索引的行號。

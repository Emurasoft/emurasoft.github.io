# Editor\_LineFromChar

檢索包含指定字元索引 (序列位置) 的行的索引。一個字元索引是以零為初始值的整個文字起始處的字元的索引。您能直接用該內嵌函式或明確地發送
[EE\_LINE\_FROM\_CHAR](../message/ee_line_from_char)
消息。

Editor\_LineFromChar( HWND hwnd, int nLogical, UINT nSerialIndex );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nLogical_

> 指定下列值之一。
>
> | 值 | 含義 |
> | --- | --- |
> | POS\_VIEW | 顯示坐標 |
> | POS\_LOGICAL\_A | 邏輯坐標 (把雙位元字元計為兩個) |
> | POS\_LOGICAL\_W | 邏輯坐標 (把雙位元字元計為一個) |

_nSerialIndex_

> 指定被包含在要被檢索的行號中的字元的字元索引。如果參數是 -1，EE\_LINE\_FROM\_CHAR
> 檢索目前的行 (游標所在行) 的行號。

## 返回值

> 返回值是從零開始的、包含由 _nSerialIndex_ 指定的字元索引的行號。
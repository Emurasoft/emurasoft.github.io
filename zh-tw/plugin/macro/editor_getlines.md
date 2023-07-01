# Editor\_GetLines

檢索目前的文檔的行數。您能直接用該內嵌函式或明確地發送 [EE\_GET\_LINES](../message/ee_get_lines) 消息。

Editor\_GetLines( HWND hwnd, int nLogical );

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

## 返回值

> 返回在 EmEditor 中的行數。如果最后的一行以歸位結尾，那么最后的一行也會被算在內。如果文字為空，返回 1。

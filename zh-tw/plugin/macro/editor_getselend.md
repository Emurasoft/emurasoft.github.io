# Editor\_GetSelEnd

檢索選區的結尾字元位置。您能直接用該內嵌函式或明確地發送 [EE\_GET\_SEL\_END](../message/ee_get_sel_end) 消息。

Editor\_GetSelEnd( HWND hwnd, int nLogical, POINT\_PTR\* pptPos );

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

_pptPos_

> 指標至一個會接收選區的結尾字元位置的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

> 不使用返回值。
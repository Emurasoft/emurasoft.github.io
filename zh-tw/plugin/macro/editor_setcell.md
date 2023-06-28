# Editor\_SetCell

在指定的儲存格中設置文字。你能用該內嵌函式或明確地發送
[EE\_GET\_CELL](../message/ee_set_cell) 消息。

Editor\_SetCell( HWND hwnd, GET\_CELL\_INFO\* pGetCellInfo, LPCWSTR szString );

## 參數

_hwnd_

> 指定 EmEditor 視圖或方塊架的視窗控制代碼。

_pGetCellInfo_

> 指針指向 [GET\_CELL\_INFO](../structure/get_cell_info) 結構。

_szString_

> 指定要設置的字串。

## 返回值

> 如果成功，返回值為零或正數值，如果失敗，返回負數值。
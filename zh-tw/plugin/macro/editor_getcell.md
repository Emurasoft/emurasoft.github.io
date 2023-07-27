# Editor\_GetCell

在指定的儲存格內檢索 Unicode 文字。你能用該內嵌函式或明確地發送
[EE\_GET\_CELL](../message/ee_get_cell) 消息。

Editor\_GetCell( HWND hwnd, GET\_CELL\_INFO\* pGetCellInfo, LPWSTR szString );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pGetCellInfo_

指針指向 [GET\_CELL\_INFO](../structure/get_cell_info) 結構。

_szString_

指針指向要接收文字的緩衝區。

## 返回值

如果 _pGetCellInfo->cch_ 是零，返回值是一個緩衝區能接收文字的必需的大小，以字元為單位。如果 _pGetLineInfo->cch_ 不是零，則不使用返回值。如果 _pGetCellInfo->iColumn_ 是 -1，返回值,是列數。

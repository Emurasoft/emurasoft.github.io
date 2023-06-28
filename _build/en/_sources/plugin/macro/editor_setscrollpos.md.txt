# Editor\_SetScrollPos

指定捲動欄位置。您能直接用該內嵌函式或明確地發送 [EE\_SET\_SCROLL\_POS](../message/ee_set_scroll_pos) 消息。

Editor\_SetScrollPos( HWND hwnd, POINT\_PTR\* pptPos );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pptPos_

> 指標至一個指定捲動欄位置的 [POINT\_PTR 結構](../structure/point_ptr)。游標位置將不會被改變。

## 返回值

> 不使用返回值。
# Editor\_GetScrollPos

檢索捲軸的目前的游標位置。您能直接用該內嵌函式或明確地發送
[EE\_GET\_SCROLL\_POS](../message/ee_get_scroll_pos)
消息。

Editor\_GetScrollPos( HWND hwnd, POINT\_PTR\* pptPos );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pptPos_

指標至一個會接收捲軸位置的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

不使用返回值。

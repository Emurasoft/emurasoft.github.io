# Editor\_SetScrollPosEx

指定捲動欄位置。您能直接用該內嵌函式或明確地發送 [EE\_SET\_SCROLL\_POS](../message/ee_set_scroll_pos) 消息。

Editor\_SetScrollPos( HWND hwnd, POINT\* pptPos, BOOL bCanMoveCursor );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pptPos_

> 指標至一個指定捲動欄位置的 [POINT\_PTR](../structure/point_ptr)。游標位置將不會被改變。

_bCanMoveCursor_

> 如果該參數是 TRUE 并且 [**通過捲動位置移動游標** 核取方塊](../../dlg/properties/scroll/index) 被勾選，游標位置也會被移動。如果該參數是 FALSE，游標位置則不會被移動。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 5.00 或之後的版本。

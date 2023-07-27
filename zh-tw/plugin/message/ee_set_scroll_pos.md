# EE\_SET\_SCROLL\_POS

指定滾動欄位置。您能明確地發送該消息或用 [Editor\_SetScrollPos](../macro/editor_setscrollpos) 內嵌函式或 [Editor\_SetScrollPosEx](../macro/editor_setscrollposex) 內嵌函式。

EE\_SET\_SCROLL\_POS

wParam = (WPARAM) (BOOL) bCanMoveCursor;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## 參數

_bCanMoveCursor_

如果該參數是 TRUE 并且 [通過滾動位置移動光標 復選框](../../dlg/properties/scroll/index) 被勾選，光標位置也會被移動。如果該參數是 FALSE，光標位置則不會被移動。

_pptPos_

指針指向一個指定滾動欄位置的 [POINT\_PTR 結構](../structure/point_ptr)。光標位置將不會被改變。

## 返回值

不使用返回值。

## 支持版本

支持 EmEditor 3.00 或之後的版本。然而，bCanMoveCursor 支持 EmEditor 5.00 或之後的版本。在前幾個版本中，bCanMoveCursor 被假定為 FALSE.

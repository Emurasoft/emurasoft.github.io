# Editor\_SetCaretPosEx

移動游標位置并且選擇性地延伸選區。您能直接用該內嵌函式或明確地發送 [EE\_SET\_CARET\_POS](../message/ee_set_caret_pos) 消息。

Editor\_SetCaretPosEx( HWND hwnd, int nLogical, POINT\_PTR\* pptPos,
BOOL bExtend );

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
> | POS\_SCROLL\_ALWAYS | 當與 POS\_SCROLL\_CENTER 或 POS\_SCROLL\_TOP 一起使用時，游標位置會移動即使目前的游標位置已經可見。 |
> | POS\_SCROLL\_CENTER | 游標位置向視窗中心靠近。 |
> | POS\_SCROLL\_DONT\_CARE | 游標位置成為捲動變得最小的地方。 |
> | POS\_SCROLL\_TOP | 游標位置成為視窗的頂部。 |

_pptPos_

> 指標至一個指定游標位置的 [POINT\_PTR 結構](../structure/point_ptr)。

_bExtend_

> 決定是否要延伸目前的選區。如果 _bExtend_ 是 TRUE，那么選區活動尾端會移動到指定位置，而定位端仍會呆在原來的位置。否則，兩端都會被移動到指定的位置。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 4.03 或之後的版本。然而，POS\_SCROLL\_DONT\_CARE，POS\_SCROLL\_CENTER，以及 POS\_SCROLL\_TOP 標志支持 EmEditor 6.00 或之後的版本。POS\_SCROLL\_ALWAYS 支持 EmEditor 7.00.4 或之後的版本。
# Editor\_SetSelView

變更選區的開始和結束位置。您能直接用該內嵌函式或明確地發送 [EE\_SET\_SEL\_VIEW](../message/ee_set_sel_view) 消息。

Editor\_SetSelView( HWND hwnd, POINT\_PTR\* pptSelStart, POINT\_PTR\* pptSelEnd );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pptSelStart_

> 指標至一個指定選區開始位置的 [POINT\_PTR 結構](../structure/point_ptr)。該位置由顯示坐標標示。

_pptSelEnd_

> 指標至一個指定選區結束位置的 [POINT\_PTR 結構](../structure/point_ptr)。該位置由顯示坐標標示。

## 返回值

> 不使用返回值。

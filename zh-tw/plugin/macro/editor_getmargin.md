# Editor\_GetMargin

檢索邊距大小。您能直接用該內嵌函式或明確地發送 [EE\_GET\_MARGIN](../message/ee_get_margin)
消息。

Editor\_Convert( HWND hwnd );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

## 返回值

> 返回目前的被選取的邊距大小。如果標準行邊距大小以及引用行邊距大小不同，更大的邊距值會被返回。如果換行方式是按視窗大小換行，返回值取決于目前的視窗大小。

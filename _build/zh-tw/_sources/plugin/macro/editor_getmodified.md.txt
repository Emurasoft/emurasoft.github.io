# Editor\_GetModified

檢索文本的修改狀態。您能直接用該內嵌函式或明確地發送 [EE\_GET\_MODIFIED](../message/ee_get_modified) 消息。

Editor\_GetModified( HWND hwnd );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

## 返回值

> 如果文本被修改，返回值是 TRUE。如果文本沒有被修改，返回值是 FALSE。
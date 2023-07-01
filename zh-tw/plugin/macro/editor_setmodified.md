# Editor\_SetModified

變更文字的修改狀態。您能直接用該內嵌函式或明確地發送 [EE\_SET\_MODIFIED](../message/ee_set_modified) 消息。

Editor\_SetModified( HWND hwnd, BOOL bModified );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_bModified_

> TRUE，把狀態變更為修改過，或 FALSE，把狀態變更為未經修改。

## 返回值

> 不使用返回值。

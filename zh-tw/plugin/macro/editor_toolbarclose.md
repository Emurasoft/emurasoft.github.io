# Editor\_ToolbarClose

關閉一個自訂工具列。您能直接用該內嵌函式或明確地發送 [EE\_TOOLBAR\_CLOSE](../message/ee_toolbar_close)
消息。

Editor\_ToolbarClose( HWND hwnd, UINT nCustomRebarID );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nToolbarID_

> 指定要關閉的工具列。這會是 EE\_TOOLBAR\_OPEN 消息的返回值。

## 返回值

> 如果消息成功并且工具列狀態被改變，返回值是 TRUE。如果消息不成功或工具列狀態沒有更改，返回值是 FALSE。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。

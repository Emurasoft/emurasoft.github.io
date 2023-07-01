# Editor\_CustomBarClose

關閉自訂顯示條。您能直接用該內嵌函式或明確地發送 [EE\_CUSTOM\_BAR\_CLOSE](../message/ee_custom_bar_close) 消息。

Editor\_CustomBarClose( HWND hwnd, UINT nCustomBarID );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nCustomBarID_

> 指定要關閉的自訂顯示條。這會是 Editor\_CustomBarOpen 內嵌函式的返回值。

## 返回值

> 如果消息成功，返回值為非零值。如果該消息不成功，返回值為零。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。

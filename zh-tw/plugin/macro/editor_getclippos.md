# Editor\_GetClipPos

檢索剪貼簿記錄中的目前的位置。您能直接用該內嵌函式或明確地發送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_GetClipPos( HWND hwnd );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

## 返回值

> 檢索剪貼簿記錄中的目前的位置。如果消息不成功，返回值是 -1。

## 支持版本

> 支持 EmEditor 9.00 或之後的版本。

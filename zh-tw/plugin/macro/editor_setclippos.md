# Editor\_SetClipPos

在剪貼簿記錄上設置目前的位置。您能直接用該內嵌函式或明確地發送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_SetClipPos( HWND hwnd, int iPos );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_iPos_

在剪貼簿記錄上指定新位置。

## 返回值

在剪貼簿記錄上檢索目前的位置。如果消息失敗，返回值是 -1。

## 支持版本

支持 EmEditor 9.00 或之後的版本。

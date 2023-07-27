# Editor\_RotateClip

在剪貼簿記錄上旋轉目前的位置。您能直接用該內嵌函式或明確地發送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_RotateClip( HWND hwnd, int iDirection );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_iDirection_

指定您想要在剪貼簿記錄上旋轉目前的位置的方向。

## 返回值

如果成功的話，返回值是 1。如果消息失敗，返回值是 -1。

## 支持版本

支持 EmEditor 9.00 或之後的版本。

# Editor\_RemoveClip

在剪貼簿記錄上的指定位置處刪除文字。您能直接用該內嵌函式或明確地發送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_RemoveClip( HWND hwnd, UINT iPos, UINT nFlags );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_iPos_

> 指定剪貼簿記錄上的位置。

_nFlags_

> 指定要刪除的剪貼簿的格式。
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 剪貼簿格式是標準文字。 |
> | SEL\_TYPE\_LINE | 剪貼簿格式是文字行。 |
> | SEL\_TYPE\_BOX | 剪貼簿格式是文字的垂直選區。 |

## 返回值

> 返回值是剪貼簿記錄上文字被刪除的位置。如果消息沒有成功，返回值是 -1。

## 支持版本

> 支持 EmEditor 9.00 或之後的版本。
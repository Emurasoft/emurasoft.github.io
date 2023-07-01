# Editor\_InsertClip

在剪貼簿記錄上的指定位置處插入文字。您能直接用該內嵌函式或明確地發送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_InsertClip( HWND hwnd, LPCWSTR pszText, UINT iPos, UINT nFlags );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_pszText_

> 指定要插入的文字。

_iPos_

> 在剪貼簿記錄上指定舊的位置。

_nFlags_

> 指定要插入或刪除的剪貼簿的格式。
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_CHAR | 剪貼簿格式是標準文字。 |
> | SEL\_TYPE\_LINE | 剪貼簿格式是文字行。 |
> | SEL\_TYPE\_BOX | 剪貼簿格式是文字的垂直選區。 |

## 返回值

> 返回值是剪貼簿記錄上的新文字被插入的位置處。如果消息失敗，返回值是　－１。

## 支持版本

> 支持 EmEditor 9.00 或之後的版本。

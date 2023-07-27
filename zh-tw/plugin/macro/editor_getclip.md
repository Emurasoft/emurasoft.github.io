# Editor\_GetClip

在剪貼簿記錄中的指定位置處檢索文字。您能直接用該內嵌函式或明確地發送 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
消息。

Editor\_GetClip( HWND hwnd, LPWSTR pszBuf, UINT cchBuf, UINT iPos, UINT\* pnFlags );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pszBuf_

指定接收文字的緩沖區。

_cchBuf_

用字元數指定緩沖區大小，包括終止空字元。

_iPos_

指定剪貼簿記錄中的位置。如果指定的 (單位) 是 -1，那么實際的剪貼簿內容會被檢索而不是剪貼簿記錄中的內容。

_nFlags_

這個值被實際的剪貼簿格式填充。

|     |     |
| --- | --- |
| SEL\_TYPE\_CHAR | 剪貼簿格式是標準文字。 |
| SEL\_TYPE\_LINE | 剪貼簿格式是文字行。 |
| SEL\_TYPE\_BOX | 剪貼簿格式是文字的垂直選區。 |

## 返回值

返回值是 pszBuf 緩沖區大小， 用包括終止空字元在內的需要接收文字的字元數表示。如果消息不成功，返回值是 -1。

## 支持版本

支持 EmEditor 9.00 或之後的版本。

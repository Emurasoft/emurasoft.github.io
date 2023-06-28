# Editor\_GetSelTypeEx

獲得選區狀態的類型。您能直接用該內嵌函式或明確地發送 [EE\_GET\_SEL\_TYPE](../message/ee_get_sel_type) 消息。

Editor\_GetSelTypeEx( HWND hwnd, BOOL bNeedAlways );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_bNeedAlways_

> 如果參數是 TRUE，EE\_GET\_SEL\_TYPE 返回選區狀態的類型即使沒有選取。如果參數是 FALSE，EE\_GET\_SEL\_TYPE 會返回 SEL\_TYPE\_NONE，如果沒有選取。

## 返回值

> 返回一個下列值的組合。SEL\_TYPE\_NONE，SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，和 SEL\_TYPE\_BOX 不能被組合。SEL\_TYPE\_KEYBOARD 和 SEL\_TYPE\_SELECTED 能與其他值組合。如果 bNeedAlways 是 TRUE，并且文字被選取的話，一個用 SEL\_TYPE\_SELECTED 的邏輯總數會被返回。如果 bNeedAlways 是 FALSE，不會使用 SEL\_TYPE\_SELECTED。

> | 值 | 含義 |
> | --- | --- |
> | SEL\_TYPE\_NONE | 沒有選取。 |
> | SEL\_TYPE\_CHAR | 字元被選取。 |
> | SEL\_TYPE\_LINE | 行被選取。 |
> | SEL\_TYPE\_BOX | 方塊被選取。 |
> | SEL\_TYPE\_KEYBOARD | 用鍵盤選取。 |
> | SEL\_TYPE\_SELECTED | 已選取 (當 bNeedAlways = TRUE)。 |

## 支持版本

> 支持 EmEditor 3.00 或之後的版本。然而，bNeedAlways 支持 EmEditor 5.00 或之後的版本。在 5.00 之前的版本中，bNeedAlways 被假定為 FALSE。
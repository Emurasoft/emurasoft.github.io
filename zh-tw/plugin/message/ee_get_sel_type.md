# EE\_GET\_SEL\_TYPE

獲得選區狀態的類型。您能明確地發送該消息或用 [Editor\_GetSelType](../macro/editor_getseltype) 內嵌函式或 [Editor\_GetSelTypeEx](../macro/editor_getseltypeex) 內嵌函式。

EE\_GET\_SEL\_TYPE

wParam = (WPARAM) (BOOL) bNeedAlways;

lParam = (LPARAM)0;

## 參數

_bNeedAlways_

> 如果參數是 TRUE，EE\_GET\_SEL\_TYPE 返回選區狀態的類型，即使沒有選取。如果參數是 FALSE, EE\_GET\_SEL\_TYPE 返回 SEL\_TYPE\_NONE 如果沒有選取的話。

## 返回值

> 返回一個下列值的組合。SEL\_TYPE\_NONE，SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，和 SEL\_TYPE\_BOX 不能被組合。SEL\_TYPE\_KEYBOARD 和 SEL\_TYPE\_SELECTED 能與其他值組合。如果 bNeedAlways 是 TRUE，并且文本被選取的話，一個用 SEL\_TYPE\_SELECTED 的邏輯總數會被返回。如果 bNeedAlways 是 FALSE，不會使用 SEL\_TYPE\_SELECTED。
>
> | 值 | 含義 |
> | --- | --- |
> | SEL\_TYPE\_NONE | 沒有選取。 |
> | SEL\_TYPE\_CHAR | 字符被選取。 |
> | SEL\_TYPE\_LINE | 行被選取。 |
> | SEL\_TYPE\_BOX | 框被選取。 |
> | SEL\_TYPE\_KEYBOARD | 用鍵盤選取。 |
> | SEL\_TYPE\_SELECTED | 已選取 (當 bNeedAlways = TRUE)。 |

## 支持版本

> 支持 EmEditor 3.00 或之後的版本。然而，bNeedAlways 支持 EmEditor 5.00 或之後的版本。在 5.00 之前的版本中，bNeedAlways 被假定為 FALSE。

# Editor\_GetSelType

獲得選區狀態的類型。您能直接用該內嵌函式或明確地發送 [EE\_GET\_SEL\_TYPE](../message/ee_get_sel_type) 消息。

Editor\_GetSelType( HWND hwnd );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

## 返回值

> 返回一個下列值的組合。SEL\_TYPE\_NONE，SEL\_TYPE\_CHAR，SEL\_TYPE\_LINE，和 SEL\_TYPE\_BOX 不能被組合。只有 SEL\_TYPE\_KEYBOARD 能與其他值組合。

> | 值 | 含義 |
> | --- | --- |
> | SEL\_TYPE\_NONE | 沒有選取。 |
> | SEL\_TYPE\_CHAR | 字元被選取。 |
> | SEL\_TYPE\_LINE | 行被選取。 |
> | SEL\_TYPE\_BOX | 方塊被選取。 |
> | SEL\_TYPE\_KEYBOARD | 用鍵盤選取。 |

## 支持版本

> 支持 EmEditor 3.00 或之後的版本。

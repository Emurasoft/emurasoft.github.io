# Editor\_SetSelType

設置選區狀態的類型。您能直接用該內嵌函式或明確地發送
the [EE\_SET\_SEL\_TYPE message](../message/ee_set_sel_type).

Editor\_SetSelType( hwnd, nSelType );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nSelType_

> 您能從如下值中指定一個組合。 However,
> SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, SEL\_TYPE\_BOX cannot be
> combined. Only SEL\_TYPE\_KEYBOARD can be combined with SEL\_TYPE\_NONE,
> SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, or SEL\_TYPE\_BOX.
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_NONE | 沒有選擇。 |
> | SEL\_TYPE\_CHAR | 流選擇模式。 |
> | SEL\_TYPE\_LINE | 行選擇模式。 |
> | SEL\_TYPE\_BOX | 垂直選擇模式。 |
> | SEL\_TYPE\_KEYBOARD | 指定鍵盤選擇模式。這個值能與另一個值進行組合。 |

## 返回值

> 不使用。
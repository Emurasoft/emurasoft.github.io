# Editor\_ShowOutline

顯示或隱藏大綱。您能直接用該內嵌函式或明確地發送 [EE\_SHOW\_OUTLINE](../message/ee_show_outline) 消息。

Editor\_ShowOutline( HWND hwnd, WPARAM nFlags );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nFlags_

> 指定下列值之一。
>
> | 值 | 含義 |
> | --- | --- |
> | SHOW\_OUTLINE\_SHOW | 顯示大綱。 |
> | SHOW\_OUTLINE\_HIDE | 隱藏大綱。 |

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。

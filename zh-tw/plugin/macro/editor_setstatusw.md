# Editor\_SetStatusW

在狀態列上顯示一條 Unicode 消息。您能直接用該內嵌函式或明確地發送 [EE\_SET\_STATUSW](../message/ee_set_statusw) 消息。

Editor\_SetStatusW( HWND hwnd, LPCWSTR szStatus, UINT nFlags = 0 );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_szStatus_

> 指定要顯示在狀態列上的消息文字。

_nFlags_

> 指定以下值的組合。
>
> | 值 | 含義 |
> | --- | --- |
> | STATUS\_FLAG\_NONE | 用正常顏色顯示消息。 |
> | STATUS\_FLAG\_MESSAGE | 用預設亮顯顏色顯示消息。 |
> | STATUS\_FLAG\_WARNING | 用黃色顯示消息。 |
> | STATUS\_FLAG\_ERROR | 用紅色顯示消息。 |
> | STATUS\_FLAG\_ERASE\_SHORTLY | 幾秒鐘後顯示一條消息，然後將其刪除。 |

## 返回值

> 不使用返回值。
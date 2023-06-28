# EE\_SET\_STATUSW

在狀態列上顯示一條 Unicode 消息。您能明確地發送該消息或用 [Editor\_SetStatusW](../macro/editor_setstatusw) 內嵌函式。

EE\_SET\_STATUSW

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szStatus;

## 參數

_szStatus_

> 指定要顯示在狀態列上的消息文本。

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
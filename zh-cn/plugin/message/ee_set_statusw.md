# EE\_SET\_STATUSW

在状态栏上显示一条 Unicode 消息。你能明确地发送该消息或用 [Editor\_SetStatusW](../macro/editor_setstatusw) 内联函数。

EE\_SET\_STATUSW

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szStatus;

## 参数

_szStatus_

> 指定要显示在状态栏上的消息文本。

_nFlags_

> 指定以下值的组合。
>
> | 值 | 含义 |
> | --- | --- |
> | STATUS\_FLAG\_NONE | 用正常颜色显示消息。 |
> | STATUS\_FLAG\_MESSAGE | 用默认高亮颜色显示消息。 |
> | STATUS\_FLAG\_WARNING | 用黄色显示消息。 |
> | STATUS\_FLAG\_ERROR | 用红色显示消息。 |
> | STATUS\_FLAG\_ERASE\_SHORTLY | 几秒钟后显示一条消息，然后将其删除。 |

## 返回值

> 不使用返回值。

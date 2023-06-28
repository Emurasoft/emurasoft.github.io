# Editor\_SetStatusW

在状态栏上显示一条 Unicode 消息。你能直接用该内联函数或明确地发送 [EE\_SET\_STATUSW](../message/ee_set_statusw) 消息。

Editor\_SetStatusW( HWND hwnd, LPCWSTR szStatus, UINT nFlags = 0 );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

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
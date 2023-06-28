# EP\_SYNC\_NOW

如果支持同步功能，则指示插件立即同步。

EP\_SYNC\_NOW

hwnd = hwndView;

wParam = nFlags;

lParam = 0;

## 参数

_hwndView_

> EmEditor 视图的窗口句柄。如果无法确定活动视图，则此值可以为 NULL。

_nFlags_

> 此标志可以包括以下值的组合。SYNC\_SETTINGS\_SEND 和 SYNC\_SETTINGS\_RECEIVE 不能同时指定。
>
> | 值 | 含义 |
> | --- | --- |
> | SYNC\_SETTINGS\_SEND | 插件应发送设置。 |
> | SYNC\_SETTINGS\_RECEIVE | 插件应接收设置。 |
> | SYNC\_FLAG\_FORCE | 即使设置文件的时间戳很旧，插件也应该接收设置。 |
> | SYNC\_FLAG\_REFRESH\_UI | 插件应在收到设置后更新 UI。 |

## 返回值

> 返回值被忽略。

## 版本

> 支持 Version 20.9 或之后的版本。
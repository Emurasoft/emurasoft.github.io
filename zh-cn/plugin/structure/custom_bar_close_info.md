# CUSTOM\_BAR\_CLOSE\_INFO

用于 [EVENT\_CUSTOM\_BAR\_CLOSED 事件](../event/index)。

```
typedef struct _CUSTOM_BAR_CLOSE_INFO {
	UINT nID;
	int iPos;
	DWORD dwFlags;
} CUSTOM_BAR_CLOSE_INFO;
```

## 成员

_nID_

\[in\] 自定义分栏 ID。

_iPos_

\[in\] 在关闭自定义分栏之前的位置。

|     |     |
| --- | --- |
| 0 | 窗口的左边。 |
| 1 | 窗口的顶部。 |
| 2 | 窗口的右边。 |
| 3 | 窗口的底部。 |

_dwFlags_

\[out\] 自定义分栏被关闭的原因。

|     |     |
| --- | --- |
| 0 | 自定义分栏被用户关闭。 |
| CLOSED\_FRAME\_WINDOW | 框架窗口被关闭。 |
| CLOSED\_ANOTHER\_CUSTOM\_BAR | 自定义分栏被关闭因为另一个自定义分栏被打开。 |

## 版本

支持 EmEditor 6.00 或之后的版本。

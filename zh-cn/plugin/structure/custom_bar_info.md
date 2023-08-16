# CUSTOM\_BAR\_INFO

用于 [Editor\_CustomBarOpen](../macro/editor_custombaropen) 内联函数 ( [EE\_CUSTOM\_BAR\_OPEN](../message/ee_custom_bar_open) 消息) 中。

```
typedef struct _CUSTOM_BAR_INFO {
	size_t cbSize;
	HWND hwndCustomBar;
	HWND hwndClient;
	LPCTSTR pszTitle;
	int iPos;
} CUSTOM_BAR_INFO;
```

## 成员

_cbSize_

\[in\] 以字节为单位的数据结构大小。在发送 EE\_CUSTOM\_BAR\_OPEN 消息之前，把这个成员设为 sizeof( CUSTOM\_BAR\_INFO )。

_hwndCustomBar_

\[out\] 当 EE\_CUSTOM\_BAR\_OPEN 消息成功时，到自定义分栏窗口上的句柄会被储存。

_hwndClient_

\[in\] 到客户端窗口上的句柄。

_pszTitle_

\[in\] 用于自定义分栏标题的字符串。

_iPos_

\[in\] 自定义分栏的起始位置。

|     |     |
| --- | --- |
| 0 | 窗口的左边。 |
| 1 | 窗口的顶部。 |
| 2 | 窗口的右边。 |
| 3 | 窗口的底部。 |

## 版本

支持 EmEditor 6.00 或之后的版本。

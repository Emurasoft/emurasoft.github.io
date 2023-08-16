# CUSTOM\_BAR\_INFO

Used by [Editor\_CustomBarOpen](../macro/editor_custombaropen) inline function ( [EE\_CUSTOM\_BAR\_OPEN](../message/ee_custom_bar_open) message).

```
typedef struct _CUSTOM_BAR_INFO {
	size_t cbSize;
	HWND hwndCustomBar;
	HWND hwndClient;
	LPCTSTR pszTitle;
	int iPos;
} CUSTOM_BAR_INFO;
```

## Members

_cbSize_

\[in\] Size of this data structure, in bytes. Set this member to sizeof( CUSTOM\_BAR\_INFO ) before sending the EE\_CUSTOM\_BAR\_OPEN message.

_hwndCustomBar_

\[out\] The handle to the custom bar window will be stored when the EE\_CUSTOM\_BAR\_OPEN message succeeds.

_hwndClient_

\[in\] The handle to the Client window.

_pszTitle_

\[in\] The string used for the custom bar title.

_iPos_

\[in\] The custom bar initial position.

|     |     |
| --- | --- |
| 0 | The left side of the window. |
| 1 | The top of the window. |
| 2 | The right side of the window. |
| 3 | The bottom of the window. |

## Version

Supported on EmEditor Professional Version 6.00 or later.

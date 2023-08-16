# CUSTOM\_BAR\_INFO

用於 [Editor\_CustomBarOpen](../macro/editor_custombaropen) 內嵌函式 ( [EE\_CUSTOM\_BAR\_OPEN](../message/ee_custom_bar_open) 消息) 中。

typedef struct \_CUSTOM\_BAR\_INFO {

size\_t cbSize;

HWND hwndCustomBar;

HWND hwndClient;

LPCTSTR pszTitle;

int iPos;

} CUSTOM\_BAR\_INFO;

## 構成

_cbSize_

\[in\] 以位元為單位的數據結構大小。在發送 EE\_CUSTOM\_BAR\_OPEN 消息之前，把這個成員設為 sizeof( CUSTOM\_BAR\_INFO )。

_hwndCustomBar_

\[out\] 當 EE\_CUSTOM\_BAR\_OPEN 消息成功時，到自訂分欄視窗上的句柄會被儲存。

_hwndClient_

\[in\] 到客戶端視窗上的句柄。

_pszTitle_

\[in\] 用於自訂分欄標題的字符串。

_iPos_

\[in\] 自訂分欄的起始位置。

|     |     |
| --- | --- |
| 0 | 視窗的左邊。 |
| 1 | 視窗的頂部。 |
| 2 | 視窗的右邊。 |
| 3 | 視窗的底部。 |

## 支持版本

支持 EmEditor 6.00 或之後的版本。

# TOOLBAR\_INFO

用於 [Editor\_ToolbarOpen 內嵌函式](../macro/editor_toolbaropen) ( [EE\_TOOLBAR\_OPEN 消息](../message/ee_toolbar_open)) 以及與自訂工具列相關的事件中。

typedef struct \_TOOLBAR\_INFO {

size\_t cbSize;

HWND hwndRebar;

HWND hwndClient;

LPCTSTR pszTitle;

UINT nMask;

UINT nID;

UINT nFlags;

UINT fStyle;

UINT cxMinChild;

UINT cyMinChild;

UINT cx;

UINT cxIdeal;

UINT nBand;

WORD wPlugInCmdID;

} TOOLBAR\_INFO;

## 構成

_cbSize_

> 用位元數表示該數據結構的大小。把這個構成部分設為 sizeof( TOOLBAR\_INFO ) 在發送 TOOLBAR\_INFO 消息前。

_hwndRebar_

> EmEditor 存儲處理到 rebar 視窗中當在 EE\_TOOLBAR\_OPEN 消息處理器中創建工具列時。

_hwndClient_

> 指定客戶端工具列視窗的處理。

_pszTitle_

> 指定工具列的標題字符串。

_nMask_

> 指定下列值的組合。
>
> |     |     |
> | --- | --- |
> | TIM\_REBAR | hwndRebar 參數有效。 |
> | TIM\_CLIENT | hwndClient 參數有效。 |
> | TIM\_TITLE | pszTitle 參數有效。 |
> | TIM\_ID | nID 參數有效。 |
> | TIM\_FLAGS | nFlags 參數有效。 |
> | TIM\_STYLE | fStyle 參數有效。 |
> | TIM\_MINCHILD | cxMinChild 和 cyMinChild 參數有效。 |
> | TIM\_CX | cx 參數有效。 |
> | TIM\_CXIDEAL | cxIdeal 參數有效。 |
> | TIM\_BAND | nBand 參數有效。 |
> | TIM\_PLUG\_IN\_CMD\_ID | wPlugInCmdID 參數有效。 |

_nID_

> 為工具列指定一個 ID。

_nFlags_

> 工具列被關閉的原因。
>
> |     |     |
> | --- | --- |
> | 0 | 工具列被用戶關閉。 |
> | CLOSED\_FRAME\_WINDOW | 框架視窗被關閉。 |

_fStyle_

> 指定區段樣式的標志。包括 RBBS\_HIDDEN 來隱藏工具列。這個參數與 REBARBANDINFO 結構中的 fStyle 參數相同。

_cxMinChild_

> 用像素表示子視窗的最小寬度。這個參數與 REBARBANDINFO 結構中的 cxMinChild 參數相同。

_cyMinChild_

> 用像素表示子視窗的最小高度。這個參數與 REBARBANDINFO 結構中的 cyMinChild 參數相同。

_cx_

> 用像素表示區段長度。這個參數與 REBARBANDINFO 結構中的 cx 參數相同。

_cxIdeal_

> 用像素表示理想的區段寬度。這個參數與 REBARBANDINFO 結構中的 cxIdeal 參數相同。

_nBand_

> 插入區段位置處的已零為基準的索引。如果您把這個參數設為 -1，rebar 控制會添加新的區段在最后的位置處。

_wPlugInCmdID_

> 該外掛程式的命令 ID。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。
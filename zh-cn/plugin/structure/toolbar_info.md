# TOOLBAR\_INFO

用于 [Editor\_ToolbarOpen 内联函数](../macro/editor_toolbaropen) ( [EE\_TOOLBAR\_OPEN 消息](../message/ee_toolbar_open)) 以及与自定义工具栏相关的事件中。

```
typedef struct _TOOLBAR_INFO {
	size_t cbSize;
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
} TOOLBAR_INFO;
```

## 成员

_cbSize_

用字节数表示该数据结构的大小。把这个构成部分设为 sizeof( TOOLBAR\_INFO ) 在发送 TOOLBAR\_INFO 消息前。

_hwndRebar_

EmEditor 存储处理到 rebar 窗口中当在 EE\_TOOLBAR\_OPEN 消息处理器中创建工具栏时。

_hwndClient_

指定客户端工具栏窗口的处理。

_pszTitle_

指定工具栏的标题字符串。

_nMask_

指定下列值的组合。

|     |     |
| --- | --- |
| TIM\_REBAR | hwndRebar 参数有效。 |
| TIM\_CLIENT | hwndClient 参数有效。 |
| TIM\_TITLE | pszTitle 参数有效。 |
| TIM\_ID | nID 参数有效。 |
| TIM\_FLAGS | nFlags 参数有效。 |
| TIM\_STYLE | fStyle 参数有效。 |
| TIM\_MINCHILD | cxMinChild 和 cyMinChild 参数有效。 |
| TIM\_CX | cx 参数有效。 |
| TIM\_CXIDEAL | cxIdeal 参数有效。 |
| TIM\_BAND | nBand 参数有效。 |
| TIM\_PLUG\_IN\_CMD\_ID | wPlugInCmdID 参数有效。 |

_nID_

为工具栏指定一个 ID。

_nFlags_

工具栏被关闭的原因。

|     |     |
| --- | --- |
| 0 | 工具栏被用户关闭。 |
| CLOSED\_FRAME\_WINDOW | 框架窗口被关闭。 |

_fStyle_

指定区段样式的标志。包括 RBBS\_HIDDEN 来隐藏工具栏。这个参数与 REBARBANDINFO 结构中的 fStyle 参数相同。

_cxMinChild_

用像素表示子窗口的最小宽度。这个参数与 REBARBANDINFO 结构中的 cxMinChild 参数相同。

_cyMinChild_

用像素表示子窗口的最小高度。这个参数与 REBARBANDINFO 结构中的 cyMinChild 参数相同。

_cx_

用像素表示区段长度。这个参数与 REBARBANDINFO 结构中的 cx 参数相同。

_cxIdeal_

用像素表示理想的区段宽度。这个参数与 REBARBANDINFO 结构中的 cxIdeal 参数相同。

_nBand_

插入区段位置处的已零为基准的索引。如果你把这个参数设为 -1，rebar 控制会添加新的区段在最后的位置处。

_wPlugInCmdID_

该插件的命令 ID。

## 版本

支持 EmEditor 7.00 或之后的版本。

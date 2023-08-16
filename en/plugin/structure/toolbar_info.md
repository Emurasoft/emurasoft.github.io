# TOOLBAR\_INFO

Used by [Editor\_ToolbarOpen inline function](../macro/editor_toolbaropen) ( [EE\_TOOLBAR\_OPEN message](../message/ee_toolbar_open)) and events related to custom toolbars.

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

## Members

_cbSize_

Size of this data structure, in bytes. Set this member to sizeof( TOOLBAR\_INFO ) before sending the TOOLBAR\_INFO message.

_hwndRebar_

EmEditor stores the handle to the rebar window when the toolbar is created inside the EE\_TOOLBAR\_OPEN message handler.

_hwndClient_

Specifies the handle to the client toolbar window.

_pszTitle_

Specifies a title string for the toolbar.

_nMask_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| TIM\_REBAR | hwndRebar parameter is valid. |
| TIM\_CLIENT | hwndClient parameter is valid. |
| TIM\_TITLE | pszTitle parameter is valid. |
| TIM\_ID | nID parameter is valid. |
| TIM\_FLAGS | nFlags parameter is valid. |
| TIM\_STYLE | fStyle parameter is valid. |
| TIM\_MINCHILD | cxMinChild and cyMinChild parameters are valid. |
| TIM\_CX | cx parameter is valid. |
| TIM\_CXIDEAL | cxIdeal parameter is valid. |
| TIM\_BAND | nBand parameter is valid. |
| TIM\_PLUG\_IN\_CMD\_ID | wPlugInCmdID parameter is valid. |

_nID_

Specifies an ID for the toolbar.

_nFlags_

The reason that the toolbar is closed.

|     |     |
| --- | --- |
| 0 | The toolbar is closed by a user. |
| CLOSED\_FRAME\_WINDOW | The frame window is being closed. |

_fStyle_

Flags that specify the band style. Include RBBS\_HIDDEN to hide the toolbar. This parameter is identical to the fStyle parameter of the REBARBANDINFO structure.

_cxMinChild_

Minimum width of the child window, in pixels. This parameter is identical to the cxMinChild parameter of the REBARBANDINFO structure.

_cyMinChild_

Minimum height of the child window, in pixels. This parameter is identical to the cyMinChild parameter of the REBARBANDINFO structure.

_cx_

Length of the band, in pixels. This parameter is identical to the cx parameter of the REBARBANDINFO structure.

_cxIdeal_

Ideal width of the band, in pixels. This parameter is identical to the cxIdeal parameter of the REBARBANDINFO structure.

_nBand_

Zero-based index of the location where the band will be inserted. If you set this parameter to -1, the rebar control will add the new band at the last location.

_wPlugInCmdID_

The command ID of the plug-in.

## Version

Supported on Version 7.00 or later.

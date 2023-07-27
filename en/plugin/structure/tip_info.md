# TIP\_INFO

Used by [EE\_SHOW\_TIP](../message/ee_show_tip) message.

typedef struct \_TIP\_INFO {

UINT cbSize;

LPCWSTR pszTip;

POINT\_PTR ptCaret;

POINT ptDev;

UINT nFlags;

} TIP\_INFO;

## Members

_cbSize_

Size of this data structure, in bytes. Set this member to sizeof( TIP\_INFO ) before sending the [EE\_SHOW\_TIP](../message/ee_show_tip) message.

_pszTip_

Specifies the text to display in the tooltip. The length of the text must be no more than 3,999 characters long. The string may include clickable text specified in this form: "<a href="url">clickable text</a>".

_ptCaret_

Currently not used.

_ptDev_

Currently not used.

_nFlags_

Specifies one of the following values.

|     |     |
| --- | --- |
| SHOW\_TIP\_ACTIVE\_STRING | Displays the tooltip at the active string where the mouse pointer is hovered. |
| SHOW\_TIP\_CURRENT\_CARET | Displays the tooltip at the caret position. |
| SHOW\_TIP\_CURRENT\_MOUSE | Displays the tooltip at the mouse pointer position. |
| SHOW\_TIP\_HIDE | Hides the tooltip if already displayed. |

## Version

Supported on Version 16.9 or later.

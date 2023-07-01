# CUSTOM\_BAR\_CLOSE\_INFO

Used by [EVENT\_CUSTOM\_BAR\_CLOSED event](../event/index).

typedef struct \_CUSTOM\_BAR\_CLOSE\_INFO {

UINT nID;

int iPos;

DWORD dwFlags;

} CUSTOM\_BAR\_CLOSE\_INFO;

## Members

_nID_

> \[in\] The custom bar ID.

_iPos_

> \[in\] The position of the custom bar immediately before it is closed.
>
> |     |     |
> | --- | --- |
> | 0 | The left side of the window. |
> | 1 | The top of the window. |
> | 2 | The right side of the window. |
> | 3 | The bottom of the window. |

_dwFlags_

> \[out\] The reason that the custom bar is closed.
>
> |     |     |
> | --- | --- |
> | 0 | The custom bar is closed by a user. |
> | CLOSED\_FRAME\_WINDOW | The frame window is being closed. |
> | CLOSED\_ANOTHER\_CUSTOM\_BAR | The custom bar is closed because another custom bar is opened. |

## Version

> Supported on EmEditor Professional Version 6.00 or later.

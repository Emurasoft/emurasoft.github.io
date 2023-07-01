# CUSTOM\_BAR\_CLOSE\_INFO

用於 [EVENT\_CUSTOM\_BAR\_CLOSED 事件](../event/index)。

typedef struct \_CUSTOM\_BAR\_CLOSE\_INFO {

UINT nID;

int iPos;

DWORD dwFlags;

} CUSTOM\_BAR\_CLOSE\_INFO;

## 構成

_nID_

> \[in\] 自訂分欄 ID。

_iPos_

> \[in\] 在關閉自訂分欄之前的位置。
>
> |     |     |
> | --- | --- |
> | 0 | 視窗的左邊。 |
> | 1 | 視窗的頂部。 |
> | 2 | 視窗的右邊。 |
> | 3 | 視窗的底部。 |

_dwFlags_

> \[out\] 自訂分欄被關閉的原因。
>
> |     |     |
> | --- | --- |
> | 0 | 自訂分欄被用戶關閉。 |
> | CLOSED\_FRAME\_WINDOW | 框架視窗被關閉。 |
> | CLOSED\_ANOTHER\_CUSTOM\_BAR | 自訂分欄被關閉因為另一個自訂分欄被打開。 |

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。

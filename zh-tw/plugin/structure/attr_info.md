# ATTR\_INFO

Used by [EE\_GET\_ATTR](../message/ee_get_attr) message.

typedef struct \_ATTR\_INFO {

size\_t cbSize; // in

POINT\_PTR ptLogical; // in

UINT nFlags; // in

UINT nAttr; // out

WCHAR szConfigScope\[MAX\_CONFIG\_NAME\]; // out

WCHAR szConfigDoc\[MAX\_CONFIG\_NAME\]; // out

} ATTR\_INFO;

## 構成

_cbSize_

> \[In\] 以位元為單位的數據結構大小。在發送 [EE\_GET\_ATTR](../message/ee_get_attr) 消息之前，把這個成員設為sizeof ( ATTR\_INFO )。

_ptLogical_

> \[In\] 指定邏輯坐標中信息能被檢索的位置。

_nFlags_

> \[In\] 從如下值中指定一個組合。
>
> |     |     |
> | --- | --- |
> | AI\_NEED\_CONFIG\_SCOPE | 需要配置名稱 (範圍) 在活動文檔上的指定位置處。 |
> | AI\_NEED\_CONFIG\_DOC | 需要為活動文檔選取的配置名稱。 |
> | AI\_NEED\_ATTR\_SUB | 保存由 nID 指定的臨時文本。 |
> | AI\_NEED\_ALL | 需要以上全部信息。 |

_nAttr_

> \[Out\] 該成員包含下列值之一。
>
> |     |     |
> | --- | --- |
> | ATTR\_NONE | 標準文本。 |
> | ATTR\_COMMENT | 一個注釋。 |
> | ATTR\_DOUBLE\_QUOTE | 在雙引號內。 |
> | ATTR\_SINGLE\_QUOTE | 在單引號內。 |
> | ATTR\_TAG | 在一個標簽內。 |

_pszConfigScope_

> \[Out\] 該成員包含配置名稱 (範圍) 在活動文檔上指定位置處，如果 nFlags 包含 AI\_NEED\_CONFIG\_SCOPE。

_pszConfigDoc_

> \[Out\] 該成員包含為活動文檔選取的配置名稱如果 nFlags 包含 AI\_NEED\_CONFIG\_DOC。

## 支持版本

> 支持 EmEditor 9.00 或之後的版本。

# ATTR\_INFO

用于 [EE\_GET\_ATTR](../message/ee_get_attr) 消息。

typedef struct \_ATTR\_INFO {

size\_t cbSize; // in

POINT\_PTR ptLogical; // in

UINT nFlags; // in

UINT nAttr; // out

WCHAR szConfigScope\[MAX\_CONFIG\_NAME\]; // out

WCHAR szConfigDoc\[MAX\_CONFIG\_NAME\]; // out

} ATTR\_INFO;

## 成员

_cbSize_

> \[In\] 以字节为单位的数据结构大小。在发送 [EE\_GET\_ATTR](../message/ee_get_attr) 消息之前，把这个成员设为sizeof ( ATTR\_INFO )。

_ptLogical_

> \[In\] 指定逻辑坐标中信息能被检索的位置。

_nFlags_

> \[In\] 指定一个下列值的组合。
>
> |     |     |
> | --- | --- |
> | AI\_NEED\_CONFIG\_SCOPE | 需要配置名称（范围）在活动文档上的指定位置处。 |
> | AI\_NEED\_CONFIG\_DOC | 需要为活动文档选取的配置名称。 |
> | AI\_NEED\_ATTR\_SUB | 保存由 nID 指定的临时文本。 |
> | AI\_NEED\_ALL | 需要以上全部信息。 |

_nAttr_

> \[Out\] 该成员包含下列值之一。
>
> |     |     |
> | --- | --- |
> | ATTR\_NONE | 标准文本。 |
> | ATTR\_COMMENT | 一个注释。 |
> | ATTR\_DOUBLE\_QUOTE | 在双引号内。 |
> | ATTR\_SINGLE\_QUOTE | 在单引号内。 |
> | ATTR\_TAG | 在一个标签内。 |

_pszConfigScope_

> \[Out\] 该成员包含配置名称（范围）在活动文档上指定位置处，如果 nFlags 包含 AI\_NEED\_CONFIG\_SCOPE。

_pszConfigDoc_

> \[Out\] 该成员包含为活动文档选取的配置名称如果 nFlags 包含 AI\_NEED\_CONFIG\_DOC。

## 版本

> 支持 EmEditor 9.00 或之后的版本。

# GET\_COLOR\_INFO

用于 [EE\_GET\_COLOR](../message/ee_get_color) 消息。

typedef struct \_GET\_COLOR\_INFO {

UINT cbSize;

BOOL bFind;

UINT nIndex;

COLORREF clrText;

COLORREF clrBack;

int nAttr;

} GET\_COLOR\_INFO;

## Fields

_cbSize_

> \[In\] 以字节为单位的数据结构大小。在发送 [EE\_GET\_COLOR](../message/ee_get_color) 消息之前，把该成员设为 sizeof( GET\_COLOR\_INFO )。

_bFind_

> \[in\] 指定 TRUE 如果检索查找的颜色，或 FALSE 如果检索其他部分的颜色。

_nIndex_

> \[in\] 指定索引来检索颜色。如果 bFind 是 FALSE，索引必须低于 MAX\_SMART\_COLOR。

_clrText_

> \[out\] 该成员包含文本颜色在从 [EE\_GET\_COLOR](../message/ee_get_color) 消息返回后。该值可以是一个颜色的 RGB 值或下列的值之一。
>
> |     |     |
> | --- | --- |
> | DEFAULT\_COLOR | 使用 Windows 系统颜色。 |
> | TRANSPARENT\_COLOR | 颜色是透明的。 |

_clrBack_

> \[out\] 该成员包含背景颜色在从 [EE\_GET\_COLOR](../message/ee_get_color) 消息返回后。该值可以是一个颜色的 RGB 值或下列的值之一。
>
> |     |     |
> | --- | --- |
> | DEFAULT\_COLOR | 使用 Windows 系统颜色。 |
> | TRANSPARENT\_COLOR | 颜色是透明的。 |

_nAttr_

> \[out\] 该成员包含样式在从 [EE\_GET\_COLOR](../message/ee_get_color) 消息返回后。该值可以是一个颜色的 RGB 值或下列的值之一。
>
> |     |     |
> | --- | --- |
> | SMART\_COLOR\_FONT\_NORMAL | 字体为标准。 |
> | SMART\_COLOR\_FONT\_UNDERLINE | 字体带下划线。 |
> | SMART\_COLOR\_FONT\_BOLD | 字体是粗体。 |
> | SMART\_COLOR\_FONT\_ITALIC | 字体是斜体。 |
> | SMART\_COLOR\_FONT\_WIGGLY | 字体弯曲。 |
> | SMART\_COLOR\_FONT\_DOTTED | 如果是行，指定的行带虚线。 |

## 支持版本

> 支持 EmEditor 14.4 或之后的版本。
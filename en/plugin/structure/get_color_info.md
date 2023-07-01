# GET\_COLOR\_INFO

Used by [EE\_GET\_COLOR](../message/ee_get_color) messages.

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

> \[In\] Size of this data structure, in bytes. Set this member to sizeof( GET\_COLOR\_INFO ) before sending the [EE\_GET\_COLOR](../message/ee_get_color) message.

_bFind_

> \[in\] Specifies TRUE if retrieving colors for Find, or FALSE if retrieving colors for one of other parts.

_nIndex_

> \[in\] Specifies the index to retrieve colors. If bFind is FALSE, the index must be less than MAX\_SMART\_COLOR.

_clrText_

> \[out\] This member contains the text color after returning from the [EE\_GET\_COLOR](../message/ee_get_color) message. The value can be an RGB value of the color or one of the following values.
>
> |     |     |
> | --- | --- |
> | DEFAULT\_COLOR | The Windows system color is used. |
> | TRANSPARENT\_COLOR | The color is transparent. |

_clrBack_

> \[out\] This member contains the background color after returning from the [EE\_GET\_COLOR](../message/ee_get_color) message. The value can be an RGB value of the color or one of the following values.
>
> |     |     |
> | --- | --- |
> | DEFAULT\_COLOR | The Windows system color is used. |
> | TRANSPARENT\_COLOR | The color is transparent. |

_nAttr_

> \[out\] This member contains the style after returning from the [EE\_GET\_COLOR](../message/ee_get_color) message. The value is one of the following values.
>
> |     |     |
> | --- | --- |
> | SMART\_COLOR\_FONT\_NORMAL | The font is normal. |
> | SMART\_COLOR\_FONT\_UNDERLINE | The font is underlined. |
> | SMART\_COLOR\_FONT\_BOLD | The font is bold. |
> | SMART\_COLOR\_FONT\_ITALIC | The font is italic. |
> | SMART\_COLOR\_FONT\_WIGGLY | The font is wiggly. |
> | SMART\_COLOR\_FONT\_DOTTED | In case of lines, the specified lines are dotted. |

## Version

> Supported on Version 14.4 or later.

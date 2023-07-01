# Editor\_GetColor

Retrieves the text and background colors and style for the specified part. You can use this inline function or explicitly send the [EE\_GET\_COLOR](../message/ee_get_color) message.

Editor\_GetColor( HWND hwnd, BOOL bFind, UINT nIndex, COLORREF\* pclrText, COLORREF\* pclrBack, int\* pnAttr );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_bFind_

> Specifies TRUE if retrieving colors for Find, or FALSE if retrieving colors for one of other parts.

_nIndex_

> Specifies the index to retrieve colors. If bFind is FALSE, the index must be less than MAX\_SMART\_COLOR.

_pclrText_

> Specifies a pointer to retrieve the text color. It is an RGB value of the color or one of the following values.
>
> |     |     |
> | --- | --- |
> | DEFAULT\_COLOR | The Windows system color is used. |
> | TRANSPARENT\_COLOR | The color is transparent. |

_pclrBack_

> Specifies a pointer to retrieve the background color. It is an RGB value of the color or one of the following values.
>
> |     |     |
> | --- | --- |
> | DEFAULT\_COLOR | The Windows system color is used. |
> | TRANSPARENT\_COLOR | The color is transparent. |

_pnAttr_

> Specifies a pointer to retrieve the style. It is one of the following values.
>
> |     |     |
> | --- | --- |
> | SMART\_COLOR\_FONT\_NORMAL | The font is normal. |
> | SMART\_COLOR\_FONT\_UNDERLINE | The font is underlined. |
> | SMART\_COLOR\_FONT\_BOLD | The font is bold. |
> | SMART\_COLOR\_FONT\_ITALIC | The font is italic. |
> | SMART\_COLOR\_FONT\_WIGGLY | The font is wiggly. |
> | SMART\_COLOR\_FONT\_DOTTED | In case of lines, the specified lines are dotted. |

## Return Values

> The return value is TRUE if succeeded, or FALSE if failed.

## Version

> Supported on Version 14.4 or later.

# Editor\_GetColor

检索指定部分的文本、背景颜色以及样式。你能用内联函数或直接送出 [EE\_GET\_COLOR](../message/ee_get_color) 信息。

Editor\_GetColor( HWND hwnd, BOOL bFind, UINT nIndex, COLORREF\* pclrText, COLORREF\* pclrBack, int\* pnAttr );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_bFind_

指定 TRUE 如果检索的颜色是查找颜色；如果检索的是其他部分的颜色，指定 FALSE。

_nIndex_

指定要检索颜色的索引。如果 bFind 是 FALSE，那么索引一定小于 MAX\_SMART\_COLOR 值。

_pclrText_

指定一个指针来检索文本颜色。它可以是一个 RGB 值或下列的值之一。

|     |     |
| --- | --- |
| DEFAULT\_COLOR | 使用 Windows 系统颜色。 |
| TRANSPARENT\_COLOR | 颜色透明。 |

_pclrBack_

指定一个指针来检索背景颜色。它可以是一个 RGB 值或下列的值之一。

|     |     |
| --- | --- |
| DEFAULT\_COLOR | 使用 Windows 系统颜色。 |
| TRANSPARENT\_COLOR | 颜色透明。 |

_pnAttr_

指定一个要检索样式的指针。它可以是下列的值之一。

|     |     |
| --- | --- |
| SMART\_COLOR\_FONT\_NORMAL | 字体为标准。 |
| SMART\_COLOR\_FONT\_UNDERLINE | 字体带下划线。 |
| SMART\_COLOR\_FONT\_BOLD | 字体是粗体。 |
| SMART\_COLOR\_FONT\_ITALIC | 字体是斜体。 |
| SMART\_COLOR\_FONT\_WIGGLY | 字体弯曲。 |
| SMART\_COLOR\_FONT\_DOTTED | 如果是行，指定的行带虚线。 |

## 返回值

返回值是 TRUE 如果通过的话，或 FALSE 如果未通过的话。

## 支持版本

支持 EmEditor 14.4 或之后的版本。

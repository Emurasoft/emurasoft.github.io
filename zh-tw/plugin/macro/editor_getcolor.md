# Editor\_GetColor

檢索指定部分的文字、背景顏色以及樣式。您能用內嵌函式或直接送出 [EE\_GET\_COLOR](../message/ee_get_color) 信息。

Editor\_GetColor( HWND hwnd, BOOL bFind, UINT nIndex, COLORREF\* pclrText, COLORREF\* pclrBack, int\* pnAttr );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_bFind_

指定 TRUE 如果檢索的顏色是尋找顏色；如果檢索的是其他部分的顏色，指定 FALSE。

_nIndex_

指定要檢索顏色的索引。如果 bFind 是 FALSE，那么索引一定小于 MAX\_SMART\_COLOR 值。

_pclrText_

指定一個指標來檢索文字顏色。它可以是一個 RGB 值或下列的值之一。

|     |     |
| --- | --- |
| DEFAULT\_COLOR | 使用 Windows 系統顏色。 |
| TRANSPARENT\_COLOR | 顏色透明。 |

_pclrBack_

指定一個指標來檢索背景顏色。它可以是一個 RGB 值或下列的值之一。

|     |     |
| --- | --- |
| DEFAULT\_COLOR | 使用 Windows 系統顏色。 |
| TRANSPARENT\_COLOR | 顏色透明。 |

_pnAttr_

指定一個要檢索樣式的指標。它可以是下列的值之一。

|     |     |
| --- | --- |
| SMART\_COLOR\_FONT\_NORMAL | 字型為標準。 |
| SMART\_COLOR\_FONT\_UNDERLINE | 字型帶下劃線。 |
| SMART\_COLOR\_FONT\_BOLD | 字型是粗體。 |
| SMART\_COLOR\_FONT\_ITALIC | 字型是斜體。 |
| SMART\_COLOR\_FONT\_WIGGLY | 字型彎曲。 |
| SMART\_COLOR\_FONT\_DOTTED | 如果是行，指定的行帶虛線。 |

## 返回值

返回值是 TRUE 如果通過的話，或 FALSE 如果未通過的話。

## 支持版本

支持 EmEditor 14.4 或之後的版本。

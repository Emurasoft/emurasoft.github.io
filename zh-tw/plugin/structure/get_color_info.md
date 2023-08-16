# GET\_COLOR\_INFO

用於 [EE\_GET\_COLOR](../message/ee_get_color) 消息。

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

\[In\] 以位元為單位的數據結構大小。在發送 [EE\_GET\_COLOR](../message/ee_get_color) 消息之前，把該成員設為 sizeof( GET\_COLOR\_INFO )。

_bFind_

\[in\] 指定 TRUE 如果檢索查找的顏色，或 FALSE 如果檢索其他部分的顏色。

_nIndex_

\[in\] 指定索引來檢索顏色。如果 bFind 是 FALSE，索引必須低于 MAX\_SMART\_COLOR。

_clrText_

\[out\] 該成員包含文本顏色在從 [EE\_GET\_COLOR](../message/ee_get_color) 消息返回后。該值可以是一個顏色的 RGB 值或下列的值之一。

|     |     |
| --- | --- |
| DEFAULT\_COLOR | 使用 Windows 系統顏色。 |
| TRANSPARENT\_COLOR | 顏色是透明的。 |

_clrBack_

\[out\] 該成員包含背景顏色在從 [EE\_GET\_COLOR](../message/ee_get_color) 消息返回后。該值可以是一個顏色的 RGB 值或下列的值之一。

|     |     |
| --- | --- |
| DEFAULT\_COLOR | 使用 Windows 系統顏色。 |
| TRANSPARENT\_COLOR | 顏色是透明的。 |

_nAttr_

\[out\] 該成員包含樣式在從 [EE\_GET\_COLOR](../message/ee_get_color) 消息返回后。該值可以是一個顏色的 RGB 值或下列的值之一。

|     |     |
| --- | --- |
| SMART\_COLOR\_FONT\_NORMAL | 字體為標準。 |
| SMART\_COLOR\_FONT\_UNDERLINE | 字體帶下劃線。 |
| SMART\_COLOR\_FONT\_BOLD | 字體是粗體。 |
| SMART\_COLOR\_FONT\_ITALIC | 字體是斜體。 |
| SMART\_COLOR\_FONT\_WIGGLY | 字體彎曲。 |
| SMART\_COLOR\_FONT\_DOTTED | 如果是行，指定的行帶虛線。 |

## 支持版本

支持 EmEditor 14.4 或之後的版本。

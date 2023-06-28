# EE\_ENUM\_HIGHLIGHT

列舉高亮的字符串。您能明確地發送該消息或用 [Editor\_EnumHighlight](../macro/editor_enumhighlight) 內嵌函式。

EE\_ENUM\_HIGHLIGHT

wParam = (WPARAM) (size\_t) cchBuf;

lParam = (LPARAM) (LPWSTR) pBuf;

## 參數

_cchBuf_

> 用字符數指定緩沖區大小。要注意的是兩個空字符會被添加到高亮字符串列表末尾。如果指定的數值為 0，該消息會返回需要檢索高亮字符串列表的大小。

_pBuf_

> 指定指針指向緩沖區來檢索高亮字符串列表。在這個緩沖區內，由一個空字符分隔的可用的高亮字符串列表會被檢索。兩個空字符會被添加到高亮字符串列表末尾。如果指定的數值為 0，pBuf 是空 (NULL)。
>
> 每一個字符串的第一個字符代表顏色和下列值的組合。
>
> |     |     |
> | --- | --- |
> | 從 0 到 9 | 顏色。用 HIGHLIGHT\_COLOR\_MASK 作為掩碼。 |
> | HIGHLIGHT\_WORD | 全詞匹配時高亮。 |
> | HIGHLIGHT\_RIGHT\_SIDE | 高亮到選定單詞右側。 |
> | HIGHLIGHT\_INSIDE\_TAG | 僅在標記內。 |
> | HIGHLIGHT\_REG\_EXP | 規則運算式。 |
> | HIGHLIGHT\_CASE | 匹配大小寫。 |
> | HIGHLIGHT\_RIGHT\_ALL | 高亮單詞與其右側區域。 |

## 返回值

> 返回值是檢索高亮字符串列表的必需大小。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。
# Editor\_EnumHighlight

列舉亮顯的字串。您能直接用該內嵌函式或明確地發送 [EE\_ENUM\_HIGHLIGHT](../message/ee_enum_highlight) 消息。

Editor\_EnumHighlight( HWND hwnd, LPWSTR pBuf, size\_t cchBuf );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_cchBuf_

> 用字元數指定緩沖區大小。要注意的是兩個空字元會被添加到亮顯字串清單末尾。如果指定的數值為 0，該消息會返回需要檢索亮顯字串清單的大小。

_pBuf_

> 指定指標至緩沖區來檢索亮顯字串清單。在這個緩沖區內，由一個空字元分隔的可用的亮顯字串清單會被檢索。兩個空字元會被添加到亮顯字串清單末尾。如果指定的數值為 0，pBuf 是空 (NULL)。
>
> The first character of each string represents the color and a combination of the following values.
>
> |     |     |
> | --- | --- |
> | 從 0 到 9 | 顏色。用 HIGHLIGHT\_COLOR\_MASK 作為掩碼。 |
> | HIGHLIGHT\_WORD | 全詞符合時亮顯 |
> | HIGHLIGHT\_RIGHT\_SIDE | 亮顯到選定單字右側。 |
> | HIGHLIGHT\_INSIDE\_TAG | 僅在標記內。 |
> | HIGHLIGHT\_REG\_EXP | 規則運算式。 |
> | HIGHLIGHT\_CASE | 符合大小寫。 |
> | HIGHLIGHT\_RIGHT\_ALL | 亮顯單字與其右側區域。 |

## 返回值

> 返回值是檢索亮顯字串清單的必需大小。

## 支持版本

> 支持 EmEditor 7.00 或之後的版本。
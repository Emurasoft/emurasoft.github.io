# EE\_CONVERT

轉換字符。您能明確地發送該消息或用
[Editor\_Convert](../macro/editor_convert) 內嵌函式。

EE\_CONVERT

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szChars;

## 參數

_nFlags_

您能指定下列數值的組合。

| 值 | 含義 |
| --- | --- |
| FLAG\_MAKE\_LOWER | 轉換為小寫字符。 |
| FLAG\_MAKE\_UPPER | 轉換為大寫字符。 |
| FLAG\_HAN\_TO\_ZEN | 轉換為全角字符。 |
| FLAG\_ZEN\_TO\_HAN. | 轉換為半角字符。 |
| FLAG\_CAPITALIZE | 每一個單詞的首字母大寫。 |
| FLAG\_MAKE\_LOWER\_L | 轉換為小寫字元（與地區設定相關）。 |
| FLAG\_MAKE\_UPPER\_L | 轉換為大寫字元（與地區設定相關）。 |
| FLAG\_CAPITALIZE\_L | 將每個單字的首字母大寫（與地區設定相關）。 |
| FLAG\_CONVERT\_SELECT\_ALL | 轉換整個文本。如果沒有設置該標志，EE\_CONVERT 僅轉換選區內的字符。 |
| FLAG\_CONVERT\_KATA | 轉換片假名。 |
| FLAG\_CONVERT\_ALPHANUMERIC | 轉換字母和數字字符。 |
| FLAG\_CONVERT\_MARK | 轉換標記。 |
| FLAG\_CONVERT\_SPACE | 轉換空白。 |
| FLAG\_CONVERT\_KANA\_MARK | 轉換假名標記。 |
| FLAG\_CONVERT\_CUSTOM | 當指定 FLAG\_HAN\_TO\_ZEN 或 FLAG\_ZEN\_TO\_HAN 時，szChars 參數指定應轉換哪些單個字元。如果指定了此值，則還必須指定 szChars 參數，並忽略 FLAG\_CONVERT\_KATA，FLAG\_CONVERT\_ALPHANUMERIC，FLAG\_CONVERT\_MARK，FLAG\_CONVERT\_SPACE，FLAG\_CONVERT\_KANA\_MARK 的值。 |
| FLAG\_JAPANESE\_YEN | 將 U+005C（反斜線）轉換為 U+FFE5（全形日幣標記），反之亦然。 |
| FLAG\_KOREAN\_WON | 將 U+005C（反斜線）轉換為 U+FFE6（全形韓幣標記），反之亦然。 |
| FLAG\_RIGHT\_SINGLE\_QUOTATION | 將 U+0027（縮寫符號）轉換為 U+2019（右單引號），反之亦然。 |
| FLAG\_RIGHT\_DOUBLE\_QUOTATION | 將 U+0022（引號）轉換為 U+201D（右雙引號），反之亦然。 |

_szChars_

如果指定了 FLAG\_CONVERT\_CUSTOM，則可以設定要轉換的單個全形字元的組合。 如果不使用，請將此參數設定為 NULL。

## 返回值

如果消息成功，返回值為非零值。如果該消息不成功，返回值為零。

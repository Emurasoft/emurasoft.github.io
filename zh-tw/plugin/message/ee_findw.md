# EE\_FINDW

搜尋一個 Unicode 字符串。您能明確地發送該消息或用
the [Editor\_FindW](../macro/editor_findw) 內嵌函式。

EE\_FINDW

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szFind;

## 參數

_nFlags_

您能從如下值中指定一個組合。

| 值 | 含義 |
| --- | --- |
| FLAG\_FIND\_AROUND | 移動到文本的開始/結束處。 |
| FLAG\_FIND\_BOOKMARK | 在有匹配的字符串的行上設置書簽。 |
| FLAG\_FIND\_CASE | 區分大小寫。 |
| FLAG\_FIND\_CLOSE | 搜尋完成后關閉該對話方塊。 |
| FLAG\_FIND\_COUNT | 計算匹配字符串的出現次數。 |
| FLAG\_FIND\_EMBEDDED\_NL | 比對 CSV 文檔中的內嵌新行字元，不比對其他新行字元。 |
| FLAG\_FIND\_ESCAPE | 使用轉義序列。 |
| FLAG\_FIND\_NEXT | 從光標處往下搜尋字符串。如果沒有設置該標志，則往上搜尋字符串。 |
| FLAG\_FIND\_NO\_PROMPT | 禁止顯示對話方塊即使沒有找到任何字符串。 |
| FLAG\_FIND\_ONLY\_WORD | 匹配整個單詞。 |
| FLAG\_FIND\_REG\_EXP | 使用規則運算式。 |
| FLAG\_FIND\_SAVE\_HISTORY | 為重復搜尋保存搜尋過的字符串。 |
| FLAG\_FIND\_SELECT\_ALL | 選擇所有匹配的字符串。 |

_szFind_

指定一個要搜尋的字符串。

## 返回值

如果消息成功，返回值為非零值。如果消息不成功，返回值為零。

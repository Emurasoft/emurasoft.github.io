# Editor\_FindW

搜尋一個 Unicode 字串。您能直接用該內嵌函式或明確地發送
the [EE\_FINDW](../message/ee_findw) 消息。

Editor\_FindW( HWND hwnd, UINT nFlags, LPCWSTR szFind )

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_nFlags_

> 您能從如下值中指定一個組合。
>
> | 值 | 含義 |
> | --- | --- |
> | FLAG\_FIND\_AROUND | 移動到文字的開始/結束處。 |
> | FLAG\_FIND\_BOOKMARK | 在有符合的字串的行上設置書籤。 |
> | FLAG\_FIND\_CASE | 區分大小寫。 |
> | FLAG\_FIND\_CLOSE | 搜尋完成后關閉該對話方塊。 |
> | FLAG\_FIND\_COUNT | 計算符合字串的出現次數。 |
> | FLAG\_FIND\_EMBEDDED\_NL | 比對 CSV 文檔中的內嵌新行字元，不比對其他新行字元。 |
> | FLAG\_FIND\_ESCAPE | 使用逸出序列。 |
> | FLAG\_FIND\_NEXT | 從游標處往下搜尋字串。如果沒有設置該標志，則往上搜尋字串。 |
> | FLAG\_FIND\_NO\_PROMPT | 禁止顯示對話方塊即使沒有找到任何字串。 |
> | FLAG\_FIND\_ONLY\_WORD | 符合整個單字。 |
> | FLAG\_FIND\_REG\_EXP | 使用規則運算式。 |
> | FLAG\_FIND\_SAVE\_HISTORY | 為重複搜尋儲存搜尋過的字串。 |
> | FLAG\_FIND\_SELECT\_ALL | 選擇所有符合的字串。 |

_szFind_

> 指定一個要搜尋的字串。

## 返回值

> 如果消息成功，返回值為非零值。如果消息不成功，返回值為零。
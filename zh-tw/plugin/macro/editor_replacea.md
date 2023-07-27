# Editor\_ReplaceA

取代一個 ANSI 字串。R您能直接用該內嵌函式或明確地發送
[EE\_REPLACEA](../message/ee_replacea) 消息。

Editor\_ReplaceA( HWND hwnd, UINT nFlags, LPCSTR szFindReplace );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nFlags_

您能從如下值中指定一個組合。

| 值 | 含義 |
| --- | --- |
| FLAG\_FIND\_CASE | 區分大小寫。 |
| FLAG\_FIND\_CLOSE | 搜尋完成后關閉對話方塊。 |
| FLAG\_FIND\_ESCAPE | 使用逸出序列。 |
| FLAG\_FIND\_NO\_PROMPT | 禁止顯示對話方塊即使沒有找到字串。 |
| FLAG\_FIND\_ONLY\_WORD | 符合整個單字。 |
| FLAG\_FIND\_REG\_EXP | 使用規則運算式。 |
| FLAG\_FIND\_SAVE\_HISTORY | 為重複搜尋儲存搜尋過的字串。 |
| FLAG\_REPLACE\_ALL | 取代所有符合的結果。 |
| FLAG\_REPLACE\_SEL\_ONLY | 當被用 FLAG\_REPLACE\_ALL 指定時，僅在選區中取代。 |

_szFindReplace_

指定一個要搜尋的字串和一個用來取代的字串。您必須按照先指定要搜尋的字串，然后指定用來取代的字串這個順序，另外，兩者之間必須插入空字元 ('\\0')。

## 返回值

如果消息成功，返回值不是零。如果消息不成功，返回值是零。

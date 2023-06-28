# EE\_REPLACEA

替換一個 ANSI 字符串。您能明確地發送該消息或用
[Editor\_ReplaceA](../macro/editor_replacea) 內嵌函式。

EE\_REPLACEA

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCSTR) szFindReplace;

## 參數

_nFlags_

> 您能從如下值中指定一個組合。
>
> | 值 | 含義 |
> | --- | --- |
> | FLAG\_FIND\_CASE | 區分大小寫。 |
> | FLAG\_FIND\_CLOSE | 搜尋完成后關閉對話方塊。 |
> | FLAG\_FIND\_ESCAPE | 使用轉義序列。 |
> | FLAG\_FIND\_NO\_PROMPT | 禁止顯示對話方塊即使沒有找到字符串。 |
> | FLAG\_FIND\_ONLY\_WORD | 匹配整個單詞。 |
> | FLAG\_FIND\_REG\_EXP | 使用規則運算式。 |
> | FLAG\_FIND\_SAVE\_HISTORY | 為重復搜尋保存搜尋過的字符串。 |
> | FLAG\_REPLACE\_ALL | 替換所有符合的結果。 |
> | FLAG\_REPLACE\_SEL\_ONLY | 當被用 FLAG\_REPLACE\_ALL 指定時，僅在選區中替換。 |

_szFindReplace_

> 指定一個要搜尋的字符串和一個用來替換的字符串。您必須按照先指定要搜尋的字符串，然后指定用來替換的字符串這個順序，另外，兩者之間必須插入空字符 ('\\0')。

## 返回值

> 如果消息成功，返回值不是零。如果消息不成功，返回值是零。
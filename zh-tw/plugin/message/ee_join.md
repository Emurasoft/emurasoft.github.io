# EE\_JOIN

按指定索引鍵資料欄,用一個與 JOIN 操作類似的方法合併兩個 CSV 文檔,并創建一個新文檔。您可以明確地發送該消息或用 [Editor\_Join](../macro/editor_join) 內嵌函式。

EE\_JOIN

wParam = (WPARAM) (JOIN\_INFO\*) pJoinInfo;

lParam = 0;

## 參數

_pJoinInfo_

> 指針指向 [JOIN\_INFO](../structure/join_info) 結構。

## 返回值

> 返回值是新文檔的行數。返回值為負數如果發生錯誤的話。如果發生錯誤,返回值是下列值之一:
>
> |     |     |
> | --- | --- |
> | E\_DOCUMENT\_1\_NOT\_FOUND | 無法找到第一個文檔。 |
> | E\_DOCUMENT\_2\_NOT\_FOUND | 無法找到第二個文檔。 |
> | E\_COLUMN\_1\_NOT\_FOUND | 無法找到第一欄。 |
> | E\_COLUMN\_2\_NOT\_FOUND | 無法找到第一欄。 |
> | E\_SELECT\_SYNTAX | 選擇的字串中有語法錯誤。 |
> | E\_SELECT\_DOCUMENT\_NOT\_FOUND | 無法在選擇的字串中找到指定的文檔。 |
> | E\_SELECT\_COLUMN\_NOT\_FOUND | 無法在選擇的字串中找到指定欄。 |
> | E\_DIFFERENT\_CSV\_MODE | 不同的 CSV 模式。 |
> | E\_NOT\_MDI | 必須啟用 Tab。 |
> | E\_WRITE\_TEMP\_FILE | 臨時檔案寫入錯誤。 |
> | E\_ABORT | 被使用者中止。 |
> | E\_FAIL | 未指定的錯誤。 |

## 版本

> 支持 EmEditor 14.8 或之後的版本。
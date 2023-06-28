# Editor\_Join

按指定索引鍵資料欄,用一個與 JOIN 操作類似的方法合併兩個 CSV 文檔,并創建一個新文檔。您可以用該內嵌函式或直接發送 [EE\_JOIN](../message/ee_join) 消息。

Editor\_Join( HWND hwnd, UINT nFlags, LPCWSTR pszDocument1, LPCWSTR pszColumn1, LPCWSTR pszDocument2, LPCWSTR pszColumn2, LPCWSTR pszSelect, int\* piDocument3 );

## 參數

_hwnd_

> 指定 EmEditor 視圖或方塊架的視窗控制代碼。

_nFlags_

> 您能指定下列值的一個組合。
>
> |     |     |
> | --- | --- |
> | JOIN\_FLAG\_UNIQUE\_KEY\_1 | 第一個文檔中指定的索引鍵資料欄包含一個唯一索引鍵。 |
> | JOIN\_FLAG\_UNIQUE\_KEY\_2 | 第二個文檔中指定的索引鍵資料欄包含一個唯一索引鍵。 |
> | JOIN\_FLAG\_INCLUDE\_ALL\_1 | 第一個文檔中的所有資料列都會被包括在輸出中。輸出文檔將包含空的資料格如果第一個文檔中的行沒有符合的結果。 |
> | JOIN\_FLAG\_INCLUDE\_ALL\_2 | 第一個文檔中的所有資料列都會被包括在輸出中。輸出文檔將包含空的資料格如果第一個文檔中的行沒有符合的結果。 |
> | JOIN\_FLAG\_MATCH\_CASE | 大小寫符合。 |
> | JOIN\_FLAG\_SIMPLE\_JOIN | 合併兩個文檔而不比較索引鍵。如果指定了此標志，則會忽略 _pszColumn1_ 和 _pszColumn2_ 參數。 |
> | JOIN\_FLAG\_IGNORE\_HEADINGS\_1 | 忽略第一個文檔中的標題，以便將第一個文檔中的標題保留在合併的文檔中。 |
> | JOIN\_FLAG\_IGNORE\_HEADINGS\_2 | 忽略第二個文檔中的標題。 |
> | JOIN\_FLAG\_CONTAIN | Key1 包含 Key2。 |
> | JOIN\_FLAG\_START\_WITH | Key1 以 Key2 開始。 |
> | JOIN\_FLAG\_END\_WITH | Key1 以 Key2 結尾。 |
> | JOIN\_FLAG\_MATCH\_SPLIT\_BOTH | 兩個分割的字串都符合。 |
> | JOIN\_FLAG\_MATCH\_SPLIT\_ONE | Key1 符合分割的 Key2。 |
> | JOIN\_FLAG\_FUZZY | 使用模糊比對。 此旗標不能與 JOIN\_FLAG\_END\_WITH、JOIN\_FLAG\_MATCH\_SPLIT\_BOTH 或 JOIN\_FLAG\_MATCH\_SPLIT\_ONE 結合使用。此旗標會使過程變慢。 |
> | JOIN\_FLAG\_SWAP | Key1 和 Key2 互換，如果還指定了 JOIN\_FLAG\_CONTAIN，JOIN\_FLAG\_START\_WITH，或 JOIN\_FLAG\_END\_WITH。 |

_pszDocument1_

> 指定字串來識別第一個文檔。這個值可以是檔案名，檔案名以及路徑，或一個冒號 (:) 后跟目前的群組中指定文檔的索引號。例如，"filename.csv"，"C:\\data\\filename.csv" (如果是 JavaScript，"C:\\\data\\\filename.csv")，或 ":2"。

_pszColumn1_

> 指定字串來識別第一個文檔的索引鍵資料欄。這個值可以是指定欄的第一行或一個冒號 (:) 后跟指定欄的索引號。例如，"first\_name" 或 ":5"。

_pszDocument2_

> 指定字串來識別第二個文檔。這個值的格式與 pszDocument1 格式相同。

_pszColumn2_

> 指定字串來識別第二個文檔的索引鍵資料欄。這個值的格式與 pszColumn1 格式相同。

_pszSelect_

> 指定字串來選擇要包括在輸出文檔中的欄。例如，"file1.csv>column1,file2.csv>column2"。

_piDocument3_

> 這個欄位將充滿輸出文檔的索引，當函數返回時。如果這個值為 NULL，這個欄位會被忽略。

## 返回值

> 返回值是新文檔的行數。返回值為負數如果發生錯誤的話。如果發生錯誤,返回值是下列值之一:
>
> |     |     |
> | --- | --- |
> | E\_DOCUMENT\_1\_NOT\_FOUND | 無法找到第一個文檔。 |
> | E\_DOCUMENT\_2\_NOT\_FOUND | 無法找到第二個文檔。 |
> | E\_COLUMN\_1\_NOT\_FOUND | 無法找到第一欄。 |
> | E\_COLUMN\_2\_NOT\_FOUND | 無法找到第二欄。 |
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
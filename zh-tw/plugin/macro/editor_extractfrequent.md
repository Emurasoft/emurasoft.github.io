# Editor\_ExtractFrequent

將常用字串抽出到新文檔中。你能直接用該內嵌函式或明確地發送 [EE\_EXTRACT\_FREQUENT](../message/ee_extract_frequent) 消息。

Editor\_ExtractFrequent( HWND hwnd, UINT nType, UINT nNumOfLines, UINT iCsvFormat, UINT64 nFlags, LPCWSTR pszIgnore );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控點。

_nType_

指定以下值之一。

| 值 | 含義 |
| --- | --- |
| FREQ\_TYPE\_LINES | 創建一個常用行清單。 |
| FREQ\_TYPE\_WORDS | 創建一個常用詞清單。單字是由非字母數字字元包圍的字串，可以通過在 **自訂** 對話方塊中的 [**編輯** 頁面](../../dlg/customize/edit/index) 上的 **將下列字元識別為字母數字** 文字方塊來自訂。 |
| FREQ\_TYPE\_CELLS | 創建一個常用儲存格清單。 |
| FREQ\_TYPE\_IPV4 | 創建一個常用 IPv4 地址清單。 |
| FREQ\_TYPE\_IPV6 | 創建一個常用 IPv6 地址清單。 |
| FREQ\_TYPE\_URI | 創建一個常用 URI 的清單。 |
| FREQ\_TYPE\_EMAIL | 創建一個常用電子郵件地址清單。 |

_nNumOfLines_

指定要抽出的最大字串數。實際匯出可能會超過此數字，以便包括所有同一頻率檢測到的多個字串。

_iCsvFormat_

指定要顯示的 CSV 格式。

_nFlags_

指定以下值的組合。

| 值 | 含義 |
| --- | --- |
| FLAG\_FIND\_CASE | 大小寫需符合。 |
| FLAG\_FIND\_OPEN\_DOC | 在同一個框架視窗中，搜索所有打開的文檔。 |
| FLAG\_FIND\_SEL\_ONLY | 僅在選區內搜索。 |

_pszIgnore_

>指定在計算常用字串時要忽略的字串。多個字串必須用換行符 (\\n) 分隔。

## 返回值

如果發生錯誤，則返回值為負。

## 版本

支持 EmEditor Professional 21.9 或之後的版本。

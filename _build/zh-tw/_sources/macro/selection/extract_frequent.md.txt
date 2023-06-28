# ExtractFrequent 方法

將常用字串抽出到新文檔中。

#### \[JavaScript\]

document.selection.ExtractFrequent( nType, nFlags, nCsvFormat, nNumOfLines, sIgnore );

#### \[VBScript\]

document.selection.ExtractFrequent nType, nFlags, nCsvFormat, nNumOfLines, sIgnore

## 參數

_nType_

> 指定以下值之一。如果省略，則使用 eeFreqTypeLines。

> | 值 | 含義 |
> | --- | --- |
> | eeFreqTypeLines | 創建一個常用行清單。 |
> | eeFreqTypeWords | 創建一個常用詞清單。單字是由非字母數字字元包圍的字串，可以通過在 **自訂** 對話方塊中的 [**編輯** 頁面](../../dlg/customize/edit/index) 上的 **將以下字元識別為英數字元** 文字方塊來自訂。 |
> | eeFreqTypeCells | 創建一個常用儲存格清單。 |
> | eeFreqTypeIPv4 | 創建一個常用 IPv4 地址清單。 |
> | eeFreqTypeIPv6 | 創建一個常用 IPv6 地址清單。 |

_nNumOfLines_

> 指定要抽出的最大字串數。實際匯出可能會超過此數字，以便包括所有同一頻率檢測到的多個字串。如果省略，則使用預設值。

_iCsvFormat_

> 指定要顯示的 CSV 格式。如果省略，則使用第一個定義的 CSV 格式。

_nFlags_

> 指定以下值的組合。如果省略，則使用 0。
>
> | 值 | 含義 |
> | --- | --- |
> | eeFindReplaceCase | 大小寫需符合。 |
> | eeFindReplaceOpenDoc | 在同一個框架視窗中，搜索所有打開的文檔。 |
> | eeFindReplaceSelOnly | 僅在選區內搜索。 |

_pszIgnore_

> 指定在計算常用字串時要忽略的字串。多個字串必須用換行符號 (\\n) 分隔。 如果省略，則使用空字串。

## 版本

支持 EmEditor Professional Version 21.9 或之後的版本。
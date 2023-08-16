# BATCH\_GREP\_INFO

用於 [Editor\_BatchFindInFiles](../macro/editor_batchfindinfiles) 和
[Editor\_BatchReplaceInFiles](../macro/editor_batchreplaceinfiles) 內嵌函式 ( [EE\_FIND\_IN\_FILESW](../message/ee_find_in_filesw) 和 [EE\_REPLACE\_IN\_FILESW \
消息](../message/ee_replace_in_filesw)) 。

typedef struct \_BATCH\_GREP\_INFO {

UINT cbSize; // sizeof( BATCH\_GREP\_INFO )

UINT nBatchCount;

UINT64 nBatchFlags;

UINT64 nTotalCount;

LPCWSTR pszPath;

LPCWSTR pszBackupPath;

LPCWSTR pszFilesToIgnore;

UINT nCP;

UINT nLimit;

HRESULT hr;

} BATCH\_GREP\_INFO;

## 欄位

_cbSize_

指定 sizeof( BATCH\_GREP\_INFO )。

_nBatchCount_

指定在 _lParam_ 參數中指定的 FIND\_REPLACE\_INFO 結構的數量。

_nBatchFlags_

指定一個以下值的組合。

|     |     |
| --- | --- |
| FLAG\_FIND\_COUNT\_FREQUENCY | 根據結果創建一個常用字串表。必須與 FLAG\_FIND\_EXTRACT 和 FLAG\_FIND\_OUTPUT\_DISPLAY 合用。 |
| FLAG\_FIND\_IGNORE\_FILES | I忽略由 _pszFilesToIgnore_ 指定的檔案或資料夾。 |
| FLAG\_FIND\_RECURSIVE | 在指定路徑的子資料夾中搜索。 |
| FLAG\_FIND\_REGEX\_BOOST | 使用 Boost.Regex 作為規則運算式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 使用 Onigmo 作為規則運算式引擎。 |
| FLAG\_FIND\_OPEN\_DIRECT | 直接打開包含指定字串的文檔。不能與 FLAG\_FIND\_OPEN\_FILTER 或 FLAG\_FIND\_OUTPUT 合用。 |
| FLAG\_FIND\_OPEN\_FILTER | 直接打開包含指定字串的文檔，並將指定字串設為篩選。不能與 FLAG\_FIND\_OPEN\_DIRECT 或 FLAG\_FIND\_OUTPUT 合用。 |
| FLAG\_FIND\_OUTPUT | 在匯出欄中以清單形式顯示「多檔尋找」結果。不能與 FLAG\_FIND\_OPEN\_DIRECT 或 FLAG\_FIND\_OPEN\_FILTER 合用。 |
| FLAG\_FIND\_OUTPUT\_ENCODING | 將編碼名稱附加到檔案名。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 區別處理 CR 和 LF。 |
| FLAG\_REPLACE\_BACKUP | 儲存備份。不能與 FLAG\_REPLACE\_KEEP\_OPEN 合用。 |
| FLAG\_REPLACE\_KEEP\_OPEN | 保持修改的檔案為打開狀態。不能與 FLAG\_REPLACE\_BACKUP 合用。 |

此外，您可以指定以下值之一。

|     |     |
| --- | --- |
| FLAG\_FIND\_FILE\_AND\_MATCHED | 搜索結果將顯示檔案名和符合的字串。 |
| FLAG\_FIND\_FILE\_LINE\_AND\_MATCHED | 搜索結果將顯示檔案名，行號和符合的字串。 |
| FLAG\_FIND\_FILENAMES\_ONLY | 搜索結果僅顯示檔案名，而包含搜索字串的整行將不顯示為結果。 |
| FLAG\_FIND\_LINE\_ONLY | 搜索結果僅顯示包含搜索字串的整行。 |
| FLAG\_FIND\_MATCHED\_ONLY | 搜索結果僅顯示符合的字串。 |

_nTotalCount_

返回時，此欄位將接收所有搜索的檔案中符合字串出現的總數。如果不用於取代檔案，則返回值為所有搜索的檔案中包含符合字串的行總數。

_pszFind_

指定要搜索的字串。

_pszReplace_

多檔取代時，指定要取代的字串。

_pszPath_

指定要搜索的路徑。它可以包括通配符，例如 \\* 和 ?。

_pszBackupPath_

當多檔取代時，指定備份資料夾，如果 _nFlags_
包括 FLAG\_REPLACE\_BACKUP。

_pszFilesToIgnore_

如果 _nFlags_ 包括 FLAG\_FIND\_IGNORE\_FILES，則指定要忽略的檔案或資料夾名稱。它可以包括通配符，例如 \* 和 ?。要指定多個檔案，用分號 (;) 來隔開檔案。

_nCP_

指定用於打開檔案的程式碼頁。

|     |     |
| --- | --- |
| CODEPAGE\_ANSI | 標準 ANSI |
| CODEPAGE\_UNICODE | Unicode little endian |
| CODEPAGE\_UNICODE\_BIGENDIAN | Unicode big endian |
| CODEPAGE\_UTF8 | UTF-8 |
| CODEPAGE\_UTF7 | UTF-7 |
| CODEPAGE\_932 | 日文 Shift JIS |
| CODEPAGE\_JIS | 日文 JIS |
| CODEPAGE\_EUC | 日文 EUC |
| CODEPAGE\_AUTO\_SJIS\_JIS | 從日文 Shift JIS 和 JIS 轉換。 |
| CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | 從日文 Shift JIS、JIS、EUC 轉換。 |
| Others | 你能通過系統使用的所有程式碼頁。 |
| CODEPAGE\_DETECT\_UNICODE | 檢測 Unicode。能與另一個值進行組合。 |
| CODEPAGE\_DETECT\_UTF8 | 檢測 UTF-8。能與另一個值進行組合。 |
| CODEPAGE\_DETECT\_CHARSET | 檢測 HTML/XML Charset。能與另一個值進行組合。 |
| CODEPAGE\_DETECT\_ALL | 檢測所有程式碼頁。能與另一個值進行組合。 |

_nLimit_

當符合數達到此數字時，EmEditor 將停止搜索檔案。 如果指定 0，則 EmEditor 不會停止搜索檔案。

_hr_

此欄位將由結果值填充，其中負值表示錯誤。錯誤值包括以下值。

|     |     |
| --- | --- |
| E\_WRONG\_NUM\_FORMAT | 檢測到數字/IP 地址範圍的格式不正確。 |
| E\_REGEX\_UNKNOWN | 規則運算式引擎中發生未知錯誤。 |

## 版本

支持 EmEditor Professional 20.0 或之後的版本。

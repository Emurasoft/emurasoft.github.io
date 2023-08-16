# GREP\_INFO\_EX

用於 [Editor\_FindInFiles 巨集](../macro/editor_findinfilesw)，
[Editor\_ReplaceInFiles 巨集](../macro/editor_replaceinfilesw) ( [EE\_FIND\_IN\_FILESW 消息](../message/ee_find_in_filesw)， [EE\_REPLACE\_IN\_FILESW 消息](../message/ee_replace_in_filesw)) 中。

typedef struct \_GREP\_INFOW {

size\_t cbSize;

UINT nCP;

UINT64 nFlags;

LPCWSTR pszFind;

LPCWSTR pszReplace;

LPCWSTR pszPath;

LPCWSTR pszBackupPath;

LPCWSTR pszFilesToIgnore;

UINT nLimit;

UINT64 nTotalCount;

HRESULT hr;

} GREP\_INFOW;

## 欄位

_cbSize_

指定 size\_of(GREP\_INFO\_EX)。

_nCP_

指定打開一個檔案的程式碼頁。

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
| CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | 從 日文 Shift JIS、JIS、EUC 轉換。 |
| Others | 你能通過系統使用的所有程式碼頁。 |
| CODEPAGE\_DETECT\_UNICODE | 偵測 Unicode。不能與另一個值合併使用。 |
| CODEPAGE\_DETECT\_UTF8 | 偵測 UTF-8。 不能與另一個值合併使用。 |
| CODEPAGE\_DETECT\_CHARSET | 偵測 HTML/XML 字元集。不能與另一個值合併使用。 |
| CODEPAGE\_DETECT\_ALL | 偵測所有程式碼頁。可以與其他值合併使用。 |

_nFlags_

指定一個下列值的組合。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 區分大小寫。 |
| FLAG\_FIND\_COUNT\_FREQUENCY | 從尋找結果中創建常用字串清單。必須與 FLAG\_FIND\_OUTPUT\_DISPLAY 合併使用。 |
| FLAG\_FIND\_ESCAPE | 使用逸出數列。不能與 FLAG\_FIND\_REG\_EXP 合併使用。 |
| FLAG\_FIND\_FUZZY | 使用模糊比對。 |
| FLAG\_FIND\_IGNORE\_FILES | 忽略被 _pszFilesToIgnore_ 指定的檔案或資料夾。 |
| FLAG\_FIND\_ONLY\_WORD | 符合整個單字。 |
| FLAG\_FIND\_RECURSIVE | 在指定路徑的子資料夾中搜索。 |
| FLAG\_FIND\_REG\_EXP | 使用規則運算式。不能與 FLAG\_FIND\_ESCAPE 合併使用。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作為規則運算式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作為規則運算式引擎。 |
| FLAG\_FIND\_OPEN\_DIRECT | 直接打開包含指定字串的文檔。不能與 FLAG\_FIND\_OPEN\_FILTER or FLAG\_FIND\_OUTPUT 合併使用。 |
| FLAG\_FIND\_OPEN\_FILTER | 直接打開包含指定字串的文檔，並且把指定字串設為篩選器。不能與 FLAG\_FIND\_OPEN\_DIRECT 或 FLAG\_FIND\_OUTPUT 合併使用。 |
| FLAG\_FIND\_OUTPUT | 在輸出列清單中顯示多檔尋找搜索結果。不能與 FLAG\_FIND\_OPEN\_DIRECT 或 FLAG\_FIND\_OPEN\_FILTER 合併使用。 |
| FLAG\_FIND\_OUTPUT\_ENCODING | 將編碼名稱附加到檔案名。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 區分 CR 和 LF。 |
| FLAG\_REPLACE\_BACKUP | 儲存備份。不能與 FLAG\_REPLACE\_KEEP\_OPEN 合併使用。 |
| FLAG\_REPLACE\_KEEP\_OPEN | 儲存修改的檔案開啟。不能與 eeReplaceBackup 合併使用。也不能與 FLAG\_REPLACE\_BACKUP 合併使用。 |

此外，您可以指定以下值之一。

|     |     |
| --- | --- |
| FLAG\_FIND\_FILE\_AND\_MATCHED | 搜索結果將顯示檔案名和符合的字串。 |
| FLAG\_FIND\_FILE\_LINE\_AND\_MATCHED | 搜索結果將顯示檔案名，行號和符合的字串。 |
| FLAG\_FIND\_FILENAMES\_ONLY | 搜索結果僅顯示檔案名，而包含搜索字串的整行將不顯示為結果。 |
| FLAG\_FIND\_LINE\_ONLY | 搜索結果僅顯示包含搜索字串的整行。 |
| FLAG\_FIND\_MATCHED\_ONLY | 搜索結果僅顯示符合的字串。 |

_pszFind_

指定要搜索的字串。

_pszReplace_

當在多個檔案中取代時，指定要取代成的字串。

_pszPath_

指定要搜索的路徑。它能包括通配符例如 \\* 和 ?。

_pszBackupPath_

當多個檔案取代時，指定備份資料夾，如果 _nFlags_ 包含 FLAG\_REPLACE\_BACKUP 的話。

_pszFilesToIgnore_

如果 _nFlags_ 包含 FLAG\_FIND\_IGNORE\_FILES，指定要忽略的檔案或資料夾名稱。它能包括通配符，例如 \* 和 ?。要指定多個檔案，請用分號來分隔檔案。

_nLimit_

當符合數達到此數字時，EmEditor 停止搜索檔案。 如果指定 0，則 EmEditor 不會停止搜索檔案。

_nTotalCount_

返回時，此欄位將接收所有搜索的檔案中符合字串出現的總數。如果不用於取代檔案，則返回值為所有搜索的檔案中包含符合字串的行總數。

_hr_

此欄位將由結果值填充，其中負值表示錯誤。錯誤值包括以下值。

|     |     |
| --- | --- |
| E\_WRONG\_NUM\_FORMAT | 檢測到數字/IP 地址範圍的格式不正確。 |
| E\_REGEX\_UNKNOWN | 規則運算式引擎中發生未知錯誤。 |

## 版本

支持 Version 15.7 或之後的版本。

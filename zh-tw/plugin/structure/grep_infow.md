# GREP\_INFOW

用於 [Editor\_FindInFilesW 巨集](../macro/editor_findinfilesw)，
[Editor\_ReplaceInFilesW 巨集](../macro/editor_replaceinfilesw) ( [EE\_FIND\_IN\_FILESW \
消息](../message/ee_find_in_filesw)， [EE\_REPLACE\_IN\_FILESW \
消息](../message/ee_replace_in_filesw))。

```
typedef struct _GREP_INFOW {
	UINT cbSize;
	UINT nCP;
	UINT nFlags;
	LPCWSTR pszFind;
	LPCWSTR pszReplace;
	LPCWSTR pszPath;
	LPCWSTR pszBackupPath;
	LPCWSTR pszFilesToIgnore;
} GREP_INFOW;
```

## Fields

_cbSize_

指定 sizeof(GREP\_INFOA)。

_nCP_

按檔案被打開的方式指定一個代碼頁。

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
| Others | 您能通過系統使用的所有代碼頁。 |
| CODEPAGE\_DETECT\_UNICODE | 偵測 Unicode。能與另一個值進行組合。 |
| CODEPAGE\_DETECT\_UTF8 | 偵測 UTF-8。能與另一個值進行組合。 |
| CODEPAGE\_DETECT\_CHARSET | 偵測 HTML/XML Charset。能與另一個值進行組合。 |
| CODEPAGE\_DETECT\_ALL | 偵測所有代碼頁。能與另一個值進行組合。 |

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 區分大小寫。 |
| FLAG\_FIND\_ESCAPE | 使用轉義序列。不能與 FLAG\_FIND\_REG\_EXP 聯用。 |
| FLAG\_FIND\_ONLY\_WORD | 匹配整個單詞。 |
| FLAG\_FIND\_REG\_EXP | 使用規則運算式。不能與 FLAG\_FIND\_ESCAPE 聯用。 |
| FLAG\_FIND\_RECURSIVE | 在指定路徑的子資料夾中搜尋。 |
| FLAG\_FIND\_FILENAMES\_ONLY | 僅顯示檔案名稱。 |
| FLAG\_REPLACE\_KEEP\_OPEN | 保存修改過的檔案開啟。不能與 eeReplaceBackup 聯用。不能與 FLAG\_REPLACE\_BACKUP 聯用。 |
| FLAG\_REPLACE\_BACKUP | 保存備份。不能與 FLAG\_REPLACE\_KEEP\_OPEN 聯用。 |
| FLAG\_FIND\_IGNORE\_FILES | 忽略用 _pszFilesToIgnore_ 指定的檔案或資料夾。 |
| FLAG\_FIND\_OUTPUT | 把搜尋結果重新導向到輸出列。 |

_pszFind_

指定一個要搜尋的字符串。

_pszReplace_

當多檔取代時，指定一個要用來替換的字符串。

_pszPath_

指定搜尋路徑。它可以包括通配符，例如 \\* 和 ?。

_pszBackupPath_

當多檔取代時，指定備份資料夾，如果 _nFlags_
包括 FLAG\_REPLACE\_BACKUP。

_pszFilesToIgnore_

如果 _nFlags_ 包括 FLAG\_FIND\_IGNORE\_FILES，指定要忽略的檔案或資料夾名稱。它能包括通配符，例如 \* 和 ?。要指定多個檔案，用分號 (;) 來區分它們。

## 支持版本

支持 EmEditor 4.02 或之後的版本。

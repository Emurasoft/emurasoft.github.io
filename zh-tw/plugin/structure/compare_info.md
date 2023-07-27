# COMPARE\_INFO

用於 [EE\_COMPARE](../message/ee_compare) 消息。

typedef struct \_COMPARE\_INFO {

UINT cbSize;

UINT flags;

LPCWSTR pszDocument1;

LPCWSTR pszDocument2;

LPCWSTR pszResultFileName;

} COMPARE\_INFO;

## 欄位

_cbSize_

指定結構的大小，sizeof( COMPARE\_INFO )。

_flags_

指定以下值的組合。

|     |     |
| --- | --- |
| COMPARE\_GENERATE\_REPORT | 生成一個報告檔案。必須在 strResultFileName 中指定路徑名稱。 |
| COMPARE\_IGNORE\_CASE | 忽略大小寫。 |
| COMPARE\_IGNORE\_COMMENT | 忽略組態標記為注釋的文字。 |
| COMPARE\_IGNORE\_CRLF | 忽略換行符的差異。 |
| COMPARE\_IGNORE\_EMBEDDED\_SPACE | 忽略一行中第一個和最後一個非空格字元之間的空格。 |
| COMPARE\_IGNORE\_ENCODING | 忽略編碼差異。 |
| COMPARE\_IGNORE\_LEAD\_SPACE | 忽略一行中第一個非空格字元之前的空格。 |
| COMPARE\_IGNORE\_TRAIL\_SPACE | 忽略一行中最後一個非空格字元後的空格。 |
| COMPARE\_OPEN\_REPORT | 打開報告檔案。必須指定 COMPARE\_GENERATE\_REPORT。 |
| COMPARE\_REPORT\_3\_COL | 使用 3 欄格式匯出報告。 |
| COMPARE\_REPORT\_DIFF\_ONLY | 僅報告不相同的行。 |
| COMPARE\_QUALITY\_1 | 搜索附近行的最快的方法。 |
| COMPARE\_QUALITY\_2 | 較快的方法。 |
| COMPARE\_QUALITY\_3 | 中等速度。 |
| COMPARE\_QUALITY\_4 | 較精確的方法。 |
| COMPARE\_QUALITY\_5 | 搜索整個檔案最精確的方法（有一定的限制）。 |
| COMPARE\_QUICK | 快速比較，不會亮顯差異。此旗標不能與除 COMPARE\_QUIET 之外的其他選項結合使用。 |
| COMPARE\_QUIET | 不顯示任何匯出消息。 |
| COMPARE\_RESET | 重設比較或同步捲動模式並清除比較結果。 |
| COMPARE\_RESET\_AFTER | 重設比較或同步捲動模式並在比較和報告生成後清除比較結果。另外，必須被指定 COMPARE\_GENERATE\_REPORT。 |
| COMPARE\_RESTORE\_POS | 完成後恢復視窗位置。 |
| COMPARE\_SPLIT\_VERT | 垂直分割視窗以顯示文檔。 |
| COMPARE\_SWITCH\_NO\_WRAP | 切換到不換行。 |
| COMPARE\_SYNC\_CARET | 同步游標位置。 |
| COMPARE\_SYNC\_SCROLL\_HORZ | 同步水平捲動。 |
| COMPARE\_SYNC\_SCROLL\_ONLY | 顯示比較文檔但不用亮顯顯示差異。 |
| COMPARE\_SYNC\_SCROLL\_VERT | 同步垂直捲動。 |
| COMPARE\_TILE\_HORZ | 水平平鋪檔案。 |
| COMPARE\_TILE\_VERT | 垂直平鋪檔案。 |

_pszDocument1_

指定用於標識第一個文檔的字串。該值可以是檔案名，帶完整路徑的檔案名或一個冒號 (:) 后跟目前的組中的文檔索引。例如，"filename.csv"，"C:\\data\\filename.csv"，或 ":2"。

_pszDocument2_

指定用於標識第二個文檔的字串。該值的格式與 strDocument1 相同。

_pszResultFileName_

如果在 flags 欄位指定了 COMPARE\_GENERATE\_REPORT，EmEditor 會用指定的檔案名儲存比較報告。

## 版本

支持 EmEditor Professional v17.7 或之後的版本。

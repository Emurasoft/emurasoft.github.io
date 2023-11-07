# LOAD\_FILE\_INFO\_EX

用於 [Editor\_LoadFileA](../macro/editor_loadfilea)
和 [Editor\_LoadFileW](../macro/editor_loadfilew)
內嵌函式 ( [EE\_LOAD\_FILEA](../message/ee_load_filea) 和
[EE\_LOAD\_FILEW](../message/ee_load_filew) 消息) 中。

```
typedef struct _LOAD_FILE_INFO_EX {
	UINT cbSize;
	UINT nCP;
	BOOL bDetectUnicode;
	BOOL bDetectAll;
	BOOL bDetectCharset;
	BOOL bDetectUTF8;
	UINT nFlags;
} LOAD_FILE_INFO_EX;
```

## Fields

_cbSize_

一定是 sizeof(LOAD\_FILE\_INFO\_EX)。

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

_bDetectUnicode_

如果 TRUE，Unicode 會被偵測。

_bDetectAll_

如果 TRUE，所有代碼頁會被偵測。

_bDetectCharset_

如果 TRUE，HTML/XML Charset 會被偵測。

_bDetectUTF8_

如果 TRUE，UTF-8 會被偵測。

_nFlags_

從如下值中指定一個組合。

|     |     |
| --- | --- |
| LFI\_ALLOW\_ASYNC\_OPEN | 允許異步打開一個檔案。 |
| LFI\_ALLOW\_NEW\_WINDOW | 在新視窗中打開一個檔案。 |
| LFI\_USE\_DISK\_MODE | 打開檔案時使用啟用磁碟模式。 |
| LFI\_DONT\_USE\_DISK\_MODE | 打開檔案時不使用啟用磁碟模式。如果既沒有指定 LFI\_USE\_DISK\_MODE 也沒有指定 LFI\_DONT\_USE\_DISK\_MODE，EmEditor 會根據將要打開的檔案大小自動選擇使用啟用磁碟模式。 |
| LFI\_DONT\_ADD\_RECENT | 不將檔案路徑添加到最近的檔案清單中。 |

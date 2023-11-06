# LOAD\_FILE\_INFO\_EX

Used by [Editor\_LoadFileA](../macro/editor_loadfilea)
and [Editor\_LoadFileW](../macro/editor_loadfilew)
inline functions ( [EE\_LOAD\_FILEA](../message/ee_load_filea) and
[EE\_LOAD\_FILEW](../message/ee_load_filew) messages).

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

Must be sizeof(LOAD\_FILE\_INFO\_EX).

_nCP_

Specifies a code page by which a file is opened.

|     |     |
| --- | --- |
| CODEPAGE\_CONFIG | Uses file encodings specified in the configuration associated with the opened file. |
| CODEPAGE\_ANSI | Normal ANSI |
| CODEPAGE\_UNICODE | Unicode little endian |
| CODEPAGE\_UNICODE\_BIGENDIAN | Unicode big endian |
| CODEPAGE\_UTF8 | UTF-8 |
| CODEPAGE\_UTF7 | UTF-7 |
| CODEPAGE\_932 | Japanese Shift JIS |
| CODEPAGE\_JIS | Japanese JIS |
| CODEPAGE\_EUC | Japanese EUC |
| CODEPAGE\_AUTO\_SJIS\_JIS | Converts from Japanese Shift JIS and JIS. |
| CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | Converts from Japanese Shift JIS、JIS、EUC. |
| Others | All code pages you can use by system. |

_bDetectUnicode_

If TRUE, Unicode will be detected.

_bDetectAll_

If TRUE, all code pages will be detected.

_bDetectCharset_

If TRUE, HTML/XML Charset will be detected.

_bDetectUTF8_

If TRUE, UTF-8 will be detected.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| LFI\_ALLOW\_ASYNC\_OPEN | Allows a file to be opened asynchronously. |
| LFI\_ALLOW\_NEW\_WINDOW | Opens a file in a new window. |
| LFI\_USE\_DISK\_MODE | Uses temporary files when opening a file. |
| LFI\_DONT\_USE\_DISK\_MODE | Doesn't use temporary files when opening a file. If neither LFI\_USE\_DISK\_MODE nor LFI\_DONT\_USE\_DISK\_MODE is specified, EmEditor automatically selects to use temporary files depending on the size of the file that is about to be opened. |
| LFI\_DONT\_ADD\_RECENT | Doesn't add the file path to the recent file list. |

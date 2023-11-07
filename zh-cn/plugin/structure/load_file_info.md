# LOAD\_FILE\_INFO\_EX

用于 [Editor\_LoadFileA](../macro/editor_loadfilea)
和 [Editor\_LoadFileW](../macro/editor_loadfilew)
内联函数 ( [EE\_LOAD\_FILEA](../message/ee_load_filea) 和
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

按文件被打开的方式指定一个代码页。

|     |     |
| --- | --- |
| CODEPAGE\_ANSI | 标准 ANSI |
| CODEPAGE\_UNICODE | Unicode little endian |
| CODEPAGE\_UNICODE\_BIGENDIAN | Unicode big endian |
| CODEPAGE\_UTF8 | UTF-8 |
| CODEPAGE\_UTF7 | UTF-7 |
| CODEPAGE\_932 | 日文 Shift JIS |
| CODEPAGE\_JIS | 日文 JIS |
| CODEPAGE\_EUC | 日文 EUC |
| CODEPAGE\_AUTO\_SJIS\_JIS | 从日文 Shift JIS 和 JIS 转换。 |
| CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | 从日文 Shift JIS、JIS、EUC 转换。 |
| Others | 你能通过系统使用的所有代码页。 |

_bDetectUnicode_

如果 TRUE，Unicode 会被侦测。

_bDetectAll_

如果 TRUE，所有代码页会被侦测。

_bDetectCharset_

如果 TRUE，HTML/XML Charset 会被侦测。

_bDetectUTF8_

如果 TRUE，UTF-8 会被侦测。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| LFI\_ALLOW\_ASYNC\_OPEN | 允许异步打开一个文件。 |
| LFI\_ALLOW\_NEW\_WINDOW | 在新窗口中打开一个文件。 |
| LFI\_USE\_DISK\_MODE | 打开文件时使用启用硬盘模式。 |
| LFI\_DONT\_USE\_DISK\_MODE | 打开文件时不使用启用硬盘模式。如果既没有指定 LFI\_USE\_DISK\_MODE 也没有指定 LFI\_DONT\_USE\_DISK\_MODE，EmEditor 会根据要打开的文件大小自动选择使用启用硬盘模式。 |
| LFI\_DONT\_ADD\_RECENT | 不将文件路径添加到最近的文件列表中。 |

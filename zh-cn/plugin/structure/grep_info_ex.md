# GREP\_INFO\_EX

用于 [Editor\_FindInFiles 宏](../macro/editor_findinfilesw)，
[Editor\_ReplaceInFiles 宏](../macro/editor_replaceinfilesw) ( [EE\_FIND\_IN\_FILESW 消息](../message/ee_find_in_filesw)， [EE\_REPLACE\_IN\_FILESW 消息](../message/ee_replace_in_filesw)) 中。

```
typedef struct _GREP_INFOW {
	size_t cbSize;
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
} GREP_INFOW;
```

## 字段

_cbSize_

指定 size\_of(GREP\_INFO\_EX)。

_nCP_

指定打开一个文件的代码页。

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
| CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | 从 日文 Shift JIS、JIS、EUC 转换。 |
| Others | 你能通过系统使用的所有代码页。 |
| CODEPAGE\_DETECT\_UNICODE | 检测 Unicode。不能与另一个值合并。 |
| CODEPAGE\_DETECT\_UTF8 | 检测 UTF-8。 不能与另一个值合并。 |
| CODEPAGE\_DETECT\_CHARSET | 检测 HTML/XML 字符集。不能与另一个值合并。 |
| CODEPAGE\_DETECT\_ALL | 检测所有代码页。可以与其他值合并。 |

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 区分大小写。 |
| FLAG\_FIND\_COUNT\_FREQUENCY | 从查找结果中创建常用字符串列表。必须与 FLAG\_FIND\_OUTPUT\_DISPLAY 同时使用。 |
| FLAG\_FIND\_ESCAPE | 使用转义符。不能与 FLAG\_FIND\_REG\_EXP 同时使用。 |
| FLAG\_FIND\_FUZZY | 使用模糊匹配。 |
| FLAG\_FIND\_IGNORE\_FILES | 忽略被 _pszFilesToIgnore_ 指定的文件或文件夹。 |
| FLAG\_FIND\_ONLY\_WORD | 匹配整个单词。 |
| FLAG\_FIND\_RECURSIVE | 在指定路径的子文件夹中搜索。 |
| FLAG\_FIND\_REG\_EXP | 使用正则表达式。不能与 FLAG\_FIND\_ESCAPE 同时使用。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作为正则表达式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作为正则表达式引擎。 |
| FLAG\_FIND\_OPEN\_DIRECT | 直接打开包含指定字符串的文档。不能与 FLAG\_FIND\_OPEN\_FILTER or FLAG\_FIND\_OUTPUT 同时使用。 |
| FLAG\_FIND\_OPEN\_FILTER | 直接打开包含指定字符串的文档，并且把指定字符串设为筛选器。不能与 FLAG\_FIND\_OPEN\_DIRECT 或 FLAG\_FIND\_OUTPUT 同时使用。 |
| FLAG\_FIND\_OUTPUT | 在输出栏列表中显示在文件中查找搜索结果。不能与 FLAG\_FIND\_OPEN\_DIRECT 或 FLAG\_FIND\_OPEN\_FILTER 同时使用。 |
| FLAG\_FIND\_OUTPUT\_ENCODING | 将编码名称附加到文件名。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 区分 CR 和 LF。 |
| FLAG\_REPLACE\_BACKUP | 保存备份。不能与 FLAG\_REPLACE\_KEEP\_OPEN 同时使用。 |
| FLAG\_REPLACE\_KEEP\_OPEN | 保存修改的文件开启。不能与 eeReplaceBackup 同时使用。也不能与 FLAG\_REPLACE\_BACKUP 同时使用。 |

此外，您可以指定以下值之一。

|     |     |
| --- | --- |
| FLAG\_FIND\_FILE\_AND\_MATCHED | 搜索结果将显示文件名和匹配的字符串。 |
| FLAG\_FIND\_FILE\_LINE\_AND\_MATCHED | 搜索结果将显示文件名，行号和匹配的字符串。 |
| FLAG\_FIND\_FILENAMES\_ONLY | 搜索结果仅显示文件名，而包含搜索字符串的整行将不显示为结果。 |
| FLAG\_FIND\_LINE\_ONLY | 搜索结果仅显示包含搜索字符串的整行。 |
| FLAG\_FIND\_MATCHED\_ONLY | 搜索结果仅显示匹配的字符串。 |

_pszFind_

指定要搜索的字符串。

_pszReplace_

当在多个文件中替换时，指定要替换成的字符串。

_pszPath_

指定要搜索的路径。它能包括通配符例如 \\* 和 ?。

_pszBackupPath_

当多个文件替换时，指定备份文件夹，如果 _nFlags_ 包含 FLAG\_REPLACE\_BACKUP 的话。

_pszFilesToIgnore_

如果 _nFlags_ 包含 FLAG\_FIND\_IGNORE\_FILES，指定要忽略的文件或文件夹名称。它能包括通配符，例如 \* 和 ?。要指定多个文件，请用分号来分隔文件。

_nLimit_

当匹配数达到此数字时，EmEditor 停止搜索文件。 如果指定 0，则 EmEditor 不会停止搜索文件。

_nTotalCount_

返回时，此字段将接收所有搜索的文件中匹配字符串出现的总数。如果不用于替换文件，则返回值为所有搜索的文件中包含匹配字符串的行总数。

_hr_

此字段将由结果值填充，其中负值表示错误。错误值包括以下值。

|     |     |
| --- | --- |
| E\_WRONG\_NUM\_FORMAT | 检测到数字/IP 地址范围的格式不正确。 |
| E\_REGEX\_UNKNOWN | 正则表达式引擎中发生未知错误。 |

## 版本

支持 Version 15.7 或之后的版本。

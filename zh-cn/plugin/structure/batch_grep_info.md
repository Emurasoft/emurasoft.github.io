# BATCH\_GREP\_INFO

用于 [Editor\_BatchFindInFiles](../macro/editor_batchfindinfiles) 和
[Editor\_BatchReplaceInFiles](../macro/editor_batchreplaceinfiles) 内联函数 ( [EE\_FIND\_IN\_FILESW](../message/ee_find_in_filesw) 和 [EE\_REPLACE\_IN\_FILESW \
消息](../message/ee_replace_in_filesw)) 。

```
typedef struct _BATCH_GREP_INFO {
	UINT cbSize; // sizeof( BATCH_GREP_INFO )
	UINT nBatchCount;
	UINT64 nBatchFlags;
	UINT64 nTotalCount;
	LPCWSTR pszPath;
	LPCWSTR pszBackupPath;
	LPCWSTR pszFilesToIgnore;
	UINT nCP;
	UINT nLimit;
	HRESULT hr;
} BATCH_GREP_INFO;
```

## 字段

_cbSize_

指定 sizeof( BATCH\_GREP\_INFO )。

_nBatchCount_

指定在 _lParam_ 参数中指定的 FIND\_REPLACE\_INFO 结构的数量。

_nBatchFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| FLAG\_FIND\_COUNT\_FREQUENCY | 根据结果创建一个常用字符串表。必须与 FLAG\_FIND\_EXTRACT 和 FLAG\_FIND\_OUTPUT\_DISPLAY 合用。 |
| FLAG\_FIND\_IGNORE\_FILES | I忽略由 _pszFilesToIgnore_ 指定的文件或文件夹。 |
| FLAG\_FIND\_RECURSIVE | 在指定路径的子文件夹中搜索。 |
| FLAG\_FIND\_REGEX\_BOOST | 使用 Boost.Regex 作为正则表达式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 使用 Onigmo 作为正则表达式引擎。 |
| FLAG\_FIND\_OPEN\_DIRECT | 直接打开包含指定字符串的文档。不能与 FLAG\_FIND\_OPEN\_FILTER 或 FLAG\_FIND\_OUTPUT 合用。 |
| FLAG\_FIND\_OPEN\_FILTER | 直接打开包含指定字符串的文档，并将指定字符串设为筛选。不能与 FLAG\_FIND\_OPEN\_DIRECT 或 FLAG\_FIND\_OUTPUT 合用。 |
| FLAG\_FIND\_OUTPUT | 在输出栏中以列表形式显示“在文件中查找”结果。不能与 FLAG\_FIND\_OPEN\_DIRECT 或 FLAG\_FIND\_OPEN\_FILTER 合用。 |
| FLAG\_FIND\_OUTPUT\_ENCODING | 将编码名称附加到文件名。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 区别处理 CR 和 LF。 |
| FLAG\_REPLACE\_BACKUP | 保存备份。不能与 FLAG\_REPLACE\_KEEP\_OPEN 合用。 |
| FLAG\_REPLACE\_KEEP\_OPEN | 保持修改的文件为打开状态。不能与 FLAG\_REPLACE\_BACKUP 合用。 |

此外，您可以指定以下值之一。

|     |     |
| --- | --- |
| FLAG\_FIND\_FILE\_AND\_MATCHED | 搜索结果将显示文件名和匹配的字符串。 |
| FLAG\_FIND\_FILE\_LINE\_AND\_MATCHED | 搜索结果将显示文件名，行号和匹配的字符串。 |
| FLAG\_FIND\_FILENAMES\_ONLY | 搜索结果仅显示文件名，而包含搜索字符串的整行将不显示为结果。 |
| FLAG\_FIND\_LINE\_ONLY | 搜索结果仅显示包含搜索字符串的整行。 |
| FLAG\_FIND\_MATCHED\_ONLY | 搜索结果仅显示匹配的字符串。 |

_nTotalCount_

返回时，此字段将接收所有搜索的文件中匹配字符串出现的总数。如果不用于替换文件，则返回值为所有搜索的文件中包含匹配字符串的行总数。

_pszFind_

指定要搜索的字符串。

_pszReplace_

在文件中替换时，指定要替换的字符串。

_pszPath_

指定要搜索的路径。它可以包括通配符，例如 \\* 和 ?。

_pszBackupPath_

当在文件中替换时，指定备份文件夹，如果 _nFlags_
包括 FLAG\_REPLACE\_BACKUP。

_pszFilesToIgnore_

如果 _nFlags_ 包括 FLAG\_FIND\_IGNORE\_FILES，则指定要忽略的文件或文件夹名称。它可以包括通配符，例如 \* 和 ?。要指定多个文件，用分号 (;) 来隔开文件。

_nCP_

指定用于打开文件的代码页。

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
| CODEPAGE\_DETECT\_UNICODE | 检测 Unicode。能与另一个值进行组合。 |
| CODEPAGE\_DETECT\_UTF8 | 检测 UTF-8。能与另一个值进行组合。 |
| CODEPAGE\_DETECT\_CHARSET | 检测 HTML/XML Charset。能与另一个值进行组合。 |
| CODEPAGE\_DETECT\_ALL | 检测所有代码页。能与另一个值进行组合。 |

_nLimit_

当匹配数达到此数字时，EmEditor 将停止搜索文件。 如果指定 0，则 EmEditor 不会停止搜索文件。

_hr_

此字段将由结果值填充，其中负值表示错误。错误值包括以下值。

|     |     |
| --- | --- |
| E\_WRONG\_NUM\_FORMAT | 检测到数字/IP 地址范围的格式不正确。 |
| E\_REGEX\_UNKNOWN | 正则表达式引擎中发生未知错误。 |

## 版本

支持 EmEditor Professional 20.0 或之后的版本。

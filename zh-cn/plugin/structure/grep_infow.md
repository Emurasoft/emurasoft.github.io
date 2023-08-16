# GREP\_INFOW

用于 [Editor\_FindInFilesW 宏](../macro/editor_findinfilesw)，
[Editor\_ReplaceInFilesW 宏](../macro/editor_replaceinfilesw) ( [EE\_FIND\_IN\_FILESW \
消息](../message/ee_find_in_filesw)， [EE\_REPLACE\_IN\_FILESW \
消息](../message/ee_replace_in_filesw))。

typedef struct \_GREP\_INFOW {

UINT cbSize;

UINT nCP;

UINT nFlags;

LPCWSTR pszFind;

LPCWSTR pszReplace;

LPCWSTR pszPath;

LPCWSTR pszBackupPath;

LPCWSTR pszFilesToIgnore;

} GREP\_INFOW;

## Fields

_cbSize_

指定 sizeof(GREP\_INFOA)。

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
| CODEPAGE\_DETECT\_UNICODE | 检测 Unicode。能与另一个值进行组合。 |
| CODEPAGE\_DETECT\_UTF8 | 检测 UTF-8。能与另一个值进行组合。 |
| CODEPAGE\_DETECT\_CHARSET | 检测 HTML/XML Charset。能与另一个值进行组合。 |
| CODEPAGE\_DETECT\_ALL | 检测所有代码页。能与另一个值进行组合。 |

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 区分大小写。 |
| FLAG\_FIND\_ESCAPE | 使用转义序列。不能与 FLAG\_FIND\_REG\_EXP 联用。 |
| FLAG\_FIND\_ONLY\_WORD | 匹配整个单词。 |
| FLAG\_FIND\_REG\_EXP | 使用正则表达式。不能与 FLAG\_FIND\_ESCAPE 联用。 |
| FLAG\_FIND\_RECURSIVE | 在指定路径的子文件夹中搜索。 |
| FLAG\_FIND\_FILENAMES\_ONLY | 仅显示文件名称。 |
| FLAG\_REPLACE\_KEEP\_OPEN | 保存修改过的文件开启。不能与 eeReplaceBackup 联用。不能与 FLAG\_REPLACE\_BACKUP 联用。 |
| FLAG\_REPLACE\_BACKUP | 保存备份。不能与 FLAG\_REPLACE\_KEEP\_OPEN 联用。 |
| FLAG\_FIND\_IGNORE\_FILES | 忽略用 _pszFilesToIgnore_ 指定的文件或文件夹。 |
| FLAG\_FIND\_OUTPUT | 把搜索结果重新导向到输出栏。 |

_pszFind_

指定一个要搜索的字符串。

_pszReplace_

当在文件中替换时，指定一个要用来替换的字符串。

_pszPath_

指定搜索路径。它可以包括通配符，例如 \\* 和 ?。

_pszBackupPath_

当在文件中替换时，指定备份文件夹，如果 _nFlags_
包括 FLAG\_REPLACE\_BACKUP。

_pszFilesToIgnore_

如果 _nFlags_ 包括 FLAG\_FIND\_IGNORE\_FILES，指定要忽略的文件或文件夹名称。它能包括通配符，例如 \* 和 ?。要指定多个文件，用分号 (;) 来区分它们。

## 支持版本

支持 EmEditor 4.02 或之后的版本。

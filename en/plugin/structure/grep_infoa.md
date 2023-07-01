# GREP\_INFOA

Used by [Editor\_FindInFilesA macro](../macro/editor_findinfilesa),
[Editor\_ReplaceInFilesA inline functions](../macro/editor_replaceinfilesa) ( [EE\_FIND\_IN\_FILESA \
message](../message/ee_find_in_filesa), [EE\_REPLACE\_IN\_FILESA \
message](../message/ee_replace_in_filesa) s).

typedef struct \_GREP\_INFOA {

UINT cbSize;

UINT nCP;

UINT nFlags;

LPCSTR pszFind;

LPCSTR pszReplace;

LPCSTR pszPath;

LPCSTR pszBackupPath;

LPCSTR pszFilesToIgnore;

} GREP\_INFOA;

## Fields

_cbSize_

> Specifies size of (GREP\_INFOA).

_nCP_

> Specifies a code page by which a file is opened.
>
> |     |     |
> | --- | --- |
> | CODEPAGE\_ANSI | Normal ANSI |
> | CODEPAGE\_UNICODE | Unicode little endian |
> | CODEPAGE\_UNICODE\_BIGENDIAN | Unicode big endian |
> | CODEPAGE\_UTF8 | UTF-8 |
> | CODEPAGE\_UTF7 | UTF-7 |
> | CODEPAGE\_932 | Japanese Shift JIS |
> | CODEPAGE\_JIS | Japanese JIS |
> | CODEPAGE\_EUC | Japanese EUC |
> | CODEPAGE\_AUTO\_SJIS\_JIS | Converts from Japanese Shift JIS and JIS. |
> | CODEPAGE\_AUTO\_SJIS\_JIS\_EUC | Converts form Japanese Shift JIS、JIS、EUC. |
> | Others | All code pages you can used by system. |
> | CODEPAGE\_DETECT\_UNICODE | Detects Unicode. Can be combined with another value. |
> | CODEPAGE\_DETECT\_UTF8 | Detects UTF-8. Can be combined with another value. |
> | CODEPAGE\_DETECT\_CHARSET | Detects HTML/XML Charset. Can be combined with another value. |
> | CODEPAGE\_DETECT\_ALL | Detects all code pages. Can be combined with another value. |

_nFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | Matches cases. |
> | FLAG\_FIND\_ESCAPE | Uses escape sequences. Cannot be combined with FLAG\_FIND\_REG\_EXP. |
> | FLAG\_FIND\_FILENAMES\_ONLY | Only file names will be displayed and the whole lines containing the searched string will not be displayed as results. Cannot combine with FLAG\_FIND\_LINE\_ONLY or FLAG\_FIND\_MATCHED\_ONLY. |
> | FLAG\_FIND\_IGNORE\_FILES | Ignores the files or folders specified by _pszFilesToIgnore_. |
> | FLAG\_FIND\_LINE\_ONLY | Only the whole lines containing the searched string will be displayed as results. Cannot combine with FLAG\_FIND\_FILENAMES\_ONLY or FLAG\_FIND\_MATCHED\_ONLY. |
> | FLAG\_FIND\_MATCHED\_ONLY | Only the matched strings will be displayed as results. Cannot combine with FLAG\_FIND\_FILENAMES\_ONLY or FLAG\_FIND\_LINE\_ONLY. |
> | FLAG\_FIND\_ONLY\_WORD | Searches only words. |
> | FLAG\_FIND\_RECURSIVE | Searches in subfolders of the specified path. |
> | FLAG\_FIND\_REG\_EXP | Uses a regular expression. Cannot be combined with FLAG\_FIND\_ESCAPE. |
> | FLAG\_FIND\_OPEN\_DIRECT | Directly opens the document that includes the specified string. Cannot combine with FLAG\_FIND\_OPEN\_FILTER or FLAG\_FIND\_OUTPUT. |
> | FLAG\_FIND\_OPEN\_FILTER | Directly opens the document that includes the specified string, and set the specified string as the filter. Cannot combine with FLAG\_FIND\_OPEN\_DIRECT or FLAG\_FIND\_OUTPUT. |
> | FLAG\_FIND\_OUTPUT | Displays the Find in Files results as a list in the Output Bar. Cannot combine with FLAG\_FIND\_OPEN\_DIRECT or FLAG\_FIND\_OPEN\_FILTER. |
> | FLAG\_REPLACE\_BACKUP | Saves the backups. Cannot be combined with FLAG\_REPLACE\_KEEP\_OPEN. |
> | FLAG\_REPLACE\_KEEP\_OPEN | Keeps the modified files open. Cannot combine with eeReplaceBackup. <br> Cannot be combined with FLAG\_REPLACE\_BACKUP. |

_pszFind_

> Specifies a string to search for.

_pszReplace_

> When replacing in files, specifies a string to replace with.

_pszPath_

> Specifies a path to search from. It can include wild cards such as \* and
> ?.

_pszBackupPath_

> When replacing in files, specifies the backup folder, if _nFlags_
> includes FLAG\_REPLACE\_BACKUP.

_pszFilesToIgnore_

> If _nFlags_ includes FLAG\_FIND\_IGNORE\_FILES, specifies the file or
> folder names to ignore. It can include wild cards such as \* and ?. To
> specify multiple files, use semicolons (;) to separate them.

## Version

> Supported on EmEditor Professional Version 4.02 or later.

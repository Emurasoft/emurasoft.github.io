# BATCH\_GREP\_INFO

Used by [Editor\_BatchFindInFiles](../macro/editor_batchfindinfiles) and
[Editor\_BatchReplaceInFiles](../macro/editor_batchreplaceinfiles) inline functions ( [EE\_FIND\_IN\_FILESW](../message/ee_find_in_filesw) and [EE\_REPLACE\_IN\_FILESW \
message](../message/ee_replace_in_filesw) s).

typedef struct \_BATCH\_GREP\_INFO {

UINT cbSize; // sizeof( BATCH\_GREP\_INFO )

UINT nBatchCount;

UINT64 nBatchFlags;

UINT64 nTotalCount;

LPCWSTR pszPath;

LPCWSTR pszBackupPath;

LPCWSTR pszFilesToIgnore;

UINT nCP;

UINT nLimit;

HRESULT hr;

} BATCH\_GREP\_INFO;

## Fields

_cbSize_

> Specifies size\_of(BATCH\_GREP\_INFO).

_nBatchCount_

> Specifies the number of FIND\_REPLACE\_INFO structures specified in _lParam_.

_nBatchFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_COUNT\_FREQUENCY | Creates a table of frequent strings from the results. Must combine with FLAG\_FIND\_OUTPUT\_DISPLAY. |
> | FLAG\_FIND\_IGNORE\_FILES | Ignores the files or folders specified by _pszFilesToIgnore_. |
> | FLAG\_FIND\_RECURSIVE | Searches in subfolders of the specified path. |
> | FLAG\_FIND\_REGEX\_BOOST | Uses Boost.Regex as the regular expression engine. |
> | FLAG\_FIND\_REGEX\_ONIGMO | Uses Onigmo as the regular expression engine. |
> | FLAG\_FIND\_OPEN\_DIRECT | Directly opens the document that includes the specified string. Cannot combine with FLAG\_FIND\_OPEN\_FILTER or FLAG\_FIND\_OUTPUT. |
> | FLAG\_FIND\_OPEN\_FILTER | Directly opens the document that includes the specified string, and set the specified string as the filter. Cannot combine with FLAG\_FIND\_OPEN\_DIRECT or FLAG\_FIND\_OUTPUT. |
> | FLAG\_FIND\_OUTPUT | Displays the Find in Files results as a list in the Output Bar. Cannot combine with FLAG\_FIND\_OPEN\_DIRECT or FLAG\_FIND\_OPEN\_FILTER. |
> | FLAG\_FIND\_OUTPUT\_ENCODING | Appends encoding names to file names. |
> | FLAG\_FIND\_SEPARATE\_CRLF | Treats CR and LF separately. |
> | FLAG\_REPLACE\_BACKUP | Saves the backups. Cannot be combined with FLAG\_REPLACE\_KEEP\_OPEN. |
> | FLAG\_REPLACE\_KEEP\_OPEN | Keeps the modified files open. Cannot combine with eeReplaceBackup. <br> Cannot be combined with FLAG\_REPLACE\_BACKUP. |
>
> Additionally, you may specify one of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_FILE\_AND\_MATCHED | File names and matched strings will be displayed. |
> | FLAG\_FIND\_FILE\_LINE\_AND\_MATCHED | File names, line numbers and matched strings will be displayed. |
> | FLAG\_FIND\_FILENAMES\_ONLY | Only file names will be displayed and the whole lines containing the searched string will not be displayed as results. |
> | FLAG\_FIND\_LINE\_ONLY | Only the whole lines containing the searched string will be displayed as results. |
> | FLAG\_FIND\_MATCHED\_ONLY | Only the matched strings will be displayed as results. |

_nTotalCount_

> On return, this field will contain the total number of the occurrences of the matched string in all the searched files. If this is not used for replacing in files, the return value is the total number of lines containing matched strings in all the searched files.

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

_nLimit_

> EmEditor stops searching files when the number of matches reaches this number. If 0 is specified, EmEditor does not stop searching files.

_hr_

> This field will be filled with the result value where the negative value indicates an error. Error values include the following values.
>
> |     |     |
> | --- | --- |
> | E\_WRONG\_NUM\_FORMAT | An incorrect format of a number/IP address range was detected. |
> | E\_REGEX\_UNKNOWN | An unknown error occurred in the regular expression engine. |

## Version

> Supported on EmEditor Professional Version 20.0 or later.

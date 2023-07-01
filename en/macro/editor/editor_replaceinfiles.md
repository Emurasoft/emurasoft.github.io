# ReplaceInFiles Method (Editor Object)

Replaces text in multiple files.

#### \[JavaScript\]

nFound = editor. **ReplaceInFiles**( _strFind_, _strReplace_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _strBackupPath_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] \] );

#### \[VBScript\]

nFound = editor. **ReplaceInFiles** _strFind_, _strReplace_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _strBackupPath_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] \]

## Parameters

_strFind_

Specifies a string to search for.

_strReplace_

Specifies a string to replace with.

_strPath_

Specifies a path to search from. It can include wild cards such as \* and ?.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| eeFindRecursive | Searches in subfolders of the specified path. |
| eeFindReplaceCase | Matches cases. |
| eeFindReplaceEscSeq | Uses escape sequences. Cannot combine with eeFindReplaceRegExp. |
| eeFindReplaceIgnoreFiles | Ignores the files or folders specified by _strFilesToIgnore_. |
| eeFindReplaceOnlyWord | Searches only words. |
| eeFindReplaceRegExp | Uses a regular expression. Cannot combine with eeFindReplaceEscSeq. |
| eeOpenDetectAll | Detects all encodings. |
| eeOpenDetectCharset | Detects HTML/XML Charset. |
| eeOpenDetectUnicode | Detects Unicode signature (BOM). |
| eeOpenDetectUTF8 | Detects UTF-8. |
| eeReplaceBackup | Saves the backups. Cannot combine with eeReplaceKeepOpen. |
| eeReplaceKeepOpen | Keeps the modified files open. Cannot combine with eeReplaceBackup. |

_nEncoding_

Selects from the **[Encoding Constants](../const/const_encoding)**,
or specify any code page used in the Windows Operating System. If 0 is specified or omitted, the encoding specified in the configuration properties associated with the searched file name will be used.

_strFilesToIgnore_

If _nFlags_  includes eeFindReplaceIgnoreFiles, specifies the file or
folder names to ignore. It can include wild cards such as \* and ?. To specify
multiple files, use semicolons (;) to separate them.

_strBackupPath_

Specifies the backup folder if _nFlags_  specifies eeReplaceBackup.

_nExFlags_

Specifies a combination of the following values. However, only one of eeExFindRegexBoost and eeExFindRegexOnigmo can be specified. If none of these two is specified, the default regular expression engine is used.

|     |     |
| --- | --- |
| eeExFindFuzzy | Uses fuzzy matching. |
| eeExFindNumberRange | Matches a [number range expression](../../howto/search/number_range_syntax). This flag cannot be combined with eeFindReplaceEscSeq or eeFindReplaceRegExp. |
| eeExFindRegexBoost | Uses Boost.Regex as the regular expression engine. |
| eeExFindRegexOnigmo | Uses Onigmo as the regular expression engine. |

_nLimit_

EmEditor stops searching files when the number of matches reaches this number. If 0 is specified, EmEditor does not stop searching files.

## Return Values

The return value is the total number of replaced strings in all the searched files.

## Remarks

This action cannot be undone unless _nFlags_  specifies eeReplaceKeepOpen.
It is recommended to specify eeReplaceBackup as _nFlags_  and saves backups.
If the same file name exists in the backup folder, the new backup will overwrite
the old file.

## Version

Supported on EmEditor Professional Version 4.02 or later.

# FindInFiles Method (Editor Object)

Searches multiple files for matching string. The resultant list of the
searched files will be displayed on the current window. If the document is not
saved, this method will display the prompt message whether to save the file.

## 

### \[JavaScript\]

```
nFound = editor.FindInFiles( strFind, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ nExFlags, [ nLimit ] ] ] ] );
```

### \[VBScript\]

```
nFound = editor.FindInFiles strFind, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ nExFlags, [ nLimit ] ] ] ]
```

## Parameters

_strFind_

Specifies a string to search for.

_strPath_

Specifies a path to search from. It can include wild cards such as \* and ?.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| eeFindOpenDirect | Directly opens the document that includes the specified string. Cannot combine with eeFindOpenFilter or eeFindOutput. |
| eeFindOpenFilter | Directly opens the document that includes the specified string, and set the specified string as the filter. Cannot combine with eeFindOpenDirect or eeFindOutput. |
| eeFindOutput | Displays the Find in Files results as a list in the Output Bar. Cannot combine with eeFindOpenDirect or eeFindOpenFilter. |
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

Additionally, you may specify one of the following values.

|     |     |
| --- | --- |
| eeFindFileAndMatched | File names and matched strings will be displayed. |
| eeFindFileLineAndMatched | File names, line numbers and matched strings will be displayed. |
| eeFindFileNamesOnly | Only file names will be displayed and the whole lines containing the searched string will not be displayed as results. |
| eeFindLineOnly | Only the whole lines containing the searched string will be displayed as results. |
| eeFindMatchedOnly | Only the matched strings will be displayed as results. |

_nEncoding_

Selects from the **[Encoding Constants](../const/const_encoding)**,
or specify any code page used in the Windows Operating System. If 0 is specified or omitted, the encoding specified in the configuration properties associated with the searched file name will be used.

_strFilesToIgnore_

If _nFlags_  includes eeFindReplaceIgnoreFiles, specify the file or
folder names to ignore. It can include wild cards such as \* and ?. To specify
multiple files, use semicolons (;) to separate them.

_nExFlags_

Specifies a combination of the following values. However, only one of eeExFindRegexBoost, eeExFindRegexOnigmo, and eeExFindRegexOnigmoPerl can be specified. If none of them is specified, the default regular expression engine is used.

|     |     |
| --- | --- |
| eeExFindCountFrequency | Creates a table of frequent strings from the Extract results. Must combine with eeFindLineOnly or eeFindMatchedOnly. |
| eeExFindFuzzy | Uses fuzzy matching. |
| eeExFindNumberRange | Matches a [number range expression](../../howto/search/number_range_syntax). This flag cannot be combined with eeFindReplaceEscSeq or eeFindReplaceRegExp. |
| eeExFindOutputEncoding | Appends encoding names to file names. |
| eeExFindRegexBoost | Uses Boost.Regex as the regular expression engine. |
| eeExFindRegexOnigmo | Uses Onigmo as the regular expression engine, using the Ruby syntax. |
| eeExFindRegexOnigmoPerl | Uses Onigmo as the regular expression engine, using the Perl syntax. |

_nLimit_

EmEditor stops searching files when the number of matches reaches this number. If 0 is specified, EmEditor does not stop searching files.

## Return Values

The return value is the total number of lines containing matched strings in all the searched files.

## Version

Supported on EmEditor Professional Version 4.02 or later.

# ReplaceInFiles 方法 (Editor ����)

在多个文件中替换文本。

## 

### \[JavaScript\]

```
nFound = editor.ReplaceInFiles( strFind, strReplace, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ strBackupPath, [ nExFlags, [ nLimit ] ] ] ] ] );
```

### \[VBScript\]

```
nFound = editor.ReplaceInFiles strFind, strReplace, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ strBackupPath, [ nExFlags, [ nLimit ] ] ] ] ]
```

## 参数

_strFind_

指定一个要搜索的字符串。

_strReplace_

指定一个要替换为的字符串。

_strPath_

指定一个要搜索的路径。它包括通配符例如 \\* 和 ?。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| eeFindRecursive | 在指定路径的子文件夹中搜索。 |
| eeFindReplaceCase | 大小写需符合。 |
| eeFindReplaceEscSeq | 使用转义序列。不能与 eeFindReplaceRegExp 合用。 |
| eeFindReplaceIgnoreFiles | 忽略由 _strFilesToIgnore_ 指定的文件或文件夹。 |
| eeFindReplaceOnlyWord | 匹配整个单词。 |
| eeFindReplaceRegExp | 使用正则表达式。不能与 eeFindReplaceEscSeq 合用。 |
| eeFindSaveHistory | 为重复搜索保存搜索过的字符串。 |
| eeOpenDetectAll | 检测所有编码。 |
| eeOpenDetectCharset | 检测 HTML/XML 字符集。 |
| eeOpenDetectUnicode | 检测 Unicode 签名 (BOM)。 |
| eeOpenDetectUTF8 | 检测 UTF-8。 |
| eeReplaceBackup | 保存备份。不能与 eeReplaceKeepOpen 合用。 |
| eeReplaceKeepOpen | 保持已修改的文件开启。不能与 eeReplaceBackup 合用。 |

_nEncoding_

从[编码常数](../const/const_encoding) 中选择或指定任何用于 Windows 操作系统的代码页。

_strFilesToIgnore_

如果 _nFlags_ 包括 eeFindReplaceIgnoreFiles，指定要忽略的文件或文件夹名称。它能包括通配符，例如 \* 和 ?。要指定多个文件，用分号 (;) 来隔开文件。

_strBackupPath_

指定备份文件夹如果 _nFlags_ 指定 eeReplaceBackup。

_nExFlags_

指定下列值的组合。但是，只能指定 eeExFindRegexBoost 和 eeExFindRegexOnigmo 中的一个。如果未指定这两者，则使用默认的正则表达式引擎。

|     |     |
| --- | --- |
| eeExFindFuzzy | 使用模糊匹配。 |
| eeExFindNumberRange | 匹配 [数字范围表达式](../../howto/search/number_range_syntax)。此标志不能与 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindRegexBoost | 使用 Boost.Regex 作为正则表达式引擎。 |
| eeExFindRegexOnigmo | 使用 Onigmo 作为正则表达式引擎。 |

_nLimit_

当匹配数达到此数字时，EmEditor 停止搜索文件。 如果指定 0，则 EmEditor 不会停止搜索文件。

## 返回值

返回值是所有搜索的文件中已替换字符串的总数。

## 备注

这个动作不能被撤消除非 _nFlags_ 指定 eeReplaceKeepOpen。建议您把 eeReplaceBackup 指定为 _nFlags_ 并保存备份。如果相同的文件名称存在在备份文件夹中，那么新的备份会改写旧的文件。

## 版本

支持 EmEditor 4.02 或之后的版本。

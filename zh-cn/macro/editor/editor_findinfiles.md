# FindInFiles 方法 (Editor 对象)

在多个文件中搜索匹配的字符串。搜索到的文件的结果列表将被显示在当前窗口上。如果文档没有保存，这个方法会显示是否保存文件的提示消息。

## 

### \[JavaScript\]

```
nFound = editor.FindInFiles( strFind, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ nExFlags, [ nLimit ] ] ] ] );
```

### \[VBScript\]

```
nFound = editor.FindInFiles strFind, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ nExFlags, [ nLimit ] ] ] ]
```

## 参数

_strFind_

指定一个要搜索的字符串。

_strPath_

指定要搜索的路径。它包括通配符，例如\\* 以及 ?。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| eeFindOpenDirect | 直接打开包含指定字符串的文档。 无法与 eeFindOpenFilter 或 eeFindOutput 合用。 |
| eeFindOpenFilter | 直接打开包含指定字符串的文档，并将指定字符串设为筛选。不能与 eeFindOpenDirect 或 eeFindOutput 合用。 |
| eeFindOutput | 在输出栏中以列表形式显示“在文件中查找”结果。不能与 eeFindOpenDirect 或 eeFindOpenFilter 合用。 |
| eeFindRecursive | 在指定路径的子文件夹中搜索。 |
| eeFindReplaceCase | 大小写需符合。 |
| eeFindReplaceEscSeq | 使用转义序列。不能与 eeFindReplaceRegExp 联用。 |
| eeFindReplaceIgnoreFiles | 忽略由 _strFilesToIgnore_ 指定的文件或文件夹。 |
| eeFindReplaceOnlyWord | 匹配整个单词。 |
| eeFindReplaceRegExp | 使用正则表达式。不能与 eeFindReplaceEscSeq 联用。 |
| eeOpenDetectAll | 检测所有编码。 |
| eeOpenDetectCharset | 检测 HTML/XML 字符集。 |
| eeOpenDetectUnicode | 检测 Unicode 签名 (BOM)。 |
| eeOpenDetectUTF8 | 检测 UTF-8。 |

此外，您可以指定以下值之一。

|     |     |
| --- | --- |
| eeFindFileAndMatched | 搜索结果将显示文件名和匹配的字符串。 |
| eeFindFileLineAndMatched | 搜索结果将显示文件名，行号和匹配的字符串。 |
| eeFindFileNamesOnly | 搜索结果仅显示文件名，而包含搜索字符串的整行将不显示为结果。 |
| eeFindLineOnly | 搜索结果仅显示包含搜索字符串的整行。 |
| eeFindMatchedOnly | 搜索结果仅显示匹配的字符串。 |

_nEncoding_

从 **[编码常数](../const/const_encoding)** 中选择或指定任何用于 Windows 操作系统的代码页。

_strFilesToIgnore_

如果 _nFlags_ 包括 eeFindReplaceIgnoreFiles，指定要忽略的文件或文件夹名称。它能包括通配符，例如 \* 和 ?。要指定多个文件，用分号 (;) 来隔开文件。

_nExFlags_

指定下列值的组合。但是，只能指定 eeExFindRegexBoost 和 eeExFindRegexOnigmo 中的一个。如果未指定这两者，则使用默认的正则表达式引擎。

|     |     |
| --- | --- |
| eeExFindCountFrequency | 从提取结果中创建常用字符串列表。必须与 eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeExFindFuzzy | 使用模糊匹配。 |
| eeExFindNumberRange | 匹配 [数字范围表达式](../../howto/search/number_range_syntax)。此标志不能与 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindOutputEncoding | 将编码名称附加到文件名。 |
| eeExFindRegexBoost | 使用 Boost.Regex 作为正则表达式引擎。 |
| eeExFindRegexOnigmo | 使用 Onigmo 作为正则表达式引擎。 |

_nLimit_

当匹配数达到此数字时，EmEditor 停止搜索文件。 如果指定 0，则 EmEditor 不会停止搜索文件。

## 返回值

返回值是在所有搜索的文件中包含匹配字符串的行数。

## 版本

支持 EmEditor 4.02 或之后的版本。

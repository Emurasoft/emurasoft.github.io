# BatchReplace 方法 (Selection ����)

替换多个字符串。

## 

### \[JavaScript\]

```
nFound = document.selection.BatchReplace( filters, nFlags, nExFlags );
```

### \[VBScript\]

```
nFound = document.selection.BatchReplace( filters, nFlags, nExFlags )
```

## 参数

_filters_

指定包含搜索和替换字符串和标志的 [Filters 集合](../filters/index)。

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeFindExtract | 把匹配的行提取到一个新文档中。可以与 eeFindFileAndLine，eeFindFileNamesOnly，eeFindLineOnly，或 eeFindMatchedOnly 合用。如果没有与这些标志合用，会假定 eeFindLineOnly。 |
| eeFindFileAndLine | 不会在搜索结果中显示文件名，行号，以及包含搜索字符串的行。一定要与 eeFindExtract 合用。不能与 eeFindFileNamesOnly，eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeFindFileNamesOnly | 仅在搜索结果中显示文件名，包含搜索字符串的行不会被显示。一定要与 eeFindExtract 合用。不能与 eeFindFileAndLine，eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeFindLineOnly | 仅在搜索结果中显示包含搜索字符串的行。一定要与 eeFindExtract 合用。不能与 eeFindFileAndLine，eeFindMatchedOnly 或 eeFindFileNamesOnly 合用。 |
| eeFindMatchedOnly | 仅在搜索结果中显示匹配的字符串。一定要与 eeFindExtract 合用。不能与 eeFindFileAndLine，eeFindFileNamesOnly 或 eeFindLineOnly 合用。 |
| eeFindMatchDotNL | 正则表达式 "." 匹配换行符。 |
| eeFindOutput | 把提取结果显示在输出栏中。一定要与 eeFindExtract 合用。 |
| eeFindReplaceEmbeddedNL | Matches embedded newlines in CSV documents and does not match other newlines. |
| eeFindReplaceOpenDoc | 在同一个框架窗口中，搜索所有打开的文档。 |
| eeFindReplaceQuiet | 状态栏上不显示消息如果没有找到任何字符串的话。 |
| eeFindReplaceSelOnly | 仅在选区内搜索。 |
| eeFindSaveHistory | 为重复搜索保存搜索过的字符串。 |
| eeReplaceAll | 一次性全部替换。 |

_nExFlags_

指定一个下列值的组合。但是，eeExFindRegexBoost 和 eeExFindRegexOnigmo 中只能指定一个。如果两个都不指定，那么会使用默认的正则表达式引擎。

|     |     |
| --- | --- |
| eeExFindBOL | 正则表达式 ‘^’ 可匹配选取部分的开头。 |
| eeExFindCountFrequency | 根据提取结果创建一个常用字符串表。必须与 eeFindExtract 和 eeFindLineOnly 或 eeFindMatchedOnly 结合使用。必须启用窗口标签页。 |
| eeExFindEOL | 正则表达式 ‘$’ 可匹配选取部分的末尾。 |
| eeExFindInsertColumn | 为提取的列创建一个新的 CSV 列。必须在 nFlags 中指定 eeFindExtract。新列将插入到原始列的右侧。 |
| eeExFindLookaround | 只在选区内进行正则表达式搜索时用前后断言。 |
| eeExFindMulti | 执行多项替换全部。如果未指定，则执行批处理替换全部。详情请参阅 [批处理和多项之间的区别](../../howto/search/batch_vs_bulk)。 |
| eeExFindRegexBoost | 把 Boost.Regex 作为正则表达式引擎。 |
| eeExFindRegexOnigmo | 把 Onigmo 作为正则表达式引擎。 |
| eeExFindSeparateCRLF | 区分 CR 和 LF。 |

## 返回值

返回 1 如果搜索字符串被找到；如果没有找到搜索字符串，则返回 0。如果 eeFindExtract 或 eeReplaceAll 标志被指定，那么返回值就是文档中匹配的字符串所出现的次数。

## 版本

支持 EmEditor Professional 19.9 或之后的版本。

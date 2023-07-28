# Replace 方法 (Selection 对象)

在文档中替换一个字符串。

## 

### \[JavaScript\]

```
nFound = document.selection.Replace( strFind, strReplace,
nFlags );
```

### \[VBScript\]

```
nFound = document.selection.Replace( strFind, strReplace,
nFlags )
```

## 参数

_strFind_

指定一个要搜索的字符串。如果指定 eeExFindNumberRange，此字符串是以区间表示的数字范围。

_strReplace_

指定要替换为的字符串。

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeFindAround | 到达文档末尾时，移至文档开头再搜索。 |
| eeFindExtract | 如果在 _nExFlags_ 中未指定 eeExFindInsertColumn，则此方法使用正则表达式将查找结果提取到新文档中。eeFindReplaceRegExp 必须在 nFlags 中指定，并且 _strReplace_ 不能为空。<br>如果在 _nExFlags_ 中指定 eeExFindInsertColumn，则 CSV 文档必须处于活动状态，并且一个 或更多列必须被选择。此外，如果在 _nFlags_ 中未指定 eeFindReplaceRegExp，则该方法将插入具有匹配字符串的新列。如果在 _nFlags_ 中指定了 eeFindReplaceRegExp，则该方法将使用正则表达式插入带有替换表达式的新列。 |
| eeFindMatchDotNL | 正则表达式 "." 匹配换行符。 |
| eeFindOutput | 将提取结果显示为输出栏中的列表。必须与 eeFindExtract 结合使用。 |
| eeFindReplaceCase | 大小写需符合。 |
| eeFindReplaceEmbeddedNL | 在 CSV 文档中只匹配嵌入式换行，不匹配其他换行。 |
| eeFindReplaceEscSeq | 使用转义序列。不能与 eeFindReplaceRegExp 联用。 |
| eeFindReplaceOnlyWord | 匹配整个单词。 |
| eeFindReplaceOpenDoc | 在同一个框架窗口中，搜索所有打开的文档。 |
| eeFindReplaceQuiet | 状态栏上不显示消息如果没有找到任何字符串的话。 |
| eeFindReplaceRegExp | 为 strFind 用正则表达式。不能与 eeFindReplaceEscSeq 联用。如果此标志与 eeFindExtract 联用，则生成的匹配项将被替换为 strReplace。 |
| eeFindReplaceSelOnly | 仅在选区内搜索。 |
| eeFindSaveHistory | 为重复搜索保存搜索过的字符串。 |
| eeReplaceAll | 立即替换全部。 |
| eeReplaceSelOnly | 仅替换选定内容。 |

_nExFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| eeExFindBOL | 正则表达式 ‘^’ 可匹配选取部分的开头。 |
| eeExFindEOL | 正则表达式 ‘$’ 可匹配选取部分的末尾。 |
| eeExFindFuzzy | 使用模糊匹配。 |
| eeExFindInsertColumn | 为提取的列创建新的 CSV 列。必须在 nFlags 中指定 eeFindExtract。新列将插入在原始列的右侧。 |
| eeExFindLookaround | 只在选区内进行正则表达式搜索时用前后断言。 |
| eeExFindNumberRange | 匹配 [数字范围表达式](../../howto/search/number_range_syntax)。此标志不能与 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindRegexBoost | 把 Boost.Regex 作为正则表达式引擎。不能与 eeExFindRegexOnigmo 联用。 |
| eeExFindRegexOnigmo | 把 Onigmo 作为正则表达式引擎。不能与 eeExFindRegexBoost 联用。 |
| eeExFindSeparateCRLF | 区分 CR 和 LF。 |

## 返回值

如果指定 eeReplaceAll，返回被替换的字符串数。否则，返回 1 如果找到，或 0 如果没有找到。

## 版本

支持 EmEditor 4.00 或之后的版本。

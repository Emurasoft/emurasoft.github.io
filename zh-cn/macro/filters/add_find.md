# AddFind 方法 (Filters 集合)

添加一个要搜索的项目。

## 

### \[JavaScript\]

```
list.AddFind( strFind, nFlags, nExFlags );
```

### \[VBScript\]

```
list.AddFind( strFind, nFlags, nExFlags )
```

## 参数

_strFind_

指定要搜索的字符串。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| eeFindLogicalOr | 如果筛选有多个级别，请指定与上一级的逻辑或运算（逻辑 OR）。 |
| eeFindNegative | 显示“筛选”工具栏，并排除与指定字符串匹配的行。 |
| eeFindReplaceCase | 大小写需符合。 |
| eeFindReplaceEscSeq | 使用转义序列。不能与 eeFindReplaceRegExp 合用。 |
| eeFindReplaceOnlyWord | 整个单词需匹配。 |
| eeFindReplaceRegExp | 使用正则表达式搜索字符串。不能与 eeFindReplaceEscSeq 合用。 |
| eeFindWholeString | 匹配整个字符串。 |

_nExFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeExFindBookmarkedOnly | 仅匹配书签行。此标志不能与 eeExFindUnbookmarkedOnly 合用。 |
| eeExFindCrLf | 匹配换行符为 CR 和 LF 的行。此标志不能与 eeExFindMatchNL 合用。 |
| eeExFindCrOnly | 匹配换行符仅是 CR 的行。此标志必须与 eeExFindMatchNL 合用。 |
| eeExFindFuzzy | 使用模糊匹配。 |
| eeExFindLfOnly | 匹配换行符仅是 LF 的行。此标志必须与 eeExFindMatchNL 合用。 |
| eeExFindLinkFile | 指定 _strFind_ 是链接文件的文件路径，该链接文件包含多个用换行符分隔的搜索字符串。如果一行中包含制表符，则搜索字符串是第一个不包含制表符的字符串。 _strFind_ 可以是 EmEditor 安装路径的相对路径。它可以包含环境变量，例如 %USERPROFILE%。要指定正在运行的宏文件夹中的文件，请使用以下形式：<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\\" ) + 1 ) + "LinkFile.txt" |
| eeExFindMatchNL | 匹配指定的换行符。此标志应与 eeExFindCrLf，eeExFindCrOnly，eeExFindLfOnly，和/或 eeExFindNLOthers 合用。 |
| eeExFindNLOthers | 匹配没有换行符的行。这些行包括文件的最后一行和很长的行，这些行继续到下一行而没有换行符。此标志必须与 eeExFindMatchNL 合用。 |
| eeExFindNumberRange | 匹配 [数字范围表达式](../../howto/search/number_range_syntax)。此标志不能与 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindUnbookmarkedOnly | 仅匹配未标示为书签的行。此标志不能与 eeExFindBookmarkedOnly 合用。 |
| eeExFilterBegin | 指定一个开始筛选。此标志不能与 eeExFilterEnd 合用。 |
| eeExFilterEnd | 指定一个结束筛选。此标志不能与 eeExFilterBegin 合用。 |

## 版本

支持 EmEditor Professional 19.9 或之后的版本。

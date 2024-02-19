# Add 方法 (Filters 集合)

添加一个项目。

## 

### \[JavaScript\]

```
list.Add( strFilter, bEnabled, iColumn, nFlags, xBegin, xEnd, strReplace, nExFlags );
```

### \[VBScript\]

```
list.Add strFilter, bEnabled, iColumn, nFlags, xBegin, xEnd, strReplace, nExFlags
```

## 参数

_strFilter_

指定一个要搜索的字符串。

_bEnabled_

指定是否要启用这个筛选。

_iColumn_

指定你想要搜索的以 1 为基准的文本的列的索引；如果你要搜索整行，可以指定 0 ；如果你要用字符数把开始以及结尾的文本指定为 _xBegin_ 和 _xEnd_，可以指定 -1。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| eeFindLogicalOr | 指定一个逻辑或运算 (logical OR) 到之前的层级上在多层级筛选的情况下。 |
| eeFindNegative | 显示筛选工具栏并排除与指定字符串匹配的行。 |
| eeFindReplaceCase | 大小写需符合。 |
| eeFindReplaceEscSeq | 使用转义序列。不能与 eeFindReplaceRegExp 合用。 |
| eeFindReplaceOnlyWord | 整个单词需匹配。 |
| eeFindReplaceRegExp | 使用正则表达式搜索字符串。不能与 eeFindReplaceEscSeq 合用。 |
| eeFindWholeString | 匹配整个字符串。 |

_xBegin_

指定你要搜索的文本的起始列的索引（逻辑字符数）；指定 0 如果你想要把文本的最后一部分作为 _xEnd_。要启用这个字段， _iColumn_ 值必须是 -1。

_xEnd_

指定你要搜索的文本的末尾列的索引（逻辑字符数）；指定 0 如果你想要搜索所有剩下的文本。要启用这个字段， _iColumn_ 值必须是 -1。

_strFilter_

指定要替换为的字符串。

_nExFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeExFindLinkFile | 指定 _strFilter_ 是链接文件的文件路径，该链接文件包含多个用换行符分隔的搜索字符串。如果一行中包含制表符，则搜索字符串是第一个不包含制表符的字符串。 _strFilter_ 可以是 EmEditor 安装路径的相对路径。它可以包含环境变量，例如 %USERPROFILE%。要指定正在运行的宏文件夹中的文件，请使用以下形式：<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\\" ) + 1 ) + "LinkFile.txt" |
| eeExFindNumberRange | 匹配 [数字范围表达式](../../howto/search/number_range_syntax)。此标志不能与 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindFuzzy | 使用模糊匹配。 |

## 版本

支持 EmEditor 16.0 或之后的版本。

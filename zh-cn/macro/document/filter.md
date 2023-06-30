# Filter 方法 (Document ����)

用指定的字符串以及设定来筛选文档。

#### \[JavaScript\]

_nCount_ = document. **Filter**( _strFilter_, _iColumn_, _flags_\[, _xBegin_\[, _xEnd_\[, _ExFlags_\[ _, nVisibleLinesAbove_\[ _, nVisibleLinesBelow_\]\]\]\]\] );

#### \[VBScript\]

_nCount_ = document. **Filter**( _strFilter_, _iColumn_, _flags_\[, _xBegin_\[, _xEnd_\[, _ExFlags_\[ _, nVisibleLinesAbove_\[ _, nVisibleLinesBelow_\]\]\]\]\] )

## 参数

_strFilter_

> 指定一个要搜索的字符串。如果指定了空字符串且ExFlags为0，则将中止当前筛选。

_iColumn_

> 指定你想要搜索的以 1 为基准的文本的列的索引；指定 0 ,如果你要搜索整行；或指定 -1 如果你要用字符数把开始以及结尾的文本指定为 _xBegin_ 和 _xEnd_。

_flags_

> 指定一个下列值的组合。
>
> |     |     |
> | --- | --- |
> | eeFindContinue | 指定下次调用的 Filter 方法不会清除筛选记录。在调用 Filter 方法之后，这个筛选不会被马上应用。你可以在你要进行多个级别的筛选时，使用这个标志。它与 eeFindKeepPrevious 标志相同，但由于实际的筛选不会在每次调用消息时被应用，这个方法更适用于多个筛选级别。 |
> | eeFindKeepPrevious | 指定 Filter 方法不能在应用新筛选前清除已存在的筛选记录。你可以在你要进行多个级别的筛选时，使用这个标志。 |
> | eeFindLogicalOr | 指定一个逻辑或运算 (logical OR) 到之前的层级上在多层级筛选的情况下。 |
> | eeFindNegative | 显示筛选工具栏并排除与指定字符串匹配的行。 |
> | eeFindRemoveLast | 删除前一次添加的筛选级别。 |
> | eeFindReplaceCase | 大小写需符合。 |
> | eeFindReplaceEscSeq | 使用转义序列。不能与 eeFindReplaceRegExp 或 eeExFindNumberRange 合用。 |
> | eeFindReplaceOnlyWord | 整个单词需匹配。 |
> | eeFindReplaceRegExp | 使用正则表达式搜索字符串。不能与 eeFindReplaceEscSeq 或 eeExFindNumberRange 合用。 |
> | eeFindWholeString | 匹配整个字符串。 |

_xBegin_

> 指定你想要搜索的文本的列开始的索引（用逻辑字符数）；你也可以指定 0 如果你想要把文本的最后一部分作为 _xEnd_。要使这个字段有效， _iColumn_ 值必须是 -1。

_xEnd_

> 指定你想要搜索的文本的列结束的索引（用逻辑字符数）；你也可以指定 0 如果你想要搜索所有剩下的文本。要使这个字段有效， _iColumn_ 值必须是 -1。

_ExFlags_

> 指定一个下列值的组合。
>
> |     |     |
> | --- | --- |
> | eeExFindBookmarkedOnly | 仅匹配书签行。此标志不能与 eeExFindUnbookmarkedOnly 合用。 |
> | eeExFindCrLf | 匹配换行符为“CR + LF”的行。此标志必须与 eeExFindMatchNL 结合使用。 |
> | eeExFindCrOnly | 匹配换行符为“仅 CR”的行。此标志必须与 eeExFindMatchNL 结合使用。 |
> | eeExFindFuzzy | 使用模糊匹配。 |
> | eeExFindLfOnly | 匹配换行符为“仅 LF”的行。此标志必须与 eeExFindMatchNL 结合使用。 |
> | eeExFindLinkFile | 指定 _strFilter_ 是链接文件的文件路径，该链接文件包含多个由换行符分隔的搜索字符串。如果一行中包含制表符，则搜索字符串是第一个不包含制表符的字符串。 _strFilter_ 可能是 EmEditor 安装路径的相对路径。它可能包含环境变量，例如 %USERPROFILE%。 |
> | eeExFindMatchNL | 匹配指定的换行符。此标志应与 eeExFindCrLf，eeExFindCrOnly，eeExFindLfOnly，和/或 eeExFindNLOthers 结合使用。 |
> | eeExFindNLOthers | 匹配没有换行符的行。这些行包括文件的最后一行以及非常长的行，例如继续到下一行而没有换行符的行。此标志必须与 eeExFindMatchNL 结合使用。 |
> | eeExFindNumberRange | 匹配 [数字范围表达式](../../howto/search/number_range_syntax)。此标志不能与 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 结合使用。 |
> | eeExFindUnbookmarkedOnly | 仅匹配不是书签行的行。此标志不能与 eeExFindBookmarkedOnly 合用。 |
> | eeExFilterBegin | 指定一个开始筛选。此标志不能与 eeExFilterEnd 合用。 |
> | eeExFilterEnd | 指定一个结束筛选。此标志不能与 eeExFilterBegin 合用。 |

_nVisibleLinesAbove_

> 指定要在匹配行上方显示的额外的可见行数。如果指定了 -1，则使用先前使用的值。

_nVisibleLinesBelow_

> 指定要在匹配行下方显示的额外的可见行数。如果指定了 -1，则使用先前使用的值。

## 返回值

返回值是与指定字符串匹配的行数。如果指定字符串是一个空字符串，返回值是 -1。如果指定的是 eeFindContinue，返回值则为 0。

## 版本

支持 EmEditor Professional 14.7 或之后的版本。
# GetCell 方法

在 CSV 模式中指定的单元格中检索文本。

#### \[JavaScript\]

_str_ = document. **GetCell**( _yLine_, _iColumn_, _flags_ );

#### \[VBScript\]

_str_ = document. **GetCell**( _yLine_, _iColumn_, _flags_ )

## 参数

_yLine_

指定要检索的文本的行号。

_iColumn_

指定要检索的文本的列索引。

_flags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | eeCellIncludeNone | 返回的文本不包括加在文本上的双引号或分隔符。 |
> | eeCellIncludeQuotes | 返回的文本可以包括加在文本上的双引号，但不包括分隔符。 |
> | eeCellIncludeQuotesAndDelimiter | 返回的文本可以包括加在文本上的双引号以及分隔符。 |

## 版本

支持 EmEditor Professional 14.7 或之后的版本。
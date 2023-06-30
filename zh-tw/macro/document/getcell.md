# GetCell 方法 (Document ��H)

在 CSV 模式中指定的單元格中檢索文字。

#### \[JavaScript\]

_str_ = document. **GetCell**( _yLine_, _iColumn_, _flags_ );

#### \[VBScript\]

_str_ = document. **GetCell**( _yLine_, _iColumn_, _flags_ )

## 參數

_yLine_

指定要檢索的文字的行號。

_iColumn_

指定要檢索的文字的列索引。

_flags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | eeCellIncludeNone | 返回的文字不包括加在文字上的雙引號或分隔符。 |
> | eeCellIncludeQuotes | 返回的文字可以包括加在文字上的雙引號，但不包括分隔符。 |
> | eeCellIncludeQuotesAndDelimiter | 返回的文字可以包括加在文字上的雙引號以及分隔符。 |

## 版本

支持 EmEditor Professional 14.7 或之後的版本。
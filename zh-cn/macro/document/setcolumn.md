# SetColumn 方法

在 CSV 模式下设置文本列。

#### \[JavaScript\]

document. **SetColumn**( _iColumn_, _strInsert_, _strDelimiter_, _flags_, _yTop_, _yLines_ );

#### \[VBScript\]

document. **SetColumn**( _iColumn_, _strInsert_, _strDelimiter_, _flags_, _yTop_, _yLines_ )

## 参数

_iColumn_

指定列的索引。

_strInsert_

指定要设置的字符串。字符串可以用在 strDelimiter 指定的分隔符分隔开。

_strDelimiter_

指定用于 strInsert 中分隔字符串的分隔符。如果空着或省略该参数，同样的字符串会用于列中的每一个单元格上。

_flags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | eeAutoQuote | 查看字符串是否包含分隔符，换行符，或引号，跳过这些字符，必要时添加引号。 |
> | eeDontQuote | 不做上述过程。 |
> | eeAlwaysQuote | 总是添加引号。 |

_yTop_

指定要设置的第一行的行号。如果省略，会默认为文件的首行。

_yLines_

指定要设置的行的行数。如果为零或省略，则不指定限制。

## 示例

下面的示例会在第三列的左边插入一个空列，并合并第一列和第二列的内容作为插入的这个列的内容。在运行这个宏之前，CSV文档必须处于活动状态。由于换行符 (\\n, Chr(10)) 被当作分隔符，我们假设每个单元格不包含换行符。

#### \[JavaScript\]

document.InsertColumn( 3 );

nLines = document.GetLines() - 1;

s3 = "";

for( y = 1; y <= nLines; y++ ) {

s1 = document.GetCell( y, 1, eeCellIncludeNone );

s2 = document.GetCell( y, 2, eeCellIncludeNone );

s3 += s1 + " " + s2 + "\\n";

}

document.SetColumn( 3, s3, "\\n", eeAutoQuote );

#### \[VBScript\]

document.InsertColumn 3

nLines = document.GetLines() - 1

s3 = ""

For y = 1 To nLines

s1 = document.GetCell( y, 1, eeCellIncludeNone )

s2 = document.GetCell( y, 2, eeCellIncludeNone )

s3 = s3 + s1 + " " + s2 + Chr(10)

Next

document.SetColumn 3, s3, Chr(10), eeAutoQuote

## 版本

支持 EmEditor Professional 16.7 或之后的版本。
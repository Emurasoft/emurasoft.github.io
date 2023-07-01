# SetCell 方法 (Document ����)

在 CSV 模式下指定的单元格中设置文本。

#### \[JavaScript\]

document. **SetCell**( _yLine_, _iColumn_, _str_, _flags_ );

#### \[VBScript\]

document. **SetCell**( _yLine_, _iColumn_, _str_, _flags_ )

## 参数

_yLine_

指定要设置的文本的行号。

_iColumn_

指定要设置的文本的列索引。

_str_

指定要设置的字符串。

_flags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | eeAutoQuote | 查看字符串是否包含分隔符，换行符，或引号，跳过这些字符，必要时添加引号。 |
> | eeDontQuote | 不做上述过程。 |
> | eeAlwaysQuote | 总是添加引号。 |

## 示例

下面的示例会在第三列的左边插入一个空列，并合并第一列和第二列的内容作为插入的这个列的内容。在运行这个宏之前，CSV文档必须处于活动状态。

#### \[JavaScript\]

document.InsertColumn( 3 );

nLines = document.GetLines() - 1;

for( y = 1; y <= nLines; y++ ) {

s1 = document.GetCell( y, 1, eeCellIncludeNone );

s2 = document.GetCell( y, 2, eeCellIncludeNone );

s3 = s1 + " " + s2;

document.SetCell( y, 3, s3, eeAutoQuote );

}

#### \[VBScript\]

document.InsertColumn 3

nLines = document.GetLines() - 1

For y = 1 To nLines

s1 = document.GetCell( y, 1, eeCellIncludeNone )

s2 = document.GetCell( y, 2, eeCellIncludeNone )

s3 = s1 + " " + s2

document.SetCell y, 3, s3, eeAutoQuote

Next

## 版本

支持 EmEditor Professional 16.7 或之后的版本。

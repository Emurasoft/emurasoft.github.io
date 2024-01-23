# GetColumn 方法 (Document 对象)

在 CSV 模式中检索文本列。

## 

### \[JavaScript\]

```
str = document.GetColumn( iColumn, strDelimiter, flags, yTop, yLines );
```

### \[VBScript\]

```
str = document.GetColumn( iColumn, strDelimiter, flags, yTop, yLines )
```

## 参数

_iColumn_

指定列的索引。

_strDelimiter_

指定分隔符来分隔输出的字符串。 此参数不能为空。

_flags_

指定下列值之一。eeCellDontCheckDelimiter 可以与其他标志之一组合使用。

|     |     |
| --- | --- |
| eeCellIncludeNone | 返回的文本不包括加在文本上的双引号或分隔符。 |
| eeCellIncludeQuotes | 返回的文本可以包括加在文本上的双引号，但不包括分隔符。 |
| eeCellIncludeQuotesAndDelimiter | 返回的文本可以包括加在文本上的双引号以及分隔符。 |
| eeCellDontCheckDelimiter | 设定如果每个单元格包含这个分隔符，该方法会失败。如果未指定，则该方法不会检查每个单元格是否包含分隔符。 |

_yTop_

指定要设置的第一行的行号。如果省略，会默认为文件的首行。

_yLines_

指定要设置为限制的行数。 如果为零或省略，则不指定限制。

## 示例

以下示例检索第一列，并插入一个与第一列长度相同的新列作为第二列。运行此宏之前，CSV文档必须处于活动状态。 由于使用换行符(\\n, Chr(10)) 作为分隔符，我们假定每个单元格不包含换行符。

### \[JavaScript\]

```
s1 = document.GetColumn( 1, "\n", eeCellIncludeNone );
sLines = s1.split("\\n");
s2 = "";
nTotal = sLines.length;
for( y = 0; y < nTotal; y++ ) {
count = sLines[y].length;
s2 += count + "\\n";
}
x = s2.length;
if( x > 0 ) s2 = s2.substr( 0, x - 1 );
document.InsertColumn( 2, s2, "\\n", eeDontQuote );
```

### \[VBScript\]

```
s1 = document.GetColumn( 1, Chr(10), eeCellIncludeNone )
sLines = Split( s1, Chr(10) )
s2 = ""
For Each s In sLines
count = Len(s)
s2 = s2 & CStr( count ) & Chr(10)
Next
x = Len( s2 )
If x > 0 Then s2 = Left( s2, x - 1 )
document.InsertColumn 2, s2, Chr(10), eeDontQuote
```

## 版本

支持 EmEditor Professional 16.8 或之后的版本。

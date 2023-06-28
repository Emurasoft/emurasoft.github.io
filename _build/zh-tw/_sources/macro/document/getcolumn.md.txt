# GetColumn 方法

在 CSV 模式中檢索文字欄。

#### \[JavaScript\]

_str_ = document. **GetColumn**( _iColumn_, _strDelimiter_, _flags_, _yTop_, _yLines_ );

#### \[VBScript\]

_str_ = document. **GetColumn**( _iColumn_, _strDelimiter_, _flags_, _yTop_, _yLines_ )

## 參數

_iColumn_

指定欄的索引。

_strDelimiter_

指定分隔符來分隔輸出的字串。 此參數不能為空。

_flags_

> 指定下列值之一。eeCellDontCheckDelimiter 可以與其他標志之一組合使用。
>
> |     |     |
> | --- | --- |
> | eeCellIncludeNone | 返回的文字不包括加在文字上的雙引號或分隔符。 |
> | eeCellIncludeQuotes | 返回的文字可以包括加在文字上的雙引號，但不包括分隔符。 |
> | eeCellIncludeQuotesAndDelimiter | 返回的文字可以包括加在文字上的雙引號以及分隔符。 |
> | eeCellDontCheckDelimiter | 設定如果每個儲存格包含這個分隔符，該方法會失敗。如果未指定，則該方法不會檢查每個儲存格是否包含分隔符。 |

_yTop_

指定要設置的第一行的行號。如果省略，會預設為檔案的首行。

_yLines_

指定要設置為限制的行數。 如果為零或省略，則不指定限制。

## 範例

以下範例檢索第一列，并插入一個與第一列長度相同的新列作為第二列。運行此巨集之前，CSV文檔必須處于活動狀態。 由于使用換行符號(\\n, Chr(10)) 作為分隔符，我們假定每個儲存格不包含換行符。

#### \[JavaScript\]

s1 = document.GetColumn( 1, "\\n", eeCellIncludeNone );

sLines = s1.split("\\n");

s2 = "";

nTotal = sLines.length;

for( y = 0; y < nTotal; y++ ) {

count = sLines\[y\].length;

s2 += count + "\\n";

}

x = s2.length;

if( x > 0 ) s2 = s2.substr( 0, x - 1 );

document.InsertColumn( 2, s2, "\\n", eeDontQuote );

#### \[VBScript\]

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

## 版本

支持 EmEditor Professional 16.8 或之後的版本。
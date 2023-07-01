# SetColumn 方法 (Document ��H)

在 CSV 模式下設置文字列。

#### \[JavaScript\]

document. **SetColumn**( _iColumn_, _strInsert_, _strDelimiter_, _flags_, _yTop_, _yLines_ );

#### \[VBScript\]

document. **SetColumn**( _iColumn_, _strInsert_, _strDelimiter_, _flags_, _yTop_, _yLines_ )

## 參數

_iColumn_

指定列的索引。

_strInsert_

指定要設置的字串。字串可以用在 strDelimiter 指定的分隔符分隔開。

_strDelimiter_

指定用於 strInsert 中分隔字串的分隔符。如果空著或省略該參數，同樣的字串會用於列中的每一個儲存格上。

_flags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | eeAutoQuote | 檢視字串是否包含分隔符，換行符號，或引號，跳過這些字元，必要時添加引號。 |
> | eeDontQuote | 不做上述過程。 |
> | eeAlwaysQuote | 總是添加引號。 |

_yTop_

指定要設置的第一行的行號。如果省略，會預設為檔案的首行。

_yLines_

指定要設置的行的行數。如果為零或省略，則不指定限制。

## 範例

下面的範例會在第三列的左邊插入一個空列，并合併第一列和第二列的內容作為插入的這個列的內容。在運行這個巨集之前，CSV文檔必須處于活動狀態。由于換行符號 (\\n, Chr(10)) 被當作分隔符，我們假設每個儲存格不包含換行符號。

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

支持 EmEditor Professional 16.7 或之後的版本。

# SetCell 方法 (Document ��H)

在 CSV 模式下指定的儲存格中設置文字。

#### \[JavaScript\]

document. **SetCell**( _yLine_, _iColumn_, _str_, _flags_ );

#### \[VBScript\]

document. **SetCell**( _yLine_, _iColumn_, _str_, _flags_ )

## 參數

_yLine_

指定要設置的文字的行號。

_iColumn_

指定要設置的文字的列索引。

_str_

指定要設置的字串。

_flags_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | eeAutoQuote | 檢視字串是否包含分隔符，換行符號，或引號，跳過這些字元，必要時添加引號。 |
> | eeDontQuote | 不做上述過程。 |
> | eeAlwaysQuote | 總是添加引號。 |

## 範例

下面的範例會在第三列的左邊插入一個空列，并合併第一列和第二列的內容作為插入的這個列的內容。在運行這個巨集之前，CSV文檔必須處于活動狀態。

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

支持 EmEditor Professional 16.7 或之後的版本。

# SetColumn メソッド

CSV モードで指定する列に文字列を設定します。

#### \[JavaScript\]

document. **SetColumn**( _iColumn_, _strInsert_, _strDelimiter_, _flags_, _yTop_, _yLines_ );

#### \[VBScript\]

document. **SetColumn**( _iColumn_, _strInsert_, _strDelimiter_, _flags_, _yTop_, _yLines_ )

## パラメータ

_iColumn_

列のインデックスを指定します。

_strInsert_

設定する文字列を指定します。文字列は、strDelimiter で指定される区切り文字で区切ることができます。

_strDelimiter_

strInsert で指定された文字列を区切る区切り文字列を指定します。これが空の場合、列のすべてのセルで同じ文字列が使用されます。

_flags_

> 次のいずれかの値を指定します。
>
> |     |     |
> | --- | --- |
> | eeAutoQuote | 文字列に区切り文字、改行、引用符が含まれていないかを確認し、必要なら自動的にエスケープを行い、引用符を追加します。 |
> | eeDontQuote | 上の処理を行いません。 |
> | eeAlwaysQuote | 常に引用符を追加します。 |

_yTop_

設定する最初の行の行番号を指定します。0 または省略すると、最初の行を指定します。

_yLines_

行数を制限として指定します。0 または省略すると、制限は指定されません。

## 例

次の例は、CSV文書の3列目の左側に空の列を挿入し、各行毎に、1列目と2列目を結合して3列目として設定します。このマクロを実行する前に、CSV文書がアクティブになっている必要があります。区切り文字として、改行文字 \\n, Chr(10) を使用しているため、各セルに改行文字が含まれていないと仮定しています。

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

## バージョン

EmEditor Professional Version 16.7 以上で利用できます。
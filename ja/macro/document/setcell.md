# SetCell メソッド

CSV モードで指定するセルに文字列を設定します。

#### \[JavaScript\]

document. **SetCell**( _yLine_, _iColumn_, _str_, _flags_ );

#### \[VBScript\]

document. **SetCell**( _yLine_, _iColumn_, _str_, _flags_ )

## パラメータ

_yLine_

行番号を指定します。

_iColumn_

列のインデックスを指定します。

_str_

設定するテキストを指定します。

_flags_

> 次のいずれかの値を指定します。
>
> |     |     |
> | --- | --- |
> | eeAutoQuote | 文字列に区切り文字、改行、引用符が含まれていないかを確認し、必要なら自動的にエスケープを行い、引用符を追加します。 |
> | eeDontQuote | 上の処理を行いません。 |
> | eeAlwaysQuote | 常に引用符を追加します。 |

## 例

次の例は、CSV文書の3列目の左側に空の列を挿入し、各行毎に、1列目と2列目を結合して3列目として設定します。このマクロを実行する前に、CSV文書がアクティブになっている必要があります。

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

## バージョン

EmEditor Professional Version 16.7 以上で利用できます。
# GetColumn メソッド (Document オブジェクト)

CSV モードで指定する列の文字列を取得します。

## 

### \[JavaScript\]

```
str = document.GetColumn( iColumn, strDelimiter, flags, yTop, yLines );
```

### \[VBScript\]

```
str = document.GetColumn( iColumn, strDelimiter, flags, yTop, yLines )
```

## パラメータ

_iColumn_

列のインデックスを指定します。

_strDelimiter_

出力文字列を区切るための区切り文字列を指定します。このパラメータには空の文字列を指定することはできません。

_flags_

次のいずれかの値を指定します。eeCellDontCheckDelimiter は、他の1個のフラグを組み合わせて指定できます。

|     |     |
| --- | --- |
| eeCellIncludeNone | 出力テキストには囲む2重引用符も区切り文字列も含まれません。 |
| eeCellIncludeQuotes | 出力テキストには囲む2重引用符が含まれますが、区切り文字列も含まれません。 |
| eeCellIncludeQuotesAndDelimiter | 出力テキストには囲む2重引用符も区切り文字列も含まれます。 |
| eeCellDontCheckDelimiter | 各セルが区切り文字列を含んでいるとメソッドが失敗するべきであることを指定します。これが指定されていない場合、メソッドは各セルが区切り文字列を含んでいるかどうかを調べません。 |

_yTop_

設定する最初の行の行番号を指定します。0 または省略すると、最初の行を指定します。

_yLines_

行数を制限として指定します。0 または省略すると、制限は指定されません。

## 例

次の例は、1列目を取得し、各セルの長さで新規列を2列目として挿入します。このマクロを実行する前に、CSV文書がアクティブになっている必要があります。区切り文字として、改行文字 \\n, Chr(10) を使用しているため、各セルに改行文字が含まれていないと仮定しています。

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

## バージョン

EmEditor Professional Version 16.8 以上で利用できます。

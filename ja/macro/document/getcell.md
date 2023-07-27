# GetCell メソッド ()

CSV モードで指定するセルのテキストを取得します。

## 

### \[JavaScript\]

```
str = document.GetCell( yLine, iColumn, flags );
```

### \[VBScript\]

```
str = document.GetCell( yLine, iColumn, flags )
```

## パラメータ

_yLine_

取得するテキストの行番号を指定します。

_iColumn_

取得するテキストの列のインデックスを指定します。

_flags_

次のいずれかの値を指定します。

|     |     |
| --- | --- |
| eeCellIncludeNone | 出力テキストには囲む2重引用符も区切り文字列も含まれません。 |
| eeCellIncludeQuotes | 出力テキストには囲む2重引用符が含まれますが、区切り文字列も含まれません。 |
| eeCellIncludeQuotesAndDelimiter | 出力テキストには囲む2重引用符も区切り文字列も含まれます。 |

## バージョン

EmEditor Professional Version 14.7 以上で利用できます。

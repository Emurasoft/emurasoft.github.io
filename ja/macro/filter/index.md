# Filter オブジェクト

## プロパティ

|     |     |
| --- | --- |
| [Enabled](enabled) | オブジェクトが有効どうか示すフラグを指定します。 |
| [Value](value) | 検索する文字列を指定します。 |
| [Column](column) | 取得するテキストの列の 1 から始まるインデックスを指定します。0 を指定すると行全体から検索します。-1 を指定すると Begin と End パラメータによってテキストの開始位置と終了位置を指定します。 |
| [Flags](flags) | フラグを組み合わせて指定します。 |
| [Begin](begin) | 検索したいテキストの開始位置のインデックスを論理文字単位で指定します。テキストの最後から数えて End で指定する場合には 0 を指定します。このフィールドを有効にするには Column パラメータに -1 を指定する必要があります。 |
| [End](end) | 検索したいテキストの終了位置のインデックスを論理文字単位で指定します。最後まで全部を検索する場合には 0 を指定します。このフィールドを有効にするには Column パラメータに -1 を指定する必要があります。 |
| [ExFlags](exflags) | フラグを組み合わせて指定します。 |
| [Replace](replace) | 置換後の文字列を指定します。 |

## バージョン

EmEditor Professional Version 16.0 以上で利用できます。


```{toctree}
:hidden:
:maxdepth: 1
begin
column
enabled
end
exflags
flags
replace
value
```

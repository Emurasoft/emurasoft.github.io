# NUMBERING\_INFO

[EE\_NUMBERING メッセージ](../message/ee_numbering) で使用します。

typedef struct \_NUMBERING\_INFO {

UINT cbSize;

UINT nFlags;

LPCWSTR pszFirst;

LPCWSTR pszInc;

INT64 nMaxLines;

} NUMBERING\_INFO;

## フィールド

_cbSize_

> このデータ構造体のサイズ、sizeof( NUMBERING\_INFO )を指定します。

_nFlags_

> 次の値の組み合わせを指定することができます。
>
> | 値 | 意味 |
> | --- | --- |
> | NUM\_FLAG\_CAPITAL\_LETTERS | 16 進数を大文字で挿入します。 |
> | NUM\_FLAG\_SKIP\_EMPTY\_LINES | 箱型選択または複数選択を行っている場合、空行をスキップして数字を挿入するかどうかを指定します。 |
> | NUM\_FLAG\_RESTART\_NUM\_EMPTY | 箱型選択または複数選択を行っている場合、空行の後、番号を最初から数え直すかどうかを指定します。 |
> | NUM\_FLAG\_RESTART\_NUM\_DISCONTINUOUS | 複数選択を行っている場合、不連続行で番号を最初から数え直すかどうかを指定します。 |
> | NUM\_FLAG\_DECIMAL | 番号を 10 進数で指定します。 |
> | NUM\_FLAG\_HEXADECIMAL | 番号を 16 進数で指定します。 |
> | NUM\_FLAG\_OCTAL | 番号を 8 進数で指定します。 |
> | NUM\_FLAG\_BINARY | 番号を 2 進数で指定します。 |
> | NUM\_FLAG\_OTHER | 番号の代わりに文字を挿入します。\[最初の行\] テキスト ボックスで指定した文字から始まり、\[増加量\] テキスト ボックスで指定する Unicode の文字コード値の増加量で連続する文字を挿入します。1 行に 1 文字のみ挿入することができます。 |

_pszFirst_

> 最初の行に挿入する初期値または文字を指定します。

_pszInc_

> 増加量を 10 進数で指定します。これは最初の行と 2 番目の行の値の差になります。

_nMaxLines_

> 行数を 10 進数で指定します。

## バージョン

> Version 19.1 以上で利用できます。
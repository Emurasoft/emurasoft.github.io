# SPLIT\_COLUMN\_INFO

[EE\_SPLIT\_COLUMN メッセージ](../message/ee_split_column) で使用します。

```
typedef struct _SPLIT_COLUMN_INFO {
	UINT cbSize;
	UINT nType;
	UINT nFlags;
	int* anColumns;
	int nNumOfColumns;
	int nLimit;
	LPCWSTR pszSeparator;
	LPCWSTR pszLocale;
} SPLIT_COLUMN_INFO;
```

## フィールド

_cbSize_

このデータ構造体のサイズ、sizeof( SPLIT\_COLUMN\_INFO )を指定します。

_nType_

次の値のいずれかを指定することができます。

| 値 | 意味 |
| --- | --- |
| COLUMN\_SPLIT\_TO\_COLUMNS | 指定した列を、区切り文字で分割して右の列に置きます。 |
| COLUMN\_SPLIT\_TO\_LINES | 指定した列を、区切り文字で分割して下の行に置きます。 |
| COLUMN\_SPLIT\_TO\_NONE | 指定した列を、区切り文字で分割しませんが、並べ替えまたは分割後の重複文字列を削除します。 |

_nFlags_

次の値の組み合わせを指定します。分割文字列を並べ替えるには SORT\_ENABLED を指定する必要があり、他のフラグと組み合わせて並べ替えの動作を指定します。重複した分割文字列を削除するには SORT\_DELETE\_DUPLICATE を指定する必要があります。

|     |     |
| --- | --- |
| NORM\_IGNORECASE | 大文字と小文字を区別しないで並べ替えます。 |
| NORM\_IGNOREKANATYPE | ひらがなとカタカナを区別しないで並べ替えます。 |
| NORM\_IGNORENONSPACE | 場所を取らない文字を区別しないで並べ替えます。 |
| NORM\_IGNORESYMBOLS | 記号を無視して並べ替えます。 |
| NORM\_IGNOREWIDTH | 半角文字と全角文字の違いは無視されます。例えば、「Ｃａｔ」と「cat」は同一とみなされます。全角文字は中国語と日本語の文章で使用されているフォーマットです。 |
| SORT\_BINARY\_COMPARISON | ロケールを無視して、高速にバイナリ比較を行います。 |
| SORT\_DATE | 日付と時刻で並べ替えます。 |
| SORT\_DELETE\_DUPLICATE | 重複した分割文字列を削除します。 |
| SORT\_DIGITSASNUMBERS | \[AからZへ並べ替え\] コマンドまたは \[ZからAへ並べ替え\] コマンドを使用時でも、数字が数として扱われます。例えば、「2」は「10」の前に並べ替えられます。 |
| SORT\_ENABLED | 分割文字列を並べ替えます。 |
| SORT\_IGNORE\_PREFIX | 数字を並べ替える際、先頭の数字以外の文字は無視されます。 |
| SORT\_INSPECT\_NOT\_SEL\_ONLY | 箱型選択または複数選択が存在する時でも、行全体を調べます。 |
| SORT\_IPV4 | IPv4 アドレスを並べ替えます。 |
| SORT\_IPV6 | IPv6 アドレスを並べ替えます。 |
| SORT\_LENGTH | 文字数で並べ替えます。 |
| SORT\_LENGTH\_VIEW | \[短い文字列から長い文字列へ並べ替え\] コマンドまたは \[長い文字列から短い文字列へ並べ替え\] コマンドを使用時、全角文字が2文字として扱われます。 |
| SORT\_NUM | 数字を並べ替えます。 |
| SORT\_GROUP\_IDENTICAL | 出現頻度で並べ替える時、同じ文字列をグループ化します。SORT\_OCCURRENCE と共に指定する必要があります。 |
| SORT\_OCCURRENCE | 出現頻度で並べ替えます。 |
| SORT\_RANDOM | ランダムに並べ替えます。 |
| SORT\_REVERSE | 逆順に並べ替えます。 |
| SORT\_STABLE | 常に順位の位置関係を保ったままソートを行います。このフラグが指定されていると、指定されていない場合に比べて、通常、遅くなります。 |
| SORT\_STRINGSORT | 句読点が記号と同様に扱われます。 |
| SORT\_TEXT | テキストを並べ替えます。 |
| SORT\_WORDS | 単語数で並べ替えます。 |
| SPLIT\_DONT\_DISCARD\_EXTRA | nLimit が 0 でない時、余分な文字列を破棄しません。 |

_anColumns_

0 で始まるインデックスを含む整数の配列を指定します。

_nNumOfColumns_

anColumns で指定した列の数を指定します。

_nLimitTo_

セル毎の分割の最大数を指定します。

_pszSeparator_

列を分割する際に使用する区切り文字列を指定します。

_pszLocale_

並べ替えで使用するロケールを指定します。これが空の場合、カスタマイズ ダイアログ ボックスで指定されているロケールを使用します。

## バージョン

Version 19.9 以上で利用できます。

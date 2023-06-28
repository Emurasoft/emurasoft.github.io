# Editor\_PivotTable

CSV 文書のピボット テーブルを作成します。このインライン関数を使うか、または [EE\_PIVOT\_TABLE](../message/ee_pivot_table) メッセージを直接送ることができます。

HRESULT Editor\_PivotTable( HWND hwnd, int iRow, int iColumn, int iValue, UINT nFlags, UINT nSortRow, UINT nSortColumn, LPCWSTR pszLocale, LPCWSTR pszTotalRowLabel, LPCWSTR pszTotalColLabel, int nDecimalPlaces );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iRow_

> 新規ピボット テーブルで行に展開する CSV 文書の列のインデックスを指定します。

_iColumn_

> 新規ピボット テーブルで列に展開する CSV 文書の列のインデックスを指定します。

_iValue_

> 新規ピボット テーブルで値に展開する CSV 文書の列のインデックスを指定します。

_nFlags_

> 次の値の組み合わせを指定することができます。
>
> |     |     |
> | --- | --- |
> | PIVOT\_TYPE\_COUNT | 値の数。 |
> | PIVOT\_TYPE\_SUM | 値の合計。 |
> | PIVOT\_TYPE\_AVERAGE | 値の平均値。 |
> | PIVOT\_TYPE\_MAX | 最大値。 |
> | PIVOT\_TYPE\_MIN | 最小値。 |
> | PIVOT\_FLAG\_TOTAL\_ROW | 行の合計を表示します。 |
> | PIVOT\_FLAG\_TOTAL\_COL | 列の合計を表示します。 |

_nSortRow_

> 行に適用する並べ替えのためのフラグの組み合わせを指定します。0 の場合、並べ替えは行われません。
>
> |     |     |
> | --- | --- |
> | NORM\_IGNORECASE | 大文字と小文字を区別しないで並べ替えます。 |
> | NORM\_IGNOREKANATYPE | ひらがなとカタカナを区別しないで並べ替えます。 |
> | NORM\_IGNORENONSPACE | 場所を取らない文字を区別しないで並べ替えます。 |
> | NORM\_IGNORESYMBOLS | 記号を無視して並べ替えます。 |
> | NORM\_IGNOREWIDTH | 半角文字と全角文字の違いは無視されます。例えば、「Ｃａｔ」と「cat」は同一とみなされます。全角文字は中国語と日本語の文章で使用されているフォーマットです。 |
> | SORT\_BINARY\_COMPARISON | ロケールを無視して、高速にバイナリ比較を行います。 |
> | SORT\_DATE | 日付と時刻で並べ替えます。 |
> | SORT\_DIGITSASNUMBERS | \[AからZへ並べ替え\] コマンドまたは \[ZからAへ並べ替え\] コマンドを使用時でも、数字が数として扱われます。例えば、「2」は「10」の前に並べ替えられます。 |
> | SORT\_ENABLED | 分割文字列を並べ替えます。 |
> | SORT\_IGNORE\_PREFIX | 数字を並べ替える際、先頭の数字以外の文字は無視されます。 |
> | SORT\_INSPECT\_NOT\_SEL\_ONLY | 箱型選択または複数選択が存在する時でも、行全体を調べます。 |
> | SORT\_IPV4 | IPv4 アドレスを並べ替えます。 |
> | SORT\_IPV6 | IPv6 アドレスを並べ替えます。 |
> | SORT\_LENGTH | 文字数で並べ替えます。 |
> | SORT\_LENGTH\_VIEW | \[短い文字列から長い文字列へ並べ替え\] コマンドまたは \[長い文字列から短い文字列へ並べ替え\] コマンドを使用時、全角文字が2文字として扱われます。 |
> | SORT\_NUM | 数字を並べ替えます。 |
> | SORT\_GROUP\_IDENTICAL | 出現頻度で並べ替える時、同じ文字列をグループ化します。SORT\_OCCURRENCE と共に指定する必要があります。 |
> | SORT\_OCCURRENCE | 出現頻度で並べ替えます。 |
> | SORT\_RANDOM | ランダムに並べ替えます。 |
> | SORT\_REMOVE\_EMPTY | 空の文字列を削除します。 |
> | SORT\_REVERSE | 逆順に並べ替えます。 |
> | SORT\_STABLE | 常に順位の位置関係を保ったままソートを行います。このフラグが指定されていると、指定されていない場合に比べて、通常、遅くなります。 |
> | SORT\_STRINGSORT | 句読点が記号と同様に扱われます。 |
> | SORT\_TEXT | テキストを並べ替えます。 |
> | SORT\_WORDS | 単語数で並べ替えます。 |

_nSortColumn_

> 行に適用する並べ替えのためのフラグの組み合わせを指定します。0 の場合、並べ替えは行われません。使用できるフラグは _nSortRow_ パラメータと同じです。

_pszLocale_

> 並べ替えで使用するロケールを指定します。これが空の場合、\[カスタマイズ\] ダイアログ ボックスで \[並べ替え\] ページで指定されているロケールを使用します。

_pszTotalRowLabel_

> 行の合計値に使用するヘディングのラベルを指定します。このパラメータは、 _nFlags_ パラメータに PIVOT\_FLAG\_TOTAL\_ROW が指定されている場合のみ使用されます。

_pszTotalColLabel_

> 列の合計値に使用するヘディングのラベルを指定します。このパラメータは、 _nFlags_ パラメータに PIVOT\_FLAG\_TOTAL\_COL が指定されている場合のみ使用されます。

_nDecimalPlaces_

> 値の小数点以下の桁数を指定します。

## 戻り値

> 失敗すると負の値を返します。

## バージョン

> Version 21.4 以上で利用できます。
# Editor\_Sort

文書を並べ替えます。このインライン関数を使うか、または [EE\_SORT](../message/ee_sort) メッセージを直接送ることができます。

Editor\_Sort( HWND hwnd, UINT nFlags, LPCWSTR pszLocale, int nNumOfColumns, COLUMN\_INFO\* anColumns, BOOL\* pbModified );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

> 次の値の組み合わせを指定します。
>
> |     |     |
> | --- | --- |
> | NORM\_IGNORECASE | 大文字と小文字を区別しないで並べ替えます。 |
> | NORM\_IGNOREKANATYPE | ひらがなとカタカナを区別しないで並べ替えます。 |
> | NORM\_IGNORENONSPACE | 場所を取らない文字を区別しないで並べ替えます。 |
> | NORM\_IGNORESYMBOLS | 記号を無視して並べ替えます。 |
> | NORM\_IGNOREWIDTH | 半角文字と全角文字の違いは無視されます。例えば、「Ｃａｔ」と「cat」は同一とみなされます。全角文字は中国語と日本語の文章で使用されているフォーマットです。 |
> | SORT\_BINARY\_COMPARISON | ロケールを無視して、高速にバイナリ比較を行います。 |
> | SORT\_COLUMNS | 列を並べ替えます。これが指定されていない場合、行を並べ替えます。 |
> | SORT\_DATE | 日付と時刻で並べ替えます。 |
> | SORT\_DELETE\_DUPLICATE | SORT\_COLUMNS と共に指定されている場合、指定行の重複するセルを削除します。 |
> | SORT\_DIGITSASNUMBERS | \[AからZへ並べ替え\] コマンドまたは \[ZからAへ並べ替え\] コマンドを使用時でも、数字が数として扱われます。例えば、「2」は「10」の前に並べ替えられます。 |
> | SORT\_DIGIT\_GROUPING | 数字に桁区切りを許可します。 |
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
> | SORT\_REMOVE\_EMPTY | SORT\_COLUMNS と共に指定されている場合、空のセルを削除します。 |
> | SORT\_REVERSE | 逆順に並べ替えます。 |
> | SORT\_SELECTION\_ONLY | 選択された行のみ並べ替えます。 |
> | SORT\_STABLE | 常に順位の位置関係を保ったままソートを行います。このフラグが指定されていると、指定されていない場合に比べて、通常、遅くなります。 |
> | SORT\_STRINGSORT | 句読点が記号と同様に扱われます。 |
> | SORT\_TEXT | テキストを並べ替えます。 |
> | SORT\_UNQUOTE\_CELLS | CSV 文書で引用符を取り除いた文字列で比較します。例えば、セル文字列が _"a""b"_ の場合、実際に比較する文字列は _a"b_ になります。 |
> | SORT\_WORDS | 単語数で並べ替えます。 |

_pszLocale_

> 並べ替えで使用するロケールを指定します。これが空の場合、カスタマイズ ダイアログ ボックスで指定されているロケールを使用します。

_bModified_

> メッセージが処理されて文書が変更されると、このフィールドは TRUE が設定されます。そうでない場合は、FALSE が設定されます。

_nNumOfColumns_

> _anColumns_ パラメータに指定されているカラムの数を指定します。

_anColumns_

> 重複行を調べる列とフラグを含む COLUMN\_INFO 構造体の配列を指定します。このフィールドは NULL にすることはできません。

## 戻り値

> 戻り値は HRESULT 値になります。0 以上の整数は成功を意味し、0 未満の整数は失敗を意味します。

## バージョン

> Version 16.4 以上で利用できます。
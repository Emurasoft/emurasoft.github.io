# Editor\_ManageDuplicates

重複行を削除またはブックマークします。このインライン関数を使うか、または [EE\_MANAGE\_DUPLICATES](../message/ee_manage_duplicates) メッセージを直接送ることができます。

Editor\_ManageDuplicates( HWND hwnd, UINT nFlags, int nNumOfColumns, int\* anColumns, INT\_PTR\* pnFound, int nNumOfColumnsToCombine = 0, int\* anColumnsToCombine = NULL, LPCWSTR pszInsert = NULL, UINT nCombineFlags = 0, LPWSTR pszLocale = NULL );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| MANAGE\_DUPLICATES\_ADJACENT\_ONLY | 隣接する行のみを調べます。このフラグは文書が既に並べ替えられている場合に使用すると便利です。 |
| MANAGE\_DUPLICATES\_BOOKMARK | 重複行にブックマークを設定します。このフラグが指定されていない場合は、重複行を削除します。 |
| MANAGE\_DUPLICATES\_COMBINE | CSV 文書の上下隣の重複したセルを結合します。 |
| MANAGE\_DUPLICATES\_IGNORE\_CASE | 大文字と小文字を区別しません。 |
| MANAGE\_DUPLICATES\_IGNORE\_EMPTY\_CELLS | CSV 文書の場合、空のセルを無視します。複数の列が指定されている場合、指定した列のすべてのセルが空である必要があります。 |
| MANAGE\_DUPLICATES\_IGNORE\_EMPTY\_LINES | 空行を無視します。 |
| MANAGE\_DUPLICATES\_INCLUDE\_ALL | 各重複のすべての行を削除、または各重複のすべての行にブックマークを設定します。 |
| MANAGE\_DUPLIDATES\_INSPECT\_SEL\_ONLY | 箱型選択または複数選択が存在する時、選択された文字列のみを調べます。 |
| MANAGE\_DUPLICATES\_SELECTION\_ONLY | 選択範囲のみ調べます。 |

_nNumOfColumns_

_anColumns_ パラメータに指定されているカラムの数を指定します。これが 0 だと行全体が指定されることになります。

_anColumns_

重複行を調べる列の 0 を基底とするインデックスの配列を指定します。 _nNumOfColumns_ パラメータが 0 の場合 NULL を指定することができます。

_pnFound_

削除またはブックマークされた (既にブックマークされている行も含む) 行数が格納されます。

_nNumOfColumns_

_anColumns_ フィールドに指定されているカラムの数を指定します。これが 0 だと行全体が指定されることになります。

_anColumns_

重複行を調べるカラムの 0 を基底とするインデックスの配列を指定します。 _nNumOfColumns_ フィールドが 0 の場合 NULL を指定することができます。

_nNumOfColumnsToCombine_

_anColumnsToCombine_ フィールドに指定されているカラムの数を指定します。

_anColumnsToCombine_

結合するカラムの 0 を基底とするインデックスの配列を指定します。 _nNumOfColumns_ フィールドが 0 の場合 NULL を指定することができます。

_pszInsert_

CSV 文書の上下隣の重複したセルを結合する時に挿入する文字列を指定します。

_nFlags_

次の値の組み合わせを指定します。文字列を並べ替えるには SORT\_ENABLED を指定する必要があり、他のフラグと組み合わせて並べ替えの動作を指定します。重複した文字列を削除するには SORT\_DELETE\_DUPLICATE を指定する必要があります。

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
| SORT\_REMOVE\_EMPTY | 空の文字列を削除します。 |
| SORT\_REVERSE | 逆順に並べ替えます。 |
| SORT\_STABLE | 常に順位の位置関係を保ったままソートを行います。このフラグが指定されていると、指定されていない場合に比べて、通常、遅くなります。 |
| SORT\_STRINGSORT | 句読点が記号と同様に扱われます。 |
| SORT\_TEXT | テキストを並べ替えます。 |
| SORT\_WORDS | 単語数で並べ替えます。 |

_pszLocale_

並べ替えで使用するロケールを指定します。これが空の場合、カスタマイズ ダイアログ ボックスで指定されているロケールを使用します。

## 戻り値

戻り値は HRESULT 値になります。0 以上の整数は成功を意味し、0 未満の整数は失敗を意味します。

## バージョン

Version 16.4 以上で利用できます。

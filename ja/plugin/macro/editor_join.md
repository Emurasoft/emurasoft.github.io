# Editor\_Join

SQL においての JOIN 操作と同様な方法を使って、2個の CSV 文書を結合して新規文書を作成します。このインライン関数を使うか、または [EE\_JOIN](../message/ee_join) メッセージを直接送ることができます。

Editor\_Join( HWND hwnd, UINT nFlags, LPCWSTR pszDocument1, LPCWSTR pszColumn1, LPCWSTR pszDocument2, LPCWSTR pszColumn2, LPCWSTR pszSelect, int\* piDocument3 );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

> 次の値を組み合わせて指定します。
>
> |     |     |
> | --- | --- |
> | JOIN\_FLAG\_UNIQUE\_KEY\_1 | 第1文書の指定した列には一意キーが含まれます。 |
> | JOIN\_FLAG\_UNIQUE\_KEY\_2 | 第2文書の指定した列には一意キーが含まれます。 |
> | JOIN\_FLAG\_INCLUDE\_ALL\_1 | 第1文書のすべての行が出力に含まれます。第1文書にマッチしない行が存在する場合、出力文書には空のセルが含まれます。 |
> | JOIN\_FLAG\_INCLUDE\_ALL\_2 | 第2文書のすべての行が出力に含まれます。第2文書にマッチしない行が存在する場合、出力文書には空のセルが含まれます。 |
> | JOIN\_FLAG\_MATCH\_CASE | 大文字と小文字を区別します。 |
> | JOIN\_FLAG\_SIMPLE\_JOIN | キーを使用しないで、単純に結合します。これを指定した場合、 _pszColumn1_ と _pszColumn2_ パラメータは無視されます。 |
> | JOIN\_FLAG\_IGNORE\_HEADINGS\_1 | 第1文書のヘディングを無視します。第1文書のヘディングは、結合された文書に残ります。 |
> | JOIN\_FLAG\_IGNORE\_HEADINGS\_2 | 第2文書のヘディングを無視します。 |
> | JOIN\_FLAG\_CONTAIN | Key1 は Key2 を含みます。 |
> | JOIN\_FLAG\_START\_WITH | Key1 は Key2 から始まります。 |
> | JOIN\_FLAG\_END\_WITH | Key1 は Key2 で終わります。 |
> | JOIN\_FLAG\_MATCH\_SPLIT\_BOTH | 両方の分割文字列が一致します。 |
> | JOIN\_FLAG\_MATCH\_SPLIT\_ONE | Key1 は 分割した Key2 に一致します。 |
> | JOIN\_FLAG\_FUZZY | あいまい一致を使用します。このフラグは、JOIN\_FLAG\_END\_WITH、JOIN\_FLAG\_MATCH\_SPLIT\_BOTH、または JOIN\_FLAG\_MATCH\_SPLIT\_ONE と共に指定することはできません。このフラグは動作を遅くします。 |
> | JOIN\_FLAG\_SWAP | JOIN\_FLAG\_CONTAIN、JOIN\_FLAG\_START\_WITH、または JOIN\_FLAG\_END\_WITH と共に指定されている場合、Key1 と Key2 を入れ替えます。 |

_pszDocument1_

> 第1文書を特定する文字列を指定します。この値は、ファイル名、完全パスの付いたファイル名、またはコロン (:) で始まる現在のグループ内の文書のインデックスになります。例えば、"filename.csv"、"C:\\data\\filename.csv"、または ":2" と指定することができます。

_pszColumn1_

> 第1文書のキー列を特定する文字列を指定します。この値は、列の最初の行、またはコロン (:) で始まる列のインデックスになります。例えば、"first\_name"、":5" と指定することができます。

_pszDocument2_

> 第2文書を特定する文字列を指定します。この値のフォーマットは strDocument1 と同じです。

_pszColumn2_

> 第2文書のキー列を特定する文字列を指定します。この値のフォーマットは strColumn1 と同じです。

_pszSelect_

> 出力文書にどの列を選択するかを示す文字列を指定します。例えば、"file1.csv>column1,file2.csv>column2" と指定することができます。

_piDocument3_

> 関数が戻ると、このフィールドは出力文書のインデックスが代入されます。これが NULL の場合、このフィールドは無視されます。

## 戻り値

> 戻り値は、出力文書の行数になります。エラーが発生すると戻り値は負の数になります。エラーが発生すると、戻り値は次のいずれかの値になることがあります。
>
> |     |     |
> | --- | --- |
> | E\_DOCUMENT\_1\_NOT\_FOUND | 第1文書が見つかりません。 |
> | E\_DOCUMENT\_2\_NOT\_FOUND | 第2文書が見つかりません。 |
> | E\_COLUMN\_1\_NOT\_FOUND | 1列目が見つかりません。 |
> | E\_COLUMN\_2\_NOT\_FOUND | 2列目が見つかりません。 |
> | E\_SELECT\_SYNTAX | 選択文字列の中に構文エラーがあります。 |
> | E\_SELECT\_DOCUMENT\_NOT\_FOUND | 選択文字列の中に指定した文書が見つかりません。 |
> | E\_SELECT\_COLUMN\_NOT\_FOUND | 選択文字列の中に指定した列が見つかりません。 |
> | E\_DIFFERENT\_CSV\_MODE | 異なる CSV モードです。 |
> | E\_NOT\_MDI | タブが有効になっている必要があります。 |
> | E\_WRITE\_TEMP\_FILE | 一時ファイルの書き込みエラー。 |
> | E\_ABORT | ユーザーによって中止されました。 |
> | E\_FAIL | 詳細不明のエラー。 |

## バージョン

> Version 14.8 以上で利用できます。

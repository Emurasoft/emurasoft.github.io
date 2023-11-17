# Editor\_FindReplace

文字列を検索または置換します。このインライン関数を使うか、または [EE\_FIND\_REPLACE メッセージ](../message/ee_find_replace) を直接送ることができます。

HRESULT Editor\_FindReplace( HWND hwnd, UINT64 nFlags, LPCWSTR pszFind, LPCWSTR pszReplace, UINT64\* pnCount, UINT64\* pnMatchedLines );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

次の値の組み合わせになります。

| 定数 | 説明 |
| --- | --- |
| FLAG\_FIND\_AROUND | 文末(文頭)まで検索したら、文頭(文末)に移動する。 |
| FLAG\_FIND\_BOOKMARK | 見つかった行にブックマークを設定します。 |
| FLAG\_FIND\_CASE | 大文字と小文字を区別します。 |
| FLAG\_FIND\_COUNT | 文字列の一致する数を数えます。 |
| FLAG\_FIND\_EMBEDDED\_NL | CSV文書に埋め込まれた改行コードを検索し、その他の改行コードは検索しません。 |
| FLAG\_FIND\_ESCAPE | エスケープ シーケンスを使用します。 |
| FLAG\_FIND\_EXTRACT | 見つかった行を抽出して新規文書を作成します。 |
| FLAG\_FIND\_FUZZY | あいまい一致を使用します。 |
| FLAG\_FIND\_NEXT | カーソル位置より下方向に検索します。これが指定されていない場合、上方向に検索します。 |
| FLAG\_FIND\_NO\_PROMPT | 検索する文字列が見つからなくてもプロンプト ダイアログ ボックスを表示しません。 |
| FLAG\_FIND\_ONLY\_WORD | 単語のみ選択します。 |
| FLAG\_OPEN\_DOC | 同じフレーム ウィンドウ内に開いているすべての文書から検索します。 |
| FLAG\_FIND\_REG\_EXP | 正規表現を使って検索します。 |
| FLAG\_FIND\_REGEX\_BOOST | 正規表現エンジンとして Regex.Boost を使用します。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 正規表現エンジンとして Onigmo を使用します。 |
| FLAG\_FIND\_SAVE\_HISTORY | 次の検索用に、検索文字列を保存します。 |
| FLAG\_FIND\_SELECT\_ALL | 一致する文字列をすべて選択します。 |
| FLAG\_FIND\_SEL\_ONLY | 選択範囲のみ検索します。 |
| FLAG\_REPLACE\_ALL | すべて置換します。 |
| FLAG\_REPLACE\_SEL\_ONLY | すべて置換の場合に選択範囲のテキストのみを対象とします。FLAG\_REPLACE\_ALL とともに指定する必要があります。 |

_pszFind_

\[in\] 検索する文字列 を指定します

_pszReplace_

\[in\] 置換後の文字列を指定します。置換でない場合には、NULL を指定する必要があります。

_pnCount_

\[out\] nFlags が FLAG\_FIND\_COUNT, FLAG\_FIND\_BOOKMARK, FLAG\_FIND\_SELECT\_ALL, FLAG\_FIND\_EXTRACT or FLAG\_FIND\_FILTER を含んでいる場合、一致する数を受け取る変数へのポインタを指定します。

_pnMatchedLines_

\[out\] nFlags が FLAG\_FIND\_COUNT, FLAG\_FIND\_BOOKMARK, FLAG\_FIND\_SELECT\_ALL, FLAG\_FIND\_EXTRACT or FLAG\_FIND\_FILTER を含んでいる場合、一致する行数を受け取る変数へのポインタを指定します。

## バージョン

Version 15.7 以上で利用できます。

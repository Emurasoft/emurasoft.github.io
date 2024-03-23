# Editor\_FindA

ANSI文字列を検索します。このインライン関数を使うか、または [EE\_FINDA](../message/ee_finda)
メッセージを直接送ることができます。

Editor\_FindA( HWND hwnd, UINT nFlags, LPCSTR szFind )

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

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
| FLAG\_FIND\_FILTER | フィルター ツール バーを表示して指定する文字列に一致する行のみを表示します。このフラグが指定されている場合、FLAG\_FIND\_AROUND、FLAG\_FIND\_BOOKMARK、FLAG\_FIND\_COUNT、FLAG\_FIND\_EXTRACT、LAG\_FIND\_NEXT、FLAG\_FIND\_OPEN\_DOC、FLAG\_FIND\_NO\_PROMPT、FLAG\_FIND\_SEL\_ONLY、FLAG\_FIND\_SAVE\_HISTORY、または FLAG\_FIND\_SELECT\_ALL とともに指定することはできません。 |
| FLAG\_FIND\_NEGATIVE | フィルター ツール バーを表示して指定する文字列に一致する行を除外します。このフラグは、FLAG\_FIND\_FILTER フラグとともに指定する必要があります。 |
| FLAG\_FIND\_NEXT | カーソル位置より下方向に検索します。これが指定されていない場合、上方向に検索します。 |
| FLAG\_FIND\_NO\_PROMPT | 検索する文字列が見つからなくてもプロンプト ダイアログ ボックスを表示しません。 |
| FLAG\_FIND\_ONLY\_WORD | 単語のみ選択します。 |
| FLAG\_OPEN\_DOC | 同じフレーム ウィンドウ内に開いているすべての文書から検索します。 |
| FLAG\_FIND\_REG\_EXP | 正規表現を使って検索します。 |
| FLAG\_FIND\_SAVE\_HISTORY | 次の検索用に、検索文字列を保存します。 |
| FLAG\_FIND\_SELECT\_ALL | 一致する文字列をすべて選択します。 |
| FLAG\_FIND\_SEL\_ONLY | 選択範囲のみ検索します。 |

_szFind_

検索する文字列 を指定します。

## 戻り値

文字列が見つかった場合は 1 を返します。見つからない場合は 0 を返します。ただし、eeFindCount フラグが指定されている場合、戻り値は文書内で一致した文字列の数になります。しかし、検索文字列がカーソル位置より指定した方向に見つからない場合は、残りの文書で一致している場合でも、戻り値は 0 になります。FLAG\_FIND\_FILTER
が指定されている場合、戻り値は指定する文字列に一致する行数になります。指定文字列が空で FLAG\_FIND\_FILTER が指定されている場合、戻り値は -1 になります。

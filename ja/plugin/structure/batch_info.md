# BATCH\_INFO

[EE\_FIND\_REPLACE \
メッセージ](../message/ee_find_replace) で使用します。

typedef struct \_BATCH\_INFO {

UINT cbSize;

UINT nBatchCount;

UINT64 nBatchFlags;

UINT64 nTotalCount;

} BATCH\_INFO;

## フィールド

_cbSize_

sizeof( BATCH\_INFO ) を指定します。

_nBatchCount_

_lParam_ に指定されている FIND\_REPLACE\_INFO 構造体の数を指定します。

_nBatchFlags_

\[in\] 次の値の組み合わせになります。

| 定数 | 説明 |
| --- | --- |
| FLAG\_FIND\_AROUND | 文末(文頭)まで検索したら、文頭(文末)に移動する。 |
| FLAG\_FIND\_BOL | 正規表現「^」が選択の最初に一致することができます。 |
| FLAG\_FIND\_BOOKMARK | 見つかった行にブックマークを設定します。 |
| FLAG\_FIND\_COUNT | 文字列の一致する数を数えます。 |
| FLAG\_FIND\_COUNT\_FREQUENCY | 抽出の結果より頻出文字列の表を作成します。FLAG\_FIND\_EXTRACT と FLAG\_FIND\_OUTPUT\_DISPLAY と組み合わせて使用します。ウィンドウのタブが有効である必要があります。 |
| FLAG\_FIND\_EMBEDDED\_NL | CSV文書に埋め込まれた改行コードを検索し、その他の改行コードは検索しません。 |
| FLAG\_FIND\_EOL | 正規表現「$」が選択の最後に一致することができます。 |
| FLAG\_FIND\_EXTRACT | 見つかった行を抽出して新規文書を作成します。 |
| FLAG\_FIND\_LOOKAROUND | 選択範囲のみの正規表現を使用する検索で周辺を見ます。 |
| FLAG\_FIND\_MULTI | 一括検索/すべて一括置換を実行します。これが指定されていないと、連続検索/すべて連続置換を実行します。 |
| FLAG\_FIND\_NEXT | カーソル位置より下方向に検索します。これが指定されていない場合、上方向に検索します。 |
| FLAG\_FIND\_NO\_PROMPT | 検索する文字列が見つからなくてもプロンプト ダイアログ ボックスを表示しません。 |
| FLAG\_FIND\_OPEN\_DOC | 同じフレーム ウィンドウ内に開いているすべての文書から検索します。 |
| FLAG\_FIND\_OUTPUT | 抽出結果をアウトプット バーに表示します。FLAG\_FIND\_EXTRACT と組み合わせて使用します。 |
| FLAG\_FIND\_REGEX\_BOOST | 正規表現エンジンとして Regex.Boost を使用します。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 正規表現エンジンとして Onigmo を使用します。 |
| FLAG\_FIND\_SAVE\_HISTORY | 次の検索用に、検索文字列を保存します。 |
| FLAG\_FIND\_SEPARATE\_CRLF | CR と LF を区別します。 |
| FLAG\_FIND\_SEL\_ONLY | 選択範囲のみ検索します。 |
| FLAG\_REPLACE\_ALL | すべて置換します。 |
| FLAG\_REPLACE\_SEL\_ONLY | すべて置換の場合に選択範囲のテキストのみを対象とします。FLAG\_REPLACE\_ALL とともに指定する必要があります。 |

_nCount_

\[out\] nBatchFlags が FLAG\_FIND\_COUNT、FLAG\_FIND\_BOOKMARK、FLAG\_FIND\_SELECT\_ALL、FLAG\_FIND\_EXTRACT、FLAG\_FIND\_FILTER、または FLAG\_REPLACE\_ALL を含んでいる場合、一致する数を受け取る変数へのポインタを指定します。

## バージョン

Version 19.9 以上で利用できます。

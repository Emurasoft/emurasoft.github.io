# EXTRACT\_FREQUENT\_INFO

[EE\_EXTRACT\_FREQUENT メッセージ](../message/ee_extract_frequent) で使用します。

typedef struct \_EXTRACT\_FREQUENT\_INFO {

UINT cbSize;

UINT nType;

UINT nNumOfLines;

UINT iCsvFormat;

UINT64 nFlags;

LPCWSTR pszIgnore;

} EXTRACT\_FREQUENT\_INFO;

## フィールド

_cbSize_

sizeof( EXTRACT\_FREQUENT\_INFO ) を指定します。

_nType_

次のいずれかの値を指定します。

| 値 | 意味 |
| --- | --- |
| FREQ\_TYPE\_LINES | 頻出する行の一覧を作成します。 |
| FREQ\_TYPE\_WORDS | 頻出する単語の一覧を作成します。単語は英数字でない文字に囲まれた文字列であり、\[カスタマイズ\] ダイアログ ボックスの [\[編集\] ページ](../../dlg/customize/edit/index) の \[次の文字を英数字として扱う\] テキスト ボックスでカスタマイズできます。 |
| FREQ\_TYPE\_CELLS | 頻出するセルの一覧を作成します。このオプションは CSV 文書がアクティブの時のみ利用可能です。 |
| FREQ\_TYPE\_IPV4 | 頻出するIPv4アドレスの一覧を作成します。 |
| FREQ\_TYPE\_IPV6 | 頻出するIPv6アドレスの一覧を作成します。 |

_nNumOfLines_

抽出する文字列の最大数を指定します。実際の出力は、同じ頻度だけ検出された複数の文字列をすべて含めるため、この数を超える場合があります。

_iCsvFormat_

表示に使用する CSV フォーマットを指定します。

_nFlags_

次の値を組み合わせて指定します。

| 値 | 意味 |
| --- | --- |
| FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
| FLAG\_FIND\_OPEN\_DOC | 同じフレーム ウィンドウ内に開いているすべての文書から検索します。 |
| FLAG\_FIND\_SEL\_ONLY | 選択範囲のみ検索します。 |

_pszIgnore_

頻出文字列を数える間、無視する文字列の一覧を指定します。複数の文字列は、LF (\\n) で区切る必要があります。

## バージョン

Version 21.9 以上で利用できます。

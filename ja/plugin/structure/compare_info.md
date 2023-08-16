# COMPARE\_INFO

[EE\_COMPARE](../message/ee_compare) メッセージで使用します。

typedef struct \_COMPARE\_INFO {

UINT cbSize;

UINT flags;

LPCWSTR pszDocument1;

LPCWSTR pszDocument2;

LPCWSTR pszResultFileName;

} COMPARE\_INFO;

## フィールド

_cbSize_

この構造体のサイズ、sizeof( COMPARE\_INFO ) を指定します。

_flags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| COMPARE\_GENERATE\_REPORT | レポート ファイルを作成します。ファイルのパスは strResultFileName パラメータに指定する必要があります。 |
| COMPARE\_IGNORE\_CASE | 大文字小文字の区別を無視します。 |
| COMPARE\_IGNORE\_COMMENT | コメントを無視します。 |
| COMPARE\_IGNORE\_CRLF | 改行コードの違いを無視します。 |
| COMPARE\_IGNORE\_EMBEDDED\_SPACE | 行の中間に埋め込まれた空白を無視します。 |
| COMPARE\_IGNORE\_ENCODING | エンコードの違いを無視します。 |
| COMPARE\_IGNORE\_LEAD\_SPACE | 行頭の空白を無視します。 |
| COMPARE\_IGNORE\_TRAIL\_SPACE | 行末の空白を無視します。 |
| COMPARE\_OPEN\_REPORT | レポート ファイルを開きます。COMPARE\_GENERATE\_REPORT も指定する必要があります。 |
| COMPARE\_REPORT\_3\_COL | 3列のフォーマットでレポートを出力します。 |
| COMPARE\_REPORT\_DIFF\_ONLY | 異なる行のみをレポートします。 |
| COMPARE\_QUALITY\_1 | 近くの行のみを検索する最も速い方法。 |
| COMPARE\_QUALITY\_2 | より速い方法。 |
| COMPARE\_QUALITY\_3 | 中間の速度。 |
| COMPARE\_QUALITY\_4 | より正確な方法。 |
| COMPARE\_QUALITY\_5 | 最も正確な方法で最も多くの行を検索します。 |
| COMPARE\_QUICK | 高速に比較し、相違点を強調表示しません。このフラグは COMPARE\_QUIET 以外のオプションと組み合わせて使用できません。 |
| COMPARE\_QUIET | メッセージを表示しません。 |
| COMPARE\_RESET | 比較や同期スクロールをリセットして比較結果をクリアします。 |
| COMPARE\_RESET\_AFTER | 比較とレポート作成の後、比較や同期スクロールをリセットして比較結果をクリアします。COMPARE\_GENERATE\_REPORT も指定する必要があります。 |
| COMPARE\_RESTORE\_POS | 終了時、ウィンドウ位置を復元します。 |
| COMPARE\_SPLIT\_VERT | ウィンドウを左右に分割して文書を表示します。 |
| COMPARE\_SWITCH\_NO\_WRAP | 折り返さないに切り替えます。 |
| COMPARE\_SYNC\_CARET | カーソル位置を同期します。 |
| COMPARE\_SYNC\_SCROLL\_HORZ | 水平スクロールを同期します。 |
| COMPARE\_SYNC\_SCROLL\_ONLY | 比較は行わず、同期スクロールのみを行います。 |
| COMPARE\_SYNC\_SCROLL\_VERT | 垂直スクロールを同期します。 |
| COMPARE\_TILE\_HORZ | 文書を上下に並べます。 |
| COMPARE\_TILE\_VERT | 文書を左右に並べます。 |

_pszDocument1_

第1文書を特定する文字列を指定します。この値は、ファイル名、完全パスの付いたファイル名、またはコロン (:) で始まる現在のグループ内の文書のインデックスになります。例えば、"filename.csv"、"C:\\data\\filename.csv"、または ":2" と指定することができます。

_pszDocument2_

第2文書を特定する文字列を指定します。この値のフォーマットは strDocument1 と同じです。

_pszResultFileName_

flags フィールドに COMPARE\_GENERATE\_REPORT が指定されていると、EmEditor は比較のレポートを指定するファイル名で保存します。

## バージョン

Version 17.7 以上で利用できます。

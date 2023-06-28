# Compare メソッド

2個の文書を比較します。

#### \[JavaScript\]

_n_ = editor. **Compare**( _nFlags_, _strDocument1_, _strDocument2_, _strResultFileName_ );

#### \[VBScript\]

_n_ = editor. **Compare**( _nFlags_, _strDocument1_, _strDocument2_, _strResultFileName_ )

## パラメータ

_nFlags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| eeCompareGenerateReport | レポート ファイルを作成します。ファイルのパスは strResultFileName パラメータに指定する必要があります。 |
| eeCompareOpenReport | レポート ファイルを開きます。eeCompareGenerateReport も指定する必要があります。 |
| eeCompareQuality1 | 近くの行のみを検索する最も速い方法。 |
| eeCompareQuality2 | より速い方法。 |
| eeCompareQuality3 | 中間の速度。 |
| eeCompareQuality4 | より正確な方法。 |
| eeCompareQuality5 | 最も正確な方法で最も多くの行を検索します。 |
| eeCompareQuick | 高速に比較し、相違点を強調表示しません。このフラグは eeCompareQuiet 以外のオプションと組み合わせて使用できません。 |
| eeCompareQuiet | メッセージを表示しません。 |
| eeCompareReport3Col | 3列のフォーマットでレポートを出力します。 |
| eeCompareReportDiffOnly | 異なる行のみをレポートします。 |
| eeCompareReset | 比較や同期スクロールをリセットして比較結果をクリアします。 |
| eeCompareResetAfter | 比較とレポート作成の後、比較や同期スクロールをリセットして比較結果をクリアします。eeCompareGenerateReport も指定する必要があります。 |
| eeCompareRestorePos | 終了時、ウィンドウ位置を復元します。 |
| eeCompareSplitVert | ウィンドウを左右に分割して文書を表示します。 |
| eeCompareSwitchNoWrap | 折り返さないに切り替えます。 |
| eeCompareSyncCaret | カーソル位置を同期します。 |
| eeCompareSyncScrollHorz | 水平スクロールを同期します。 |
| eeCompareSyncScrollOnly | 比較は行わず、同期スクロールのみを行います。 |
| eeCompareSyncScrollVert | 垂直スクロールを同期します。 |
| eeCompareTileHorz | 文書を上下に並べます。 |
| eeCompareTileVert | 文書を左右に並べます。 |
| eeIgnoreCases | 大文字小文字の区別を無視します。 |
| eeIgnoreComments | コメントを無視します。 |
| eeIgnoreEmbeddedSpaces | 行の中間に埋め込まれた空白を無視します。 |
| eeIgnoreEncodings | エンコードの違いを無視します。 |
| eeIgnoreLeadSpaces | 行頭の空白を無視します。 |
| eeIgnoreNewlines | 改行コードの違いを無視します。 |
| eeIgnoreTrailingSpaces | 行末の空白を無視します。 |

_strDocument1_

第1文書を特定する文字列を指定します。この値は、ファイル名、完全パスの付いたファイル名、またはコロン (:) で始まる現在のグループ内の文書のインデックスになります。例えば、"filename.csv"、"C:\\data\\filename.csv" (JavaScript の場合は、"C:\\\data\\\filename.csv") 、または ":2" と指定することができます。strDocument1 と strDocument2 の両方が空の文字列の場合、EmEditor は最近使用された 2 個のファイルを選択します。

_strDocument2_

第2文書を特定する文字列を指定します。この値のフォーマットは strDocument1 と同じです。

_strResultFileName_

nFlags パラメータに COMPARE\_GENERATE\_REPORT が指定されていると、EmEditor は比較のレポートを指定するファイル名で保存します。

## 戻り値

戻り値は次のいずれかの値になります。

|     |     |
| --- | --- |
| eeDiff | 2個の文書は同じではありません。 |
| eeMatched | 2個の文書は同じです。 |
| eeMatchedIgnored | 2個の文書は無視した場所を除き同じです。 |

## バージョン

EmEditor Professional Version 17.7 以上で利用できます。
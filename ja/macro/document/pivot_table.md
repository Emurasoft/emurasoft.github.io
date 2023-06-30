# PivotTable メソッド ()

CSV文書でピボット テーブルを作成します。

#### \[JavaScript\]

document. **PivotTable**( iRow, iColumn, iValue, nFlags, strSortRow, nSortRowFlags, strSortColumn, nSortColumnFlags, strLocale, strTotalRowLabel, strTotalColLabel, nDecimalPlaces );

#### \[VBScript\]

document. **PivotTable** iRow, iColumn, iValue, nFlags, strSortRow, nSortRowFlags, strSortColumn, nSortColumnFlags, strLocale, strTotalRowLabel, strTotalColLabel, nDecimalPlaces

## パラメータ

_iRow_

> 新規ピボット テーブルで行に展開する CSV 文書の列のインデックスを指定します。

_iColumn_

> 新規ピボット テーブルで列に展開する CSV 文書の列のインデックスを指定します。

_iValue_

> 新規ピボット テーブルで値に展開する CSV 文書の列のインデックスを指定します。

_nFlags_

> 次の値の組み合わせを指定します。
>
> |     |     |
> | --- | --- |
> | eePivotTypeCount | 値の数。 |
> | eePivotTypeSum | 値の合計。 |
> | eePivotTypeAverage | 値の平均値。 |
> | eePivotTypeMax | 最大値。 |
> | eePivotTypeMin | 最小値。 |
> | eePivotTotalRows | 行の合計を表示します。 |
> | eePivotTotalColumns | 列の合計を表示します。 |

_strSortRow_

> 行に適用するフラグを指定する文字列を指定します。省略すると、並べ替えは行われません。フォーマットは以下の通りです。
>
> 構文:
>
> option (+/-)
>
> option: 以下のテーブルから並べ替えオプションを選択します。
>
> |     |     |
> | --- | --- |
> | A | テキストを並べ替えます。 |
> | D | 日付と時刻で並べ替えます。 |
> | I | IPv4 アドレスを並べ替えます。 |
> | P | IPv6 アドレスを並べ替えます。 |
> | L | 文字数で並べ替えます。 |
> | N | 数字を並べ替えます。 |
> | O | 出現頻度で並べ替えます。 |
> | W | 単語数で並べ替えます。 |
>
> (+/-): 以下のテーブルから並べ替えオプションを選択します。
>
> |     |     |
> | --- | --- |
> | + | 昇順。 |
> | - | 降順。 |
>
> 例:
>
> |     |     |
> | --- | --- |
> | A+ | テキストを昇順で並べ替えます。 |
> | N- | 数字を降順で並べ替えます。 |

_nSortRowFlags_

> 行に適用する並べ替えのためのフラグの組み合わせを指定します。これらのフラグは _strSortRow_ が空でない場合のみ指定できます。このパラメータは省略できます。
>
> |     |     |
> | --- | --- |
> | eeSortBinaryComparison | ロケールを無視して、高速にバイナリ比較を行います。 |
> | eeSortDigitsAsNumbers | \[AからZへ並べ替え\] コマンドまたは \[ZからAへ並べ替え\] コマンドを使用時でも、数字が数として扱われます。例えば、「2」は「10」の前に並べ替えられます。 |
> | eeSortGroupIdentical | 出現頻度で並べ替える時、同じ文字列をグループ化します。 |
> | eeSortIgnoreCase | 大文字と小文字を区別しないで並べ替えます。 |
> | eeSortIgnoreKanaType | ひらがなとカタカナを区別しないで並べ替えます。 |
> | eeSortIgnoreNonSpace | 場所を取らない文字を区別しないで並べ替えます。 |
> | eeSortIgnoreSymbols | 記号を無視して並べ替えます。 |
> | eeSortIgnoreWidth | 半角文字と全角文字の違いは無視されます。例えば、「Ｃａｔ」と「cat」は同一とみなされます。全角文字は中国語と日本語の文章で使用されているフォーマットです。 |
> | eeSortIgnorePrefix | 数字を並べ替える際、先頭の数字以外の文字は無視されます。 |
> | eeSortLengthView | \[短い文字列から長い文字列へ並べ替え\] コマンドまたは \[長い文字列から短い文字列へ並べ替え\] コマンドを使用時、全角文字が2文字として扱われます。 |
> | eeSortStable | 常に順位の位置関係を保ったままソートを行います。このフラグが指定されていると、指定されていない場合に比べて、通常、遅くなります。 |
> | eeSortStringSort | 句読点が記号と同様に扱われます。 |

_strSortColumn_

> 列に適用するフラグを指定する文字列を指定します。省略すると、並べ替えは行われません。フォーマットは _strSortRow_ パラメータと同じです。

_nSortColumnFlags_

> 列に適用する並べ替えのためのフラグの組み合わせを指定します。これらのフラグは _strSortColulmn_ が空でない場合のみ指定できます。このパラメータは省略できます。

_strLocale_

> 並べ替えで使用するロケールを指定します。これが空の場合、\[カスタマイズ\] ダイアログ ボックスで \[並べ替え\] ページで指定されているロケールを使用します。

_strTotalRowLabel_

> 行の合計値に使用するヘディングのラベルを指定します。このパラメータは、 _nFlags_ パラメータに eePivotTotalRows が指定されている場合のみ使用されます。

_strTotalColLabel_

> 列の合計値に使用するヘディングのラベルを指定します。このパラメータは、 _nFlags_ パラメータに eePivotTotalColumns が指定されている場合のみ使用されます。

_nDecimalPlaces_

> 値の小数点以下の桁数を指定します。

## 例

CSV 文書の 1 列目をピボット テーブルの行に、2 列目をピボット テーブルの列に、3 列目をピボット テーブルの値にしてピボット テーブルを作成します。行と列をロケールを無視して高速にバイナリ比較を行って並べ替えします。合計を表示します。

#### \[JavaScript\]

document.PivotTable( 1, 2, 3, eePivotTypeSumInt \| eePivotTotalRows \| eePivotTotalColumns, "A+", eeSortBinaryComparison, "A+", eeSortBinaryComparison, "", "Grand Total", "Grand Total" );

#### \[VBScript\]

document.PivotTable 1, 2, 3, eePivotTypeSumInt Or eePivotTotalRows Or eePivotTotalColumns, "A+", eeSortBinaryComparison, "A+", eeSortBinaryComparison, "", "Grand Total", "Grand Total"

## バージョン

EmEditor Professional Version 21.4 以上で利用できます。
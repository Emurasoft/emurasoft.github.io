# SplitColumn メソッド ()

CSV モードで指定された列を区切り文字で分割して右の列または下の行に置きます。

#### \[JavaScript\]

document. **SplitColumn**( _strColumns_, _strSeparator_, _strSeparator_, _nType_, _strSortType_, _nFlags_, _nLimit_, BSTR _strLocale_ );

#### \[VBScript\]

document. **SplitColumn** _strColumns_, _strSeparator_, _strSeparator_, _nType_, _strSortType_, _nFlags_, _nLimit_, BSTR _strLocale_

## パラメータ

_strColumns_

> 分割する列の 1 を基底とするインデックスの配列を文字列で指定します。例えば、"1,3,5" は、1列目、3列目、および 5列目を意味します。

_strSeparator_

> 列を分割する際に使用する区切り文字列を指定します。このパラメータは空にすることができません。

_nType_

> 次の値のいずれかを指定することができます。省略すると、eeSplitIntoColumns を指定することになります。
>
> | 値 | 意味 |
> | --- | --- |
> | eeSplitIntoColumns | _iColumn1_ から _iColumn2_ までの列を、区切り文字で分割して右の列に置きます。 |
> | eeSplitIntoLines | _iColumn1_ から _iColumn2_ までの列を、区切り文字で分割して下の行に置きます。 |
> | eeSplitIntoNone | _iColumn1_ から _iColumn2_ までの列を、区切り文字で分割しませんが、並べ替えまたは分割後の重複文字列を削除します。 |

_strSortType_

> フラグを指定する文字列を指定します。省略すると、分割の後、並べ替えは行われません。フォーマットは以下の通りです。
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
> | V | 逆順に並べ替えます。 |
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

_nFlags_

> 次の値の組み合わせを指定します。分割後に重複文字列を削除するには、eeRemoveDuplicates を指定する必要があります。その他のフラグは、 _strSortType_ に空でない文字列を指定した場合だけ、指定できます。このパラメータは省略できます。
>
> |     |     |
> | --- | --- |
> | eeDontDiscardExtra | nLimit が 0 でない時、余分な文字列を破棄しません。 |
> | eeRemoveDuplicates | 重複文字列を削除します。 |
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

_nLimit_

> セル毎の分割の最大数を指定します。0 を指定するか省略すると、分割数を制限しません。

_strLocale_

> 並べ替えで使用するロケールを指定します。これが空の場合、カスタマイズ ダイアログ ボックスで指定されているロケールを使用します。

## 例

次の例は、1列目をセミコロンで分割して、下の行に置きます。

#### \[JavaScript\]

document.SplitColumn( "1", ";", eeSplitIntoLines );

#### \[VBScript\]

document.SplitColumn "1", ";", eeSplitIntoLines

## バージョン

EmEditor Professional Version 19.9 以上で利用できます。
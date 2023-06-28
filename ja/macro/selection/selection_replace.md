# Replace メソッド

指定した文字列を指定した文字列に置き換えます。

#### \[JavaScript\]

nFound = document.selection. **Replace**( _strFind_, _strReplace_, _nFlags_\[, _nExFlags_\] );

#### \[VBScript\]

nFound = document.selection. **Replace**( _strFind_, _strReplace_, _nFlags_\[, _nExFlags_\] )

## 引数

_strFind_

検索する文字列を指定します。

_strReplace_

置き換える文字列を指定します。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eeFindAround | 文末まで検索したら文頭に移動し、文頭まで検索したら文末に移動します。 |
| eeFindExtract | nExFlags に eeExFindInsertColumn が指定されていない場合、正規表現を使用して一致するすべての文字列を検索して抽出し、置換表現で置換します。nFlags に eeFindReplaceRegExp を指定する必要があり、置換表現は空にすることができません。eeFindOutput と組み合わせて指定することができます。<br>nExFlags に eeExFindInsertColumn を指定する場合は、CSV 文書がアクティブで、1列以上の列が選択されている必要があります。さらに、nFlags に eeFindReplaceRegExp が指定されていない場合、一致した文字列によって新しい CSV 列を作成し、元の列は変更されません。nFlags に eeFindReplaceRegExp が指定されている場合、置換表現によって新しい CSV 列を作成し、元の列は変更されません。 |
| eeFindMatchDotNL | 正規表現「.」が改行コードに一致することができます。 |
| eeFindOutput | 抽出結果の一覧をアウトプット バーに表示します。eeFindExtract と一緒に指定する必要があります。 |
| eeFindReplaceCase | 大文字と小文字を区別して検索します。 |
| eeFindReplaceEmbeddedNL | CSV文書に埋め込まれた改行コードを検索し、その他の改行コードは検索しません。 |
| eeFindReplaceEscSeq | 文字列をエスケープ シーケンスで指定します。eeFindReplaceRegExp または eeExFindNumberRange と組み合わせて指定できません。 |
| eeFindReplaceOnlyWord | 単語のみを検索します。 |
| eeFindReplaceOpenDoc | 同じフレーム ウィンドウ内に開いているすべての文書から検索します。 |
| eeFindReplaceQuiet | 指定した文字列が見つからなかった場合、ステータス バーにメッセージを表示しません。 |
| eeFindReplaceRegExp | 文字列を正規表現で指定します。eeFindReplaceEscSeq または eeExFindNumberRange と組み合わせて指定できません。 |
| eeFindReplaceSelOnly | 選択範囲のみ置換します。 |
| eeFindSaveHistory | 次の検索用に、検索文字列を保存します。 |
| eeReplaceAll | すべて一度に置換します。 |
| eeReplaceSelOnly | 選択範囲のみ置換します。(eeFindReplaceSelOnly と同じ) |

_nExFlags_

次の値の組み合わせを指定します。ただし、eeExFindRegexBoost と eeExFindRegexOnigmo は、どちらか一方のみ指定できます。どちらも指定されない場合には、既定の正規表現エンジンを使用します。

|     |     |
| --- | --- |
| eeExFindBOL | 正規表現「^」が選択の最初に一致することができます。 |
| eeExFindEOL | 正規表現「$」が選択の最後に一致することができます。 |
| eeExFindFuzzy | あいまい一致を使用します。 |
| eeExFindInsertColumn | 置換表現によって新しい CSV 列を作成し、元の列は変更されません。nFlags パラメータに eeFindReplaceRegExp が指定されていない場合、置換表現は空である必要があり、新しい列は一致した文字列を変更なしに埋められます。新しい列は元の列の右側に挿入されます。eeFindExtract と共に指定する必要があります。 |
| eeExFindLookaround | 選択範囲のみの正規表現を使用する検索で周辺を見ます。 |
| eeExFindNumberRange | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、eeFindReplaceEscSeq または eeFindReplaceRegExp と一緒に指定することはできません。 |
| eeExFindRegexBoost | 正規表現エンジンとして Boost.Regex を使用します。 |
| eeExFindRegexOnigmo | 正規表現エンジンとして Onigmo を使用します。 |
| eeExFindSeparateCRLF | CR と LF を区別します。 |

## 戻り値

eeReplaceAll を指定すると、置換した文字列の数を返します。eeReplaceAll を指定しない場合、文字列が見つかった場合は 1
を返し、見つからない場合は 0 を返します。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
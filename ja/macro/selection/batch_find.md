# BatchFind メソッド ()

複数の文字列を検索します。

## 

### \[JavaScript\]

```
nFound = document.selection.BatchFind( filters, nFlags, nExFlags );
```

### \[VBScript\]

```
nFound = document.selection.BatchFind( filters, nFlags, nExFlags )
```

## 引数

_filters_

検索文字列やフラグを含む [Filters コレクション](../filters/index) を指定します。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eeFindAround | 文末まで検索したら文頭に移動し、文頭まで検索したら文末に移動します。 |
| eeFindBookmark | 見つかった行にブックマークを設定します。 |
| eeFindCount | 文字列の一致する数を数えます。 |
| eeFindExtract | 見つかった行を抽出して新規文書を作成します。eeFindFileAndLine、eeFindFileNamesOnly、eeFindLineOnly、または eeFindMatchedOnly と組み合わせて指定します。これらのフラグが指定されない場合には、eeFindLineOnly が指定されたとみなされます。 |
| eeFindFileAndLine | ファイル名、行番号、および検索した文字列を含む行の内容が結果として表示されます。eeFindExtract と組み合わせて使用します。eeFindFileNamesOnly、eeFindLineOnly または eeFindMatchedOnly と組み合わせて指定できません。 |
| eeFindFileNamesOnly | ファイル名のみ表示します。eeFindExtract と組み合わせて使用します。eeFindFileAndLine、eeFindLineOnly または eeFindMatchedOnly と組み合わせて指定できません。 |
| eeFindLineOnly | 検索した文字列を含む行の内容だけが結果として表示されます。eeFindExtract と組み合わせて使用します。eeFindFileAndLine、eeFindMatchedOnly または eeFindFileNamesOnly と組み合わせて指定できません。 |
| eeFindMatchedOnly | 一致した文字列のみが結果として表示されます。eeFindExtract と組み合わせて使用します。eeFindFileAndLine、eeFindFileNamesOnly または eeFindLineOnly と組み合わせて指定できません。 |
| eeFindNext | カーソル位置から下方向に検索します。 |
| eeFindMatchDotNL | 正規表現「.」が改行コードに一致することができます。 |
| eeFindOutput | 抽出結果をアウトプット バーに表示します。eeFindExtract と組み合わせて使用します。 |
| eeFindPrevious | カーソル位置から上方向に検索します。 |
| eeFindReplaceEmbeddedNL | CSV文書に埋め込まれた改行コードを検索し、その他の改行コードは検索しません。 |
| eeFindReplaceOpenDoc | 同じフレーム ウィンドウ内に開いているすべての文書から検索します。 |
| eeFindReplaceQuiet | 指定した文字列が見つからなかった場合、ステータス バーにメッセージを表示しません。 |
| eeFindReplaceSelOnly | 選択範囲のみ検索します。 |
| eeFindSaveHistory | 次の検索用に、検索文字列を保存します。 |

_nExFlags_

次の値の組み合わせを指定します。ただし、eeExFindRegexBoost と eeExFindRegexOnigmo は、どちらか一方のみ指定できます。どちらも指定されない場合には、既定の正規表現エンジンを使用します。

|     |     |
| --- | --- |
| eeExFindBOL | 正規表現「^」が選択の最初に一致することができます。 |
| eeExFindCountFrequency | 抽出の結果より頻出文字列の表を作成します。eeFindExtract と、eeFindLineOnly または eeFindMatchedOnly と組み合わせて使用します。ウィンドウのタブが有効である必要があります。 |
| eeExFindEOL | 正規表現「$」が選択の最後に一致することができます。 |
| eeExFindLookaround | 選択範囲のみの正規表現を使用する検索で周辺を見ます。 |
| eeExFindRegexBoost | 正規表現エンジンとして Boost.Regex を使用します。 |
| eeExFindRegexOnigmo | 正規表現エンジンとして Onigmo を使用します。 |
| eeExFindSeparateCRLF | CR と LF を区別します。 |

## 戻り値

文字列が見つかった場合は 1 を返します。見つからない場合は 0 を返します。ただし、eeFindCount、eeFindBookmark、eeFindSelectAll、eeFindExtract フラグが指定されている場合、戻り値は文書内で一致した文字列の数になります。

## バージョン

EmEditor Professional Version 19.9 以上で利用できます。

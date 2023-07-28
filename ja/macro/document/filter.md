# Filter メソッド (Document オブジェクト)

指定する文字列と設定で文書にフィルターをかけます。

## 

### \[JavaScript\]

```
nCount = document.Filter( strFilter, iColumn, flags[, xBegin[, xEnd[, ExFlags[ , nVisibleLinesAbove[ , nVisibleLinesBelow]]]]] );
```

### \[VBScript\]

```
nCount = document.Filter( strFilter, iColumn, flags[, xBegin[, xEnd[, ExFlags[ , nVisibleLinesAbove[ , nVisibleLinesBelow]]]]] )
```

## パラメータ

_strFilter_

検索する文字列を指定します。指定文字列が空で、ExFlags に 0 を指定すると、現在のフィルターを中止します。

_iCollumn_

取得するテキストの列の 1 から始まるインデックスを指定します。0 を指定すると行全体から検索します。-1 を指定すると xBegin と xEnd パラメータによってテキストの開始位置と終了位置を指定します。

_flags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| eeFindContinue | 次に Filter メソッドを呼ぶ際にフィルターをクリアしないことを示します。この Filter メソッドの直後には、フィルターが適用されず、次の Filter メソッドまでフィルターの適用を待ちます。このフラグは複数レベルのフィルタを作成する時に使用します。eeFindKeepPrevious フラグと似ていますが、Filter <br> メソッドを呼び出す毎にフィルターが適用されないため、複数のレベルが存在する場合には、eeFindKeepPrevious より高速に動作します。 |
| eeFindKeepPrevious | この Filter メソッドによって既存のフィルターをクリアしないことを示します。このフラグは複数レベルのフィルタを作成する時に使用します。 |
| eeFindLogicalOr | 複数レベルのフィルターの場合、以前のレベルに論理和 (論理 OR) でフィルターを実行します。 |
| eeFindNegative | フィルター ツール バーを表示して指定する文字列に一致する行を除外します。 |
| eeFindRemoveLast | 最後に追加されたフィルターのレベルを削除します。 |
| eeFindReplaceCase | 大文字と小文字を区別して検索します。 |
| eeFindReplaceEscSeq | 文字列をエスケープ シーケンスで指定します。eeFindReplaceRegExp と組み合わせて指定できません。 |
| eeFindReplaceOnlyWord | 単語のみを検索します。 |
| eeFindReplaceRegExp | 文字列を正規表現で指定します。eeFindReplaceEscSeq と組み合わせて指定できません。 |
| eeFindWholeString | 文字列全体に一致します。 |

_xBegin_

検索したいテキストの開始位置のインデックスを論理文字単位で指定します。テキストの最後から数えて xEnd で指定する場合には 0
を指定します。このフィールドを有効にするには iColumn パラメータに -1 を指定する必要があります。

_xEnd_

検索したいテキストの終了位置のインデックスを論理文字単位で指定します。最後まで全部を検索する場合には 0
を指定します。このフィールドを有効にするには iColumn パラメータに -1 を指定する必要があります。

_ExFlags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| eeExFindBookmarkedOnly | ブックマークが設定された行のみ一致します。このフラグは eeExFindUnbookmarkedOnly と一緒に指定することはできません。 |
| eeExFindCrLf | 改行コードが CR+LF の行に一致します。このフラグは、eeExFindMatchNL と一緒に指定する必要があります。 |
| eeExFindCrOnly | 改行コードが CR のみの行に一致します。このフラグは、eeExFindMatchNL と一緒に指定する必要があります。 |
| eeExFindFuzzy | あいまい一致を使用します。 |
| eeExFindLfOnly | 改行コードが LF のみの行に一致します。このフラグは、eeExFindMatchNL と一緒に指定する必要があります。 |
| eeExFindLinkFile | _strFilter_ が改行で分割された複数の検索文字列を含むリンク ファイルへのファイルのパスであることを指定します。行にタブ文字が含まれている場合、検索文字列はタブを含まない最初の文字列になります。 _strFilter_ は EmEditor インストール パスからの相対パスにすることができます。%USERPROFILE% などの環境変数を含むこともできます。 |
| eeExFindMatchNL | 指定する改行コードに一致します。このフラグは、eeExFindCrLf、eeExFindCrOnly、eeExFindLfOnly、または eeExFindNLOthers と一緒に指定します。 |
| eeExFindNLOthers | 改行コードが存在しない行に一致します。これらの行には、ファイルの最終行、および改行コード無しで次の行に続く非常に長い行が含まれます。このフラグは、eeExFindMatchNL と一緒に指定する必要があります。 |
| eeExFindNumberRange | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、eeFindReplaceEscSeq または eeFindReplaceRegExp と一緒に指定することはできません。 |
| eeExFindUnbookmarkedOnly | ブックマークが設定されていない行のみ一致します。このフラグは eeExFindBookmarkedOnly と一緒に指定することはできません。 |
| eeExFilterBegin | 開始フィルターを指定します。このフラグは eeExFilterEnd と一緒に指定することはできません。 |
| eeExFilterEnd | 終了フィルターを指定します。このフラグは eeExFilterBegin と一緒に指定することはできません。 |

_nVisibleLinesAbove_

一致した行の上に表示する追加の行数を指定します。-1 を指定すると以前に使用されていた値を使用します。

_nVisibleLinesBelow_

一致した行の下に表示する追加の行数を指定します。-1 を指定すると以前に使用されていた値を使用します。

## 戻り値

戻り値は、指定する文字列に一致する行数になります。指定文字列が空で、かつ FLAG\_FIND\_BOOKMARKED\_ONLY、FLAG\_FIND\_UNBOOKMARKED\_ONLY、FLAG\_FIND\_MATCH\_NL のいずれも指定されていない場合、戻り値は -1 になります。eeFindContinue が指定されている場合、戻り値は 0 になります。

## バージョン

EmEditor Professional Version 14.7 以上で利用できます。

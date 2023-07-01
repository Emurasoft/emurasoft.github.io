# AddFind メソッド ()

検索するアイテムを追加します。

#### \[JavaScript\]

list. **AddFind**( _strFind_, _nFlags_, _nExFlags_ );

#### \[VBScript\]

list. **AddFind**( _strFind_, _nFlags_, _nExFlags_ )

## パラメータ

_strFind_

検索する文字列を指定します。

_nFlags_

> 次の値を組み合わせて指定します。
>
> |     |     |
> | --- | --- |
> | eeFindLogicalOr | 複数レベルのフィルターの場合、以前のレベルに論理和 (論理 OR) でフィルターを実行します。 |
> | eeFindNegative | フィルター ツール バーを表示して指定する文字列に一致する行を除外します。 |
> | eeFindReplaceCase | 大文字と小文字を区別して検索します。 |
> | eeFindReplaceEscSeq | 文字列をエスケープ シーケンスで指定します。eeFindReplaceRegExp と組み合わせて指定できません。 |
> | eeFindReplaceOnlyWord | 単語のみを検索します。 |
> | eeFindReplaceRegExp | 文字列を正規表現で指定します。eeFindReplaceEscSeq と組み合わせて指定できません。 |
> | eeFindWholeString | 文字列全体に一致します。 |

_nExFlags_

> 次の値を組み合わせて指定します。
>
> |     |     |
> | --- | --- |
> | eeExFindBookmarkedOnly | ブックマークが設定された行のみ一致します。このフラグは eeExFindUnbookmarkedOnly と一緒に指定することはできません。 |
> | eeExFindCrLf | 改行コードが CR+LF の行に一致します。このフラグは、eeExFindMatchNL と一緒に指定する必要があります。 |
> | eeExFindCrOnly | 改行コードが CR のみの行に一致します。このフラグは、eeExFindMatchNL と一緒に指定する必要があります。 |
> | eeExFindFuzzy | あいまい一致を使用します。 |
> | eeExFindLinkFile | _strFind_ が改行で分割された複数の検索文字列を含むリンク ファイルへのファイルのパスであることを指定します。行にタブ文字が含まれている場合、検索文字列はタブを含まない最初の文字列になります。 _strFind_ は EmEditor インストール パスからの相対パスにすることができます。%USERPROFILE% などの環境変数を含むこともできます。実行中のマクロ フォルダ内のファイルを指定するには、次のようにしてください。<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
> | eeExFindLfOnly | 改行コードが LF のみの行に一致します。このフラグは、eeExFindMatchNL と一緒に指定する必要があります。 |
> | eeExFindMatchNL | 指定する改行コードに一致します。このフラグは、eeExFindCrLf、eeExFindCrOnly、eeExFindLfOnly、または eeExFindNLOthers と一緒に指定します。 |
> | eeExFindNLOthers | 改行コードが存在しない行に一致します。これらの行には、ファイルの最終行、および改行コード無しで次の行に続く非常に長い行が含まれます。このフラグは、eeExFindMatchNL と一緒に指定する必要があります。 |
> | eeExFindNumberRange | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、eeFindReplaceEscSeq または eeFindReplaceRegExp と一緒に指定することはできません。 |
> | eeExFindUnbookmarkedOnly | ブックマークが設定されていない行のみ一致します。このフラグは eeExFindBookmarkedOnly と一緒に指定することはできません。 |
> | eeExFilterBegin | 開始フィルターを指定します。このフラグは eeExFilterEnd と一緒に指定することはできません。 |
> | eeExFilterEnd | 終了フィルターを指定します。このフラグは eeExFilterBegin と一緒に指定することはできません。 |

## バージョン

EmEditor Professional Version 19.9 以上で利用できます。

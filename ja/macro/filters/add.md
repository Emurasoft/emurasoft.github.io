# Add メソッド ()

アイテムを追加します。

#### \[JavaScript\]

list. **Add**( _strFilter_, _bEnabled_, _iColumn_, _nFlags_, _xBegin_, _xEnd_, _strReplace_, _nExFlags_ );

#### \[VBScript\]

list. **Add** _strFilter_, _bEnabled_, _iColumn_, _nFlags_, _xBegin_, _xEnd, strReplace, nExFlags_

## パラメータ

_strFilter_

検索する文字列を指定します。

_bEnabled_

フィルターが有効かどうかを指定します。

_iColumn_

取得するテキストの列の 1 から始まるインデックスを指定します。0 を指定すると行全体から検索します。-1 を指定すると xBegin と xEnd パラメータによってテキストの開始位置と終了位置を指定します。

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

_xBegin_

> 検索したいテキストの開始位置のインデックスを論理文字単位で指定します。テキストの最後から数えて xEnd で指定する場合には 0
> を指定します。このフィールドを有効にするには iColumn パラメータに -1 を指定する必要があります。

_xEnd_

> 検索したいテキストの終了位置のインデックスを論理文字単位で指定します。最後まで全部を検索する場合には 0
> を指定します。このフィールドを有効にするには iColumn パラメータに -1 を指定する必要があります。

_strFilter_

置き換える文字列を指定します。

_nExFlags_

> 次の値を組み合わせて指定します。
>
> |     |     |
> | --- | --- |
> | eeExFindLinkFile | _strFilter_ が改行で分割された複数の検索文字列を含むリンク ファイルへのファイルのパスであることを指定します。行にタブ文字が含まれている場合、検索文字列はタブを含まない最初の文字列になります。 _strFilter_ は EmEditor インストール パスからの相対パスにすることができます。%USERPROFILE% などの環境変数を含むこともできます。実行中のマクロ フォルダ内のファイルを指定するには、次のようにしてください。<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
> | eeExFindFuzzy | あいまい一致を使用します。 |
> | eeExFindNumberRange | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、eeFindReplaceEscSeq または eeFindReplaceRegExp と一緒に指定することはできません。 |

## バージョン

EmEditor Professional Version 16.0 以上で利用できます。

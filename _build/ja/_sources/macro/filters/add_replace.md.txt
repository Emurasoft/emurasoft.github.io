# AddReplace メソッド

置換するアイテムを追加します。

#### \[JavaScript\]

list. **AddReplace**( _strFind_, _strReplace_, _nFlags_, _nExFlags_ );

#### \[VBScript\]

list. **AddReplace**( _strFind_, _strReplace_, _nFlags_, _nExFlags_ )

## パラメータ

_strFind_

検索する文字列を指定します。

_strReplace_

置換後の文字列を指定します。

_nFlags_

> 次の値を組み合わせて指定します。
>
> |     |     |
> | --- | --- |
> | eeFindReplaceCase | 大文字と小文字を区別して検索します。 |
> | eeFindReplaceEscSeq | 文字列をエスケープ シーケンスで指定します。eeFindReplaceRegExp と組み合わせて指定できません。 |
> | eeFindReplaceOnlyWord | 単語のみを検索します。 |
> | eeFindReplaceRegExp | 文字列を正規表現で指定します。eeFindReplaceEscSeq と組み合わせて指定できません。 |

_nExFlags_

> 次の値を組み合わせて指定します。
>
> |     |     |
> | --- | --- |
> | eeExFindLinkFile | _strFind_ が改行で分割された複数の検索文字列を含むリンク ファイルへのファイルのパスであることを指定します。行にタブ文字が含まれている場合、検索文字列はタブを含まない最初の文字列になり、置換文字列は2番目の文字列になります。 _strFind_ は EmEditor インストール パスからの相対パスにすることができます。%USERPROFILE% などの環境変数を含むこともできます。実行中のマクロ フォルダ内のファイルを指定するには、次のようにしてください。<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
> | eeExFindFuzzy | あいまい一致を使用します。 |
> | eeExFindNumberRange | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、eeFindReplaceEscSeq または eeFindReplaceRegExp と一緒に指定することはできません。 |

## バージョン

EmEditor Professional Version 19.9 以上で利用できます。
# FindInFiles メソッド

指定するパスの複数のファイルから文字列を検索します。検索したファイルの一覧は現在のウィンドウに表示されます。ファイルを保存していない場合は、ファイルを保存するかどうかを選択するメッセージ ボックスが表示されます。ユーザーが途中で処理を中止した場合、エラーを発生します。

#### \[JavaScript\]

nFound = editor. **FindInFiles**( _strFind_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] );

#### \[VBScript\]

nFound = editor. **FindInFiles** _strFind_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \]

## パラメータ

_strFind_

検索する文字列を指定します。

_strPath_

検索するパスを指定します。ここには、\\* または ? のワイルド カードを含めて指定することができます。複数のファイルを指定する場合は、; で区切ります。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eeFindOpenDirect | ファイルから検索の結果を一覧としては表示せずに、検索文字列を含むファイルを直接開きます。eeFindOpenFilter または eeFindOutput と組み合わせて指定できません。 |
| eeFindOpenFilter | ファイルから検索の結果を一覧としては表示せずに、検索文字列を含むファイルを直接開き、さらにフィルターに検索文字列を設定します。eeFindOpenDirect または eeFindOutput と組み合わせて指定できません。 |
| eeFindOutput | ファイルから検索の場合、検索結果をアウトプット バーに表示します。eeFindOpenDirect または eeFindOpenFilter と組み合わせて指定できません。 |
| eeFindRecursive | サブフォルダも検索します。 |
| eeFindReplaceCase | 大文字と小文字を区別して検索します。 |
| eeFindReplaceEscSeq | 文字列をエスケープ シーケンスで指定します。eeFindReplaceRegExp と組み合わせて指定できません。 |
| eeFindReplaceIgnoreFiles | _strFilesToIgnore_ で指定する名前のファイルまたはフォルダを無視します。 |
| eeFindReplaceOnlyWord | 単語のみを検索します。 |
| eeFindReplaceRegExp | 文字列を正規表現で指定します。eeFindReplaceEscSeq と組み合わせて指定できません。 |
| eeFindSaveHistory | 検索した文字列を履歴に保存します。 |
| eeOpenDetectAll | すべて自動検出します。 |
| eeOpenDetectCharset | HTML/XML の Charset を検出します。 |
| eeOpenDetectUnicode | Unicode サイン (BOM) を検出します。 |
| eeOpenDetectUTF8 | UTF-8 を自動検出します。 |

さらに、次の値のどれか1つを指定することができます。

|     |     |
| --- | --- |
| eeFindFileAndMatched | ファイル名と一致した文字列が結果として表示されます。 |
| eeFindFileLineAndMatched | ファイル名、行番号、一致した文字列が結果として表示されます。 |
| eeFindFileNamesOnly | 見つかったファイルのファイル名だけを結果として表示し、検索した文字列を含む行の内容は表示しません。 |
| eeFindLineOnly | 検索した文字列を含む行の内容だけが結果として表示されます。 |
| eeFindMatchedOnly | 一致した文字列のみが結果として表示されます。 |

_nEncoding_

開くファイルのエンコードを指定します。 [エンコード定数](../const/const_encoding) から選択するか、または
Windows で使用されるエンコードを指定します。0 を指定するか省略すると、検索されたファイル名に関連付けられている設定のプロパティに指定されているエンコードが使用されます。

_strFilesToIgnore_

_nFlags_ に eeFindReplaceIgnoreFiles
を指定した場合、無視するファイルまたはフォルダの名前を指定します。ここには、\\* または ? のワイルド
カードを含めて指定することができます。複数のファイルを指定する場合は、; で区切ります。

_nExFlags_

次の値の組み合わせを指定します。ただし、eeExFindRegexBoost と eeExFindRegexOnigmo は、どちらか一方のみ指定できます。どちらも指定されない場合には、既定の正規表現エンジンを使用します。

|     |     |
| --- | --- |
| eeExFindCountFrequency | 結果より頻出文字列の表を作成します。eeFindLineOnly または eeFindMatchedOnly と組み合わせて使用します。 |
| eeExFindFuzzy | あいまい一致を使用します。 |
| eeExFindNumberRange | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、eeFindReplaceEscSeq または eeFindReplaceRegExp と一緒に指定することはできません。 |
| eeExFindOutputEncoding | ファイル名にエンコード名を追加します。 |
| eeExFindRegexBoost | 正規表現エンジンとして Boost.Regex を使用します。 |
| eeExFindRegexOnigmo | 正規表現エンジンとして Onigmo を使用します。 |

_nLimit_

一致の数がこの数字に到達すると、EmEditor はファイルの検索を終了します。0 を指定するか省略すると、EmEditor はファイルの検索を終了しません。

## 戻り値

戻り値は検索したすべてのファイル内で一致した文字列を含む行数になります。

## バージョン

EmEditor Professional Version 4.02 以上で利用できます。
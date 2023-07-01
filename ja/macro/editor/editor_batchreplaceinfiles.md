# BatchReplaceInFiles メソッド ()

指定するパスの複数のファイルから複数の文字列を置換します。ユーザーが途中で処理を中止した場合、エラーを発生します。

#### \[JavaScript\]

nFound = editor. **ReplaceInFiles**( _filters_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _strBackupPath_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] \] );

#### \[VBScript\]

nFound = editor. **ReplaceInFiles**( _filters_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _strBackupPath_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] \] )

## パラメータ

_filters_

検索文字列やフラグを含む [Filters コレクション](../filters/index) を指定します。

_strPath_

検索するパスを指定します。ここには、\\* または ? のワイルド カードを含めて指定することができます。複数のファイルを指定する場合は、; で区切ります。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eeFindRecursive | サブフォルダも検索します。 |
| eeFindReplaceIgnoreFiles | _strFilesToIgnore_ で指定する名前のファイルまたはフォルダを無視します。 |
| eeReplaceKeepOpen | 変更したファイルを開いたままにします。eeReplaceBackup と組み合わせて指定できません。 |
| eeReplaceBackup | バックアップを保存します。eeReplaceKeepOpen と組み合わせて指定できません。 |
| eeOpenDetectUnicode | Unicode サイン (BOM) を検出します。 |
| eeOpenDetectUTF8 | UTF-8 を自動検出します。 |
| eeOpenDetectCharset | HTML/XML の Charset を検出します。 |
| eeOpenDetectAll | すべて自動検出します。 |

_nEncoding_

開くファイルのエンコードを指定します。 [エンコード定数](../const/const_encoding) から選択するか、または
Windows で使用されるエンコードを指定します。0 を指定するか省略すると、検索されたファイル名に関連付けられている設定のプロパティに指定されているエンコードが使用されます。

_strFilesToIgnore_

_nFlags_ に eeFindReplaceIgnoreFiles
を指定した場合、無視するファイルまたはフォルダの名前を指定します。ここには、\\* または ? のワイルド
カードを含めて指定することができます。複数のファイルを指定する場合は、; で区切ります。

_strBackupPath_

_nFlags_ に eeReplaceBackup を指定した場合、バックアップ先フォルダを指定します。

_nExFlags_

次の値の組み合わせを指定します。ただし、eeExFindRegexBoost と eeExFindRegexOnigmo は、どちらか一方のみ指定できます。どちらも指定されない場合には、既定の正規表現エンジンを使用します。

|     |     |
| --- | --- |
| eeExFindMulti | すべて一括置換を実行します。これが指定されていないと、すべて連続置換を実行します。 [\[すべて連続置換\] と \[すべて一括置換\] の違い](../../howto/search/batch_vs_bulk) をお読みください。 |
| eeExFindRegexBoost | 正規表現エンジンとして Boost.Regex を使用します。 |
| eeExFindRegexOnigmo | 正規表現エンジンとして Onigmo を使用します。 |

_nLimit_

一致の数がこの数字に到達すると、EmEditor はファイルの検索を終了します。0 を指定するか省略すると、EmEditor はファイルの検索を終了しません。

## 戻り値

戻り値は検索したすべてのファイル内で置換された文字列の合計数になります。

## 注意

_nFlags_ に eeReplaceKeepOpen を指定しない場合、この操作は元に戻すことはできません。その場合、 _nFlags_
に eeReplaceBackup
を指定して、バックアップを保存することをおすすめします。バックアップ先フォルダに同じファイル名が存在する場合、以前のファイル上に上書き保存されます。

## バージョン

EmEditor Professional Version 20.0 以上で利用できます。

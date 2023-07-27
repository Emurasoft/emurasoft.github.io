# ReplaceInFiles メソッド ()

指定するパスの複数のファイルから文字列を置換します。ユーザーが途中で処理を中止した場合、エラーを発生します。

## 

### \[JavaScript\]

```
nFound = editor.ReplaceInFiles( strFind, strReplace, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ strBackupPath, [ nExFlags, [ nLimit ] ] ] ] ] );
```

### \[VBScript\]

```
nFound = editor.ReplaceInFiles strFind, strReplace, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ strBackupPath, [ nExFlags, [ nLimit ] ] ] ] ]
```

## パラメータ

_strFind_

検索する文字列を指定します。

_strReplace_

置換後の文字列を指定します。

_strPath_

検索するパスを指定します。ここには、\\* または ? のワイルド カードを含めて指定することができます。複数のファイルを指定する場合は、; で区切ります。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| eeFindReplaceCase | 大文字と小文字を区別して検索します。 |
| eeFindReplaceEscSeq | 文字列をエスケープ シーケンスで指定します。eeFindReplaceRegExp と組み合わせて指定できません。 |
| eeFindReplaceOnlyWord | 単語のみを検索します。 |
| eeFindReplaceRegExp | 文字列を正規表現で指定します。eeFindReplaceEscSeq と組み合わせて指定できません。 |
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
| eeExFindFuzzy | あいまい一致を使用します。 |
| eeExFindNumberRange | [数値範囲表現](../../howto/search/number_range_syntax) に一致します。このフラグは、eeFindReplaceEscSeq または eeFindReplaceRegExp と一緒に指定することはできません。 |
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

EmEditor Professional Version 4.02 以上で利用できます。

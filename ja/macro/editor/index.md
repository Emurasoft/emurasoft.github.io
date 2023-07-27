# Editor オブジェクト

## プロパティ

|     |     |
| --- | --- |
| [ActiveDocument](editor_activedocument) | 現在開いている Document オブジェクトを返します。 |
| [Configs](configs) | Configs コレクションを返します。 |
| [CsvList](csv_list) | [CsvList コレクション](../csv_list/index) を取得、または設定します。 |
| [Documents](editor_documents) | 現在開いている文書のコレクションを示す Documents コレクションを返します。 |
| [EnableTab](editor_enabletab) | タブが有効かどうかを取得、または設定します。 |
| [filters](filters) | Filters コレクションを返します。 |
| [FullName](editor_fullname) | EmEditor の実行ファイル emeditor.exe の完全パスとファイル名を取得します。 |
| [FuzzyOptions](fuzzy_options) | FuzzyOptions オブジェクトを返します。 |
| [LangID](langid) | 現在選択されている言語 ID を取得します。 |
| [regex](regex) | Regex オブジェクトを取得します。 |
| [RegisteredName](registeredname) | EmEditor がユーザー登録されている名前を取得します。 |
| [Version](editor_version) | 現在実行している EmEditor のバージョンを表す文字列を取得します。 |

## メソッド

|     |     |
| --- | --- |
| [BatchFindInFiles](editor_batchfindinfiles) | 指定したパスの複数のファイルから文字列を検索します。 |
| [BatchReplaceInFiles](editor_batchreplaceinfiles) | 指定するパスの複数のファイルから複数の文字列を置換します。 |
| [Compare](compare) | 2個の文書を比較します。 |
| [GetUnicodeName](getunicodename) | 指定された文字または文字列のUnicode名を取得します。 |
| [ExecuteCommandByID](editor_executecommandbyid) | EmEditor のコマンドを整数の ID で指定して実行します。 |
| [ExecuteMacro](editor_executemacro) | 指定するマクロを実行します。 |
| [ExecutePlugin](editor_executeplugin) | 指定するプラグインを実行します。 |
| [FileDialog](filedialog) | ファイルを開く、または名前を付けて保存ダイアログ ボックスを表示して、開くファイルのドライブ、ディレクトリ、名前を指定します。 |
| [FindInFiles](editor_findinfiles) | 指定したパスの複数のファイルから文字列を検索します。 |
| [GetProfileInt](getprofileint) | EmEditor の設定に応じて、レジストリまたは INI ファイルから、指定する整数値を取得します。 |
| [GetProfileString](getprofilestring) | EmEditor の設定に応じて、レジストリまたは INI ファイルから、指定する文字列値を取得します。 |
| [Join](join) | SQL においての JOIN 操作と同様な方法を使って、2個の CSV 文書を結合して新規文書を作成します。 |
| [NewFile](editor_newfile) | 新規にファイルを作成します。 |
| [OpenFile](editor_openfile) | 既存のファイルを開きます。 |
| [QueryStatusByID](editor_querystatusbyid) | EmEditor のコマンドが実行できるかどうか、またチェックされているかどうかを取得します。 |
| [QueryStringByID](editor_querystringbyid) | 指定するコマンドに関連する文字列を取得します。 |
| [RefreshCommonSettings](refresh_common_settings) | 共通の設定をロードし EmEditor ウィンドウを最新の情報に更新します。 |
| [ReplaceInFiles](editor_replaceinfiles) | 指定したパスの複数のファイルから文字列を置換します。 |
| [SaveAll](editor_saveall) | すべての EmEditor で開かれているファイルを保存します。 |
| [SaveCloseAll](editor_savecloseall) | すべての EmEditor で開かれているファイルを保存して閉じます。 |
| [Stderr](stderr) | 文字列を標準エラー出力に出力します。 |
| [WriteProfileInt](writeprofileint) | EmEditor の設定に応じて、レジストリまたは INI ファイルに、整数値を設定します。 |
| [WriteProfileString](writeprofilestring) | EmEditor の設定に応じて、レジストリまたは INI ファイルに、文字列値を設定します。 |

## バージョン

EmEditor Professional Version 8.00 以上で利用できます。


```{toctree}
:maxdepth: 1
compare
configs
csv_list
editor_activedocument
editor_batchfindinfiles
editor_batchreplaceinfiles
editor_documents
editor_enabletab
editor_executecommandbyid
editor_executemacro
editor_executeplugin
editor_findinfiles
editor_fullname
editor_newfile
editor_openfile
editor_querystatusbyid
editor_querystringbyid
editor_replaceinfiles
editor_saveall
editor_savecloseall
editor_version
filedialog
filters
fuzzy_options
getprofileint
getprofilestring
getunicodename
join
langid
refresh_common_settings
regex
registeredname
stderr
writeprofileint
writeprofilestring
```

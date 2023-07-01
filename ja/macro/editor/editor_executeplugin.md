# ExecutePlugin メソッド ()

指定するプラグインを実行します。

#### \[JavaScript\]

_nResult_ = editor. **ExecutePlugin**( _strPluginFileName_, _nFlags_, _nParam_, _strParam_ );

#### \[VBScript\]

_nResult_ = editor. **ExecutePlugin**( _strPluginFileName_, _nFlags_, _nParam_, _strParam_ )

## パラメータ

_strPluginFileName_

プラグインのファイル名を指定します。

_nFlags_

次の値の組み合わせを指定します。eePluginExecuteCommand、eePluginUserMessage、および eePluginQueryStatus は、どれか 1 つだけ指定する必要があります。

|     |     |
| --- | --- |
| eePluginExecuteCommand | ユーザーがプラグイン コマンドを選択したかのようにプラグインを実行します。これが指定されていると、nParam と strParam パラメータは無視されます。 |
| eePluginUserMessage | nParam と strParam パラメータを使用して、プラグインにメッセージを送ります 。 |
| eePluginQueryStatus | プラグインの状態を取得します。これが指定されていると、nParam と strParam パラメータは無視されます。 |
| eePluginAbsolutePath | strPluginFileName にはファイルへの完全パスが含まれます。このフラグが指定されていない場合は、プラグインは既定のプラグインフォルダ (EmEditor インストール フォルダの中の PlugIns サブ フォルダ) に存在する必要があります。 |

_nParam_

プラグインに送る整数パラメータを指定します。このパラメータの意味は各プラグインに依存します。これが省略されると、0 を指定することになります。

_strParam_

プラグインに送る文字列パラメータを指定します。このパラメータの意味は各プラグインに依存します。これが省略されると、空の文字列を指定することになります。

## 戻り値

エラーが発生すると戻り値は負の数になります。そうでなければ、eePluginExecuteCommand が指定されると、戻り値は 0 になります。eePluginUserMessage が指定されると、戻り値の意味は各プラグインに依存します。eePluginQueryStatus が指定されると、戻り値は次の値の組み合わせになります。

|     |     |
| --- | --- |
| eeStatusEnabled | プラグインは有効です。 |
| eeStatusLatched | プラグインはチェックされています。 |

## 例

#### \[JavaScript\]

editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 0, "<${1:p}>${2:${SelText}}</$1>$0" );

editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 1, "General\\\Date");

editor.ExecutePlugin( "Snippets.dll", eePluginUserMessage, 2, "/General/Date" );

#### \[VBScript\]

editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 0, "<${1:p}>${2:${SelText}}</$1>$0"

editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 1, "General" & Chr(92) & "Date"

editor.ExecutePlugin "Snippets.dll", eePluginUserMessage, 2, "/General/Date"

## バージョン

EmEditor Professional Version 15.5 以上で利用できます。

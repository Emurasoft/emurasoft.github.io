# Editor\_ExecPlugin

指定するプラグインを実行します。このインライン関数を使うか、または [EE\_EXEC\_PLUGIN](../message/ee_exec_plugin) メッセージを直接送ることができます。

HRESULT Editor\_ExecPlugin( HWND hwnd, LPCWSTR pszName, LONG nFlags, WPARAM wParam, LPARAM lParam, LONG\_PTR\* pnResult );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pszName_

> プラグインのファイル名を指定します。

_nFlags_

> 次の値の組み合わせを指定します。PLUGIN\_FLAG\_EXEC\_COMMAND、PLUGIN\_FLAG\_USER\_MSG、および PLUGIN\_FLAG\_QUERY\_STATUSは、どれか 1 つだけ指定する必要があります。
>
> |     |     |
> | --- | --- |
> | PLUGIN\_FLAG\_EXEC\_COMMAND | ユーザーがプラグイン コマンドを選択したかのようにプラグインを実行します。これが指定されていると、wParam と lParam パラメータは無視されます。 |
> | PLUGIN\_FLAG\_USER\_MSG | wParam と lParam パラメータを使用して、プラグインにメッセージを送ります 。 |
> | PLUGIN\_FLAG\_QUERY\_STATUS | プラグインの状態を取得します。これが指定されていると、wParam と lParam パラメータは無視されます。 |
> | PLUGIN\_FLAG\_ABSOLUTE\_PATH | pszName にはファイルへの完全パスが含まれます。このフラグが指定されていない場合は、プラグインは既定のプラグインフォルダ (EmEditor インストール フォルダの中の PlugIns サブ フォルダ) に存在する必要があります。 |

_wParam_

> プラグインに送る第1パラメータを指定します。このパラメータの意味は各プラグインに依存します。

_lParam_

> プラグインに送る第2パラメータを指定します。このパラメータの意味は各プラグインに依存します。

## 戻り値

> エラーが発生すると戻り値は負の数になります。そうでなければ、PLUGIN\_FLAG\_EXEC\_COMMAND が指定されると、戻り値は 0 になります。PLUGIN\_FLAG\_USER\_MSG が指定されると、戻り値の意味は各プラグインに依存します。PLUGIN\_FLAG\_QUERY\_STATUS が指定されると、戻り値は次の値の組み合わせになります。
>
> |     |     |
> | --- | --- |
> | STATUS\_ENABLED | プラグインは有効です。 |
> | STATUS\_LATCHED | プラグインはチェックされています。 |

## バージョン

> EmEditor Professional Version 15.5 以上で利用できます。

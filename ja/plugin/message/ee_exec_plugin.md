# EE\_EXEC\_PLUGIN

指定するプラグインを実行します。このメッセージを直接送るか、または
[Editor\_ExecPlugin インライン関数](../macro/editor_execplugin) を使うことができます。

EE\_EXEC\_PLUGIN

wParam = (WPARAM) (EXEC\_PLUGIN\_INFO\*) pPluginInfo;

lParam = 0;

## パラメータ

_pFilterInfo_

> [EXEC\_PLUGIN\_INFO 構造体](../structure/exec_plugin_info) へのポインタを指定します。

## 戻り値

> エラーが発生すると戻り値は負の数になります。そうでなければ、PLUGIN\_FLAG\_EXEC\_COMMAND が指定されると、戻り値は 0 になります。PLUGIN\_FLAG\_USER\_MSG が指定されると、戻り値の意味は各プラグインに依存します。PLUGIN\_FLAG\_QUERY\_STATUS が指定されると、戻り値は次の値の組み合わせになります。
>
> |     |     |
> | --- | --- |
> | STATUS\_ENABLED | プラグインは有効です。 |
> | STATUS\_LATCHED | プラグインはチェックされています。 |

## バージョン

> EmEditor Professional Version 15.5 以上で利用できます。

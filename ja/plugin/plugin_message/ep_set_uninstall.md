# EP\_SET\_UNINSTALL

アンインストールを実行します。

EP\_SET\_UNINSTALL

hwnd = hwndParent;

wParam = (WPARAM) (LPTSTR) pszUninstallCommand;

lParam = (LPARAM) (LPTSTR) pszUninstallParam;

## パラメータ

_hwndParent_

> プラグインの設定ダイアログのウィンドウ ハンドルが格納されています。

_pszUninstallCommand_

> 戻り値に UNINSTALL\_RUN\_COMMAND を指定する場合、実行するファイルの完全パスを指定します。

_pszUninstallParam_

> 戻り値に UNINSTALL\_RUN\_COMMAND を指定する場合、実行するファイルのパラメータを指定します。

## 戻り値

> 次のうちのいずれかの値を返します。
>
> |     |     |
> | --- | --- |
> | UNINSTALL\_FALSE | アンインストールを実行しません。 |
> | UNINSTALL\_SIMPLE\_DELETE | 単純に実行中のプラグインの DLL ファイルを削除します。 |
> | UNINSTALL\_RUN\_COMMAND | 指定するコマンドを実行します。 |
>
> TRUE を返すとアンインストールを実行します、FALSE を返すとアンインストールは実行されません。

## バージョン

> Version 3.00 以上で利用できます。ただし、戻り値の UNINSTALL\_RUN\_COMMAND と、pszUninstallCommand パラメータと pszUninstallParam パラメータは、Version 6.00 以上で利用できます。

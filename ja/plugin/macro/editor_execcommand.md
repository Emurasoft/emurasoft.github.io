# Editor\_ExecCommand

指定するコマンドIDを実行します。このインライン関数を使うか、または [EE\_EXEC\_COMMAND](../message/ee_exec_command) メッセージを直接送ることができます。

Editor\_ExecCommand( HWND hwnd, UINT nCmdID );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nCmdID_

> 実行するIDの [コマンドID](../cmdid/index) を指定します。

## 戻り値

> 戻り値は利用されません。
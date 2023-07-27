# EE\_EXEC\_COMMAND

指定するコマンドIDを実行します。このメッセージを直接送るか、または [Editor\_ExecCommand インライン関数](../macro/editor_execcommand) を使うことができます。

EE\_EXEC\_COMMAND

wParam = (WPARAM) (UINT) nCmdID;

lParam = 0;

## パラメータ

_nCmdID_

実行するIDの [コマンドID](../cmdid/index) を指定します。

## 戻り値

戻り値は利用されません。

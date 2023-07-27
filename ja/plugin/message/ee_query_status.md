# EE\_QUERY\_STATUS

指定するコマンドIDが実行可能か、またはチェックされた状態かを調べます。このメッセージを直接送るか、または
[Editor\_QueryStatus インライン関数](../macro/editor_querystatus) を使うことができます。

EE\_QUERY\_STATUS

wParam = (WPARAM) (UINT) nCmdID;

lParam = (LPARAM) (BOOL\*) pbChecked;

## パラメータ

_nCmdID_

実行するIDの [コマンドID](../cmdid/index) を指定します。

_pbChecked_

チェックされた状態を示すBOOL値へのポインタを示します。

## 戻り値

実行可能な状態なら 0 以外を返します。実行可能でなければ 0 を返します。

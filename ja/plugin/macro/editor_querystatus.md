# Editor\_QueryStatus

指定するコマンドIDが実行可能か、またはチェックされた状態かを調べます。このインライン関数を使うか、または
[EE\_QUERY\_STATUS メッセージ](../message/ee_query_status) を直接送ることができます。

Editor\_QueryStatus( HWND hwnd, UINT nCmdID, BOOL\* pbChecked );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nCmdID_

実行するIDの [コマンドID](../cmdid/index) を指定します。

_pbChecked_

チェックされた状態かを示します。

## 戻り値

実行可能な状態なら 0 以外を返します。実行可能でなければ 0 を返します。

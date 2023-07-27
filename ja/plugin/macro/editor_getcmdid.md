# Editor\_GetCmdID

プラグインのコマンドIDを取得します。このインライン関数を使うか、または [EE\_GET\_CMD\_ID](../message/ee_get_cmd_id) メッセージを直接送ることができます。

Editor\_GetCmdID( HWND hwnd, HINSTANCE hInstance );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_hInstance_

プラグインのインスタンス　ハンドルを指定します。

## 戻り値

このプラグインを実行するためのコマンドIDを返します。

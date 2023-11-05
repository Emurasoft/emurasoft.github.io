# EE\_GET\_CMD\_ID

プラグインのコマンドIDを取得します。このメッセージを直接送るか、または [Editor\_GetCmdID インライン関数](../macro/editor_getcmdid) を使うことができます。

```
EE_GET_CMD_ID
wParam = 0;
lParam = (LPARAM) (HINSTANCE) hInstance
```

## パラメータ

_hInstance_

プラグインのインスタンス　ハンドルを指定します。

## 戻り値

このプラグインを実行するためのコマンドIDを返します。

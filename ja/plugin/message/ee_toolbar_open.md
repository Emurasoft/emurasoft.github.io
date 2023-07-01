# EE\_TOOLBAR\_OPEN

カスタム ツール バーを開きます。このメッセージを直接送るか、または [Editor\_ToolbarOpen インライン関数](../macro/editor_toolbaropen) を使うことができます。

EE\_TOOLBAR\_OPEN

wParam = 0;

lParam = (LPARAM) (TOOLBAR\_INFO\*) pToolbarInfo;

## パラメータ

_pToolbarInfo_

> [TOOLBAR\_INFO構造体](../structure/toolbar_info) に指示します。

## 戻り値

> 成功すると、カスタム ツール バー ID を返します。失敗すると 0 を返します。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。

# EE\_LOAD\_CONFIGA

ANSI文字列で指定する設定を読み直します。このメッセージを直接送るか、または [Editor\_LoadConfigA \
インライン関数](../macro/editor_loadconfiga) を使うことができます。

EE\_LOAD\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szConfigName;

## パラメータ

_szConfigName_

設定の名前を指定します。

## 戻り値

戻り値は利用されません。

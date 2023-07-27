# EE\_CUSTOM\_BAR\_OPEN

カスタム バーを開きます。このメッセージを送る前に、既に、別のカスタム バーが開いている場合は、そのカスタム バーを閉じて、新しいカスタム バーを開きます。このメッセージを直接送るか、または [Editor\_CustomBarOpen インライン関数](../macro/editor_custombaropen) を使うことができます。

EE\_CUSTOM\_BAR\_OPEN

wParam = 0;

lParam = (LPCTSTR) (LPCTSTR) pCustomBarInfo;

## パラメータ

_pCustomBarInfo_

[CUSTOM\_BAR\_INFO 構造体](../structure/custom_bar_info) へのポインタを指定します。

## 戻り値

成功すると、カスタム バー ID を返します。この ID は、EE\_CUSTOM\_BAR\_CLOSE メッセージで閉じるときに必要です。失敗すると 0 を返します。

## バージョン

Version 6.00 以上で利用できます。

# EE\_CUSTOM\_BAR\_CLOSE

カスタム バーを閉じます。このメッセージを直接送るか、または [Editor\_CustomBar\_Close インライン関数](../macro/editor_custombarclose) を使うことができます。

EE\_CUSTOM\_BAR\_CLOSE

wParam = nCustomBarID;

lParam = 0;

## パラメータ

_nCustomBarID_

> カスタム バー ID を指定します。この値は、EE\_CUSTOM\_BAR\_OPEN メッセージを送ったときの戻り値です。

## 戻り値

> 成功すると TRUE を返します。失敗すると FALSE を返します。

## バージョン

> Version 6.00 以上で利用できます。
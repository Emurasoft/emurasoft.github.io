# EE\_TOOLBAR\_CLOSE

カスタム ツール バーを閉じます。このメッセージを直接送るか、または
[Editor\_ToolbarClose インライン関数](../macro/editor_toolbarclose) を使うことができます。

EE\_TOOLBAR\_CLOSE

(UINT)wParam = nToolbarID

## パラメータ

_nToolbarID_

> 閉じるツール バーを指定します。これは EE\_TOOLBAR\_OPEN メッセージからの戻り値です。

## 戻り値

> 関数が成功し、かつツール バーの状態が変更されたら TRUE を返します。失敗するかツール バーの状態に変更がなければ FALSE を返します。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。

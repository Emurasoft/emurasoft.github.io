# EE\_TOOLBAR\_SHOW

カスタム ツール バーの表示/非表示を切り替えます。このメッセージを直接送るか、または [Editor\_ToolbarShow インライン関数](../macro/editor_toolbarshow) を使うことができます。

```
EE_TOOLBAR_SHOW
(UINT)wParam = nToolbarID
(BOOL)lParam = bVisible
```

## パラメータ

_nToolbarID_

閉じるツール バーを指定します。EE\_TOOLBAR\_OPEN メッセージからの戻り値になります。

_bVisible_

TRUE を指定するとツール バーが表示され、FALSE を指定するとツール バーが非表示になります。

## 戻り値

メッセージが成功し、かつツール バーの状態が変更されたら TRUE を返します。失敗するか変更がなければ FALSE を返します。

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。

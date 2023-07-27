# EP\_GET\_NAME

プラグインの名前を取得します。

EP\_GET\_NAME

hwnd = hwndParent;

wParam = cb;

lParam = szName;

## パラメータ

_hwndParent_

プラグインの設定ダイアログのウィンドウ ハンドルが格納されています。

_cb_

文字列のバッファのサイズが格納されています。

_szName_

文字列のバッファへのポインタが格納されています。

## 戻り値

文字列を格納するのに必要なバッファのサイズを返します。

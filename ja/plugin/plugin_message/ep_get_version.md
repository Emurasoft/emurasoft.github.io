# EP\_GET\_VERSION

プラグインのバージョンを取得します。

EP\_GET\_NAME

hwnd = hwndParent;

wParam = cch;

lParam = szVersion;

## パラメータ

_hwndParent_

プラグインの設定ダイアログのウィンドウ ハンドルが格納されています。

_cch_

文字列の終端ヌル文字を含むバッファのサイズが文字数で格納されています。

_szVersion_

文字列のバッファへのポインタが格納されています。

## 戻り値

文字列を格納するのに必要な終端ヌル文字を含むバッファのサイズを文字数で返します。

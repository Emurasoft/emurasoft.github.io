# EE\_FREE

指定するプラグインを開放します。このメッセージを直接送るか、または [Editor\_Free インライン関数](../macro/editor_free) を使うことができます。通常、EmEditorのプラグイン設定ダイアログで使用されます。

EE\_FREE

wParam = 0;

lParam = (LPARAM)(ATOM)atom;

## パラメータ

_atom_

プラグインのファイル名のアトムを指定します。

## 戻り値

プラグインの開放に成功したら TRUE を返します。失敗すると FALSE を返します。

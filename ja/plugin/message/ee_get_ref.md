# EE\_GET\_REF

指定するプラグインの参照数を返します。このメッセージを直接送るか、または [Editor\_GetRef インライン関数](../macro/editor_getref) を使うことができます。通常、EmEditorのプラグイン設定ダイアログで使用されます。

EE\_GET\_REF

wParam = 0;

lParam = (LPARAM)(ATOM)atom;

## パラメータ

_atom_

> プラグインのファイル名のアトムを指定します。

## 戻り値

> 指定するプラグインの参照数を返します。戻り値が 0 以下の場合は、安全に、指定するプラグインを EmEditor からアンロードできることを示します。

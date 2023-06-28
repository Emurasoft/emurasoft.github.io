# EE\_ADD\_REF

プラグインの参照数1つ増加させます。このメッセージを直接送るか、または [Editor\_AddRef インライン関数](../macro/editor_addref) を使うことができます。

EE\_ADD\_REF

wParam = 0;

lParam = (LPARAM)(HINSTANCE)hInstance;

## パラメータ

_hInstance_

> プラグインのインスタンス ハンドルを指定します。

## 戻り値

> プラグインの参照数を1つ増加させた後の参照数を返します。戻り値が 0 以下の場合は、安全に、指定するプラグインを EmEditor
> からアンロードできることを示します。
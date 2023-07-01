# EE\_RELEASE

プラグインの参照数1つ減少させます。このメッセージを直接送るか、または [Editor\_Release インライン関数](../macro/editor_release) を使うことができます。

EE\_RELEASE

wParam = 0;

lParam = (LPARAM)(HINSTANCE)hInstance;

## パラメータ

_hInstance_

> プラグインのインスタンス　ハンドルを指定します。

## 戻り値

> プラグインの参照数を1つ減少させた後の参照数を返します。戻り値が 0 以下の場合は、安全に、指定するプラグインを EmEditor
> からアンロードできることを示します。

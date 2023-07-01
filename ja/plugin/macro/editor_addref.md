# Editor\_AddRef

プラグインの参照数を1つ増加させます。このインライン関数を使うか、または [EE\_ADD\_REF メッセージ](../message/ee_add_ref) を直接送ることができます。

Editor\_AddRef( HWND hwnd, HINSTANCE hInstance );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_hInstance_

> プラグインのインスタンス ハンドルを指定します。

## 戻り値

> プラグインの参照数を1つ増加させた後の参照数を返します。戻り値が 0 以下の場合は、安全に、指定するプラグインを EmEditor
> からアンロードできることを示します。

# Editor\_GetConfigA

現在アクティブな文書に選択されている設定の名前をANSI文字列で取得します。このインライン関数を使うか、または
[EE\_GET\_CONFIGA](../message/ee_get_configa) メッセージを直接送ることができます。

Editor\_GetConfigA( HWND hwnd, LPSTR szConfigName );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szConfigName_

> 設定の名前を取得するバッファを指定します。バッファは、ヌル文字 ('\\0') を含めて MAX\_CONFIG\_NAME の長さを確保します。

## 戻り値

> 戻り値は利用されません。
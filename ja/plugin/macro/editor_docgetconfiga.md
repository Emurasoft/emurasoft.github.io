# Editor\_DocGetConfigA

指定する文書に選択されている設定の名前をANSI文字列で取得します。このインライン関数を使うか、または
[EE\_GET\_CONFIGA](../message/ee_get_configa) メッセージを直接送ることができます。

Editor\_DocGetConfigA( HWND hwnd, int iDoc, LPSTR szConfigName );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iDoc_

> 対象となるドキュメントの 0 を基底とするインデックスを指定します。-1 を指定すると、現在アクティブなドキュメントを対象とします。

_szConfigName_

> 設定の名前を取得するバッファを指定します。バッファは、ヌル文字 ('\\0') を含めて MAX\_CONFIG\_NAME の長さを確保します。

## 戻り値

> 戻り値は利用されません。

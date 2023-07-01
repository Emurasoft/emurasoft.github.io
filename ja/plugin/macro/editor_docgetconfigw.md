# Editor\_DocGetConfigW

現在アクティブな選択されている設定の名前をUnicode文字列で取得します。このインライン関数を使うか、または
[EE\_GET\_CONFIGW](../message/ee_get_configw) メッセージを直接送ることができます。

Editor\_DocGetConfigW( HWND hwnd, int iDoc, LPWSTR szConfigName );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_iDoc_

> 対象となる文書の 0 を基底とするインデックスを指定します。-1 を指定すると、現在アクティブな文書を対象とします。

_szConfigName_

> 設定の名前を取得するバッファを指定します。バッファは、ヌル文字 ('\\0') を含めて MAX\_CONFIG\_NAME の長さ(文字数)を確保します。

## 戻り値

> 戻り値は利用されません。

# EE\_GET\_CONFIGW

選択されている設定の名前をUnicode文字列で取得します。このメッセージを直接送るか、 [Editor\_DocGetConfigW インライン関数](../macro/editor_docgetconfigw)、または
[Editor\_GetConfigW インライン関数](../macro/editor_getconfigw) を使うことができます。

EE\_GET\_CONFIGW

wParam = MAKEWPARAM(0, (iDoc)+1);

lParam = (LPARAM) (LPWSTR) szConfigName;

## パラメータ

_iDoc_

> 対象となる文書のインデックスを指定します。wParam の上位ワードには 1 を基底とするインデックスを指定します。wParam の上位ワードが 0 の場合、現在アクティブな文書を対象とします。

_szConfigName_

> 設定の名前を取得するバッファを指定します。バッファは、ヌル文字 ('\\0') を含めて MAX\_CONFIG\_NAME の長さ(文字数)を確保します。

## 戻り値

> 戻り値は利用されません。

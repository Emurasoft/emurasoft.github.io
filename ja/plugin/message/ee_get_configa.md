# EE\_GET\_CONFIGA

選択されている設定の名前をANSI文字列で取得します。このメッセージを直接送るか、 [Editor\_DocGetConfigA インライン関数](../macro/editor_docgetconfiga)、または
[Editor\_GetConfigA インライン関数](../macro/editor_getconfiga) を使うことができます。

EE\_GET\_CONFIGA

wParam = MAKEWPARAM(0, (iDoc)+1);

lParam = (LPARAM) (LPSTR) szConfigName;

または

EE\_GET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPSTR) szConfigName;

## パラメータ

_iDoc_

> 対象となる文書のインデックスを指定します。wParam の上位ワードには 1 を基底とするインデックスを指定します。wParam の上位ワードが 0 の場合、現在アクティブな文書を対象とします。

_szConfigName_

> 設定の名前を取得するバッファを指定します。バッファは、ヌル文字 ('\\0') を含めて MAX\_CONFIG\_NAME の長さを確保します。

## 戻り値

> 戻り値は利用されません。

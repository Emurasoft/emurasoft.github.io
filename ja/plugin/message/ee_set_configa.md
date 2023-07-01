# EE\_SET\_CONFIGA

選択されている設定の名前をANSI文字列で設定しますこのメッセージを直接送るか、 [Editor\_DocSetConfigA インライン関数](../macro/editor_docsetconfiga)、または
[Editor\_SetConfigA インライン関数](../macro/editor_setconfiga) を使うことができます。

EE\_SET\_CONFIGA

wParam = (WPARAM) MAKEWPARAM(0, (iDoc)+1);

lParam = (LPARAM) (LPCSTR) szConfigName;

または

EE\_SET\_CONFIGA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szConfigName;

## パラメータ

_iDoc_

> 対象となる文書のインデックスを指定します。wParam の上位ワードには 1 を基底とするインデックスを指定します。wParam の上位ワードが 0 の場合、現在アクティブな文書を対象とします。

_szConfigName_

> 設定の名前を指定します。

## 戻り値

> 戻り値は利用されません。

## バージョン

> Version 4.00 以上で利用できます。ただし、iDoc パラメータは Version 5.00 以上で利用できます。

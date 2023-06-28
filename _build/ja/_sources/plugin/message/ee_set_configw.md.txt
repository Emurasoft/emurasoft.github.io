# EE\_SET\_CONFIGW

選択されている設定の名前をUnicode文字列で取得します。このメッセージを直接送るか、または
[Editor\_SetConfigW インライン関数](../macro/editor_setconfigw) を使うことができます。

EE\_SET\_CONFIGW

wParam = MAKEWPARAM(0, (iDoc)+1);

lParam = (LPARAM) (LPCWSTR) szConfigName;

または

EE\_SET\_CONFIGW

wParam = 0;

lParam = (LPARAM) (LPCWSTR) szConfigName;

## パラメータ

_iDoc_

> 対象となる文書のインデックスを指定します。wParam の上位ワードには 1 を基底とするインデックスを指定します。wParam の上位ワードが 0 の場合、現在アクティブな文書を対象とします。

_szConfigName_

> 設定の名前を指定します。

## 戻り値

> 戻り値は利用されません。

## バージョン

> Version 3.00 以上で利用できます。ただし、iDoc パラメータは Version 5.00 以上で利用できます。
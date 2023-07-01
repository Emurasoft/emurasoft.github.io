# EE\_QUERY\_STRING\_EX

指定するコマンドに関連する文字列を取得します。このメッセージは MAX\_PATH 文字を超える長いファイル パスをサポートしています。このメッセージを直接送るか、または
[Editor\_QueryStringEx インライン関数](../macro/editor_querystringex) を使うことができます。

EE\_QUERY\_STRING

wParam = 0;

lParam = (LPARAM) (QUERY\_STRING\_INFO\*) pInfo;

## パラメータ

_pInfo_

> [QUERY\_STRING\_INFO 構造体](../structure/query_string_info) へのポインタを指定します。

## 戻り値

> 成功すると S\_OK を返します。それ以外の場合は負の値を返します。

## バージョン

EmEditor Professional Version 20.6 以上で利用できます。

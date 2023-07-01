# EE\_GET\_ACTIVE\_STRING

マウス ポインターがポイントしているアクティブな文字列を取得します。このメッセージを直接送るか、または [Editor\_GetActiveStringインライン関数](../macro/editor_getactivestring) を使うことができます。

EE\_GET\_ACTIVE\_STRING

wParam = (WPARAM) 0;

lParam = (LPARAM) (ACTIVE\_STRING\_INFO\*) pInfo;

## パラメータ

_pInfo_

> [ACTIVE\_STRING\_INFO 構造体](../structure/active_string_info) へのポインタを指定します。

## 戻り値

> アクティブな文字列を終端NULL文字を含めて取得するのに必要なバッファのサイズを文字単位で指定します。

## バージョン

> Version 16.9 以上で利用できます。

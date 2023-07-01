# EE\_REG\_QUERY\_VALUE

EmEditor の設定に応じて、レジストリまたは INI ファイルから、指定する値を取得します。このメッセージを直接送るか、または [Editor\_RegQueryValue インライン関数](../macro/editor_regqueryvalue) を使うことができます。

EE\_REG\_QUERY\_VALUE

wParam = 0;

(REG\_QUERY\_VALUE\_INFO\*)lParam = pRegQueryValueInfo;

## パラメータ

_pRegSetValueInfo_

> [REG\_QUERY\_VALUE\_INFO 構造体](../structure/reg_query_value_info) へのポインタ。

## 戻り値

> 成功すると ERROR\_SUCCESS を返します。失敗すると Winerror.h で定義された 0 でないエラーコードを返します。

## バージョン

EmEditor Version 7.00 以上で利用できます。

# EE\_REG\_SET\_VALUE

EmEditor の設定に応じて、レジストリまたは INI ファイルに、値を設定します。このメッセージを直接送るか、または [Editor\_RegSetValue インライン関数](../macro/editor_regsetvalue) を使うことができます。

EE\_REG\_SET\_VALUE

wParam = 0;

(REG\_SET\_VALUE\_INFO\*)lParam = pRegSetValueInfo;

## パラメータ

_pRegSetValueInfo_

[REG\_SET\_VALUE\_INFO 構造体](../structure/reg_set_value_info) に指示します。

## 戻り値

成功すると ERROR\_SUCCESS を返します。失敗すると Winerror.h で定義された 0 でないエラーコードを返します。

## バージョン

EmEditor Version 7.00 以上で利用できます。

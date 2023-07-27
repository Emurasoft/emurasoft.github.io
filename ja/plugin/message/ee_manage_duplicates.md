# EE\_MANAGE\_DUPLICATES

重複行を削除またはブックマークします。このメッセージを直接送るか、または
[Editor\_ManageDuplicates インライン関数](../macro/editor_manageduplicates) を使うことができます。

EE\_MANAGE\_DUPLICATES

wParam = 0;

lParam = (LPARAM) (MANAGE\_DUPLICATES\_INFO\*) pManageDuplicatesInfo;

## パラメータ

_pManageDuplicatesInfo_

[MANAGE\_DUPLICATES\_INFO 構造体](../structure/manage_duplicates_info) へのポインタを指定します。

## 戻り値

戻り値は HRESULT 値になります。0 以上の整数は成功を意味し、0 未満の整数は失敗を意味します。

## バージョン

Version 16.4 以上で利用できます。

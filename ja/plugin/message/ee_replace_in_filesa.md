# EE\_REPLACE\_IN\_FILESA

指定するパスの複数のファイルから ANSI 文字列を置換します。このメッセージを直接送るか、または
[Editor\_ReplaceInFilesA インライン関数](../macro/editor_replaceinfilesa) を使うことができます。

EE\_REPLACE\_IN\_FILESA

wParam = 0;

lParam = (LPARAM) (GREP\_INFOA) pGrepInfo;

## パラメータ

_pGrepInfo_

[GREP\_INFOA 構造体](../structure/grep_infoa) へのポインタを指定します。

## 戻り値

ユーザーが処理を中止した場合 FALSE を返します。そうでなければ 0 以外の値を返します。

## バージョン

EmEditor Professional Version 4.02 以上で利用できます。

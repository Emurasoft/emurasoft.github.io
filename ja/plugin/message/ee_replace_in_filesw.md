# EE\_REPLACE\_IN\_FILESW

指定するパスの複数のファイルから Unicode 文字列を検索します。このメッセージを直接送るか、または
[Editor\_ReplaceInFilesW インライン関数](../macro/editor_replaceinfilesw) を使うことができます。

EE\_REPLACE\_IN\_FILESW

wParam = 0;

lParam = (LPARAM) (GREP\_INFOW) pGrepInfo;

## パラメータ

_pGrepInfo_

> [GREP\_INFOW 構造体](../structure/grep_infow) へのポインタを指定します。

## 戻り値

> ユーザーが処理を中止した場合 FALSE を返します。そうでなければ 0 以外の値を返します。

## バージョン

> EmEditor Professional Version 4.02 以上で利用できます。
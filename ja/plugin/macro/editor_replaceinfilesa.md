# Editor\_ReplaceInFilesA

指定するパスの複数のファイルから ANSI 文字列を置換します。このメッセージを直接送るか、または
[EE\_REPLACE\_IN\_FILESA メッセージ](../message/ee_replace_in_filesa) を使うことができます。

Editor\_ReplaceInFilesA( HWND hwnd, GREP\_INFOA pGrepInfo );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pGrepInfo_

[GREP\_INFOA 構造体](../structure/grep_infoa) へのポインタを指定します。

## 戻り値

ユーザーが処理を中止した場合 FALSE を返します。そうでなければ 0 以外の値を返します。

## バージョン

EmEditor Professional v4.02 以上で利用できます。

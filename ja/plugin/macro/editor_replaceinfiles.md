# Editor\_ReplaceInFiles

指定するパスの複数のファイルから文字列を置換します。このメッセージを直接送るか、または
[EE\_REPLACE\_IN\_FILESW メッセージ](../message/ee_replace_in_filesw) を使うことができます。

Editor\_ReplaceInFiles( HWND hwnd, GREP\_INFO\_EX\* pGrepInfo );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pGrepInfo_

[GREP\_INFO\_EX 構造体](../structure/grep_infow) へのポインタを指定します。

## 戻り値

ユーザーが処理を中止した場合 FALSE を返します。そうでなければ 0 以外の値を返します。

## バージョン

EmEditor Professional v15.7 以上で利用できます。

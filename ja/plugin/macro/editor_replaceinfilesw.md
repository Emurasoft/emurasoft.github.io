# Editor\_ReplaceInFilesW

指定するパスの複数のファイルから Unicode 文字列を置換します。このインライン関数は使用されなくなります。新しいプラグインは、 [Editor\_ReplaceInFiles インライン関数](editor_replaceinfiles) を使用してください。このメッセージを直接送るか、または
[EE\_REPLACE\_IN\_FILESW メッセージ](../message/ee_replace_in_filesw) を使うことができます。

Editor\_ReplaceInFilesW( HWND hwnd, GREP\_INFOW pGrepInfo );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pGrepInfo_

> [GREP\_INFOW 構造体](../structure/grep_infow) へのポインタを指定します。

## 戻り値

> ユーザーが処理を中止した場合 FALSE を返します。そうでなければ 0 以外の値を返します。

## バージョン

> EmEditor Professional v4.02 以上で利用できます。

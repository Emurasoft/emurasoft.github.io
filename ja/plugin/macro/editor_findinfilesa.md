# Editor\_FindInFilesA

指定するパスの複数のファイルから ANSI 文字列を検索します。検索したファイルの一覧は現在のウィンドウに表示されます。ファイルを保存していない場合は、ファイルを保存するかどうかを選択するメッセージ ボックスが表示されます。このメッセージを直接送るか、または
[EE\_FIND\_IN\_FILESA メッセージ](../message/ee_find_in_filesa) を使うことができます。

Editor\_FindInFilesA( HWND hwnd, GREP\_INFOA pGrepInfo );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pGrepInfo_

> [GREP\_INFOA 構造体](../structure/grep_infoa) へのポインタを指定します。

## 戻り値

> ユーザーが処理を中止した場合 FALSE を返します。そうでなければ 0 以外の値を返します。

## バージョン

> EmEditor Professional v4.02 以上で利用できます。
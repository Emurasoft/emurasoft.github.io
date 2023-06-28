# Editor\_FindInFiles

指定するパスの複数のファイルから文字列を検索します。検索したファイルの一覧は現在のウィンドウに表示されます。ファイルを保存していない場合は、ファイルを保存するかどうかを選択するメッセージ ボックスが表示されます。このメッセージを直接送るか、または
[EE\_FIND\_IN\_FILESW メッセージ](../message/ee_find_in_filesw) を使うことができます。

Editor\_FindInFiles( HWND hwnd, GREP\_INFO\_EX\* pGrepInfo );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pGrepInfo_

> [GREP\_INFO\_EX 構造体](../structure/grep_infow) へのポインタを指定します。

## 戻り値

> ユーザーが処理を中止した場合 FALSE を返します。そうでなければ 0 以外の値を返します。

## バージョン

> EmEditor Professional v15.7 以上で利用できます。
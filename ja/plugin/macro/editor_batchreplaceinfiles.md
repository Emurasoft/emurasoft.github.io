# Editor\_BatchReplaceInFiles

指定するパスの複数のファイルから複数の文字列を置換します。このメッセージを直接送るか、または
[EE\_REPLACE\_IN\_FILESW メッセージ](../message/ee_replace_in_filesw) を使うことができます。

Editor\_BatchReplaceInFiles( HWND hwnd, FIND\_REPLACE\_INFO\* pBatchArray, BATCH\_GREP\_INFO\* pGrepInfo );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pBatchArray_

> [FIND\_REPLACE\_INFO 構造体](../structure/find_replace_info) の配列へのポインタを指定します。

_pBatchGrepInfo_

> [BATCH\_GREP\_INFO 構造体へのポインタを指定します。](../structure/batch_grep_info)

## 戻り値

> ユーザーが処理を中止した場合 FALSE を返します。そうでなければ 0 以外の値を返します。

## バージョン

> EmEditor Professional v20.0 以上で利用できます。

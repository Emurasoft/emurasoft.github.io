# EE\_FIND\_REPLACE

文字列を検索または置換します。このメッセージを直接送るか、または [Editor\_FindReplace](../macro/editor_findreplace) または [Editor\_BatchFindReplace](../macro/editor_batchfindreplace) インライン関数を使うことができます。

EE\_FIND\_REPLACE

wParam = (WPARAM) (BATCH\_INFO\*) pBatchInfo;

lParam = (LPARAM) (FIND\_REPLACE\_INFO\*) pFindReplaceInfo;

## パラメータ

_pBatchInfo_

[BATCH\_INFO 構造体](../structure/batch_info) へのポインタを指定します。連続検索を指定しない場合、このパラメータは NULL にすることができます。

_pFindReplaceInfo_

[FIND\_REPLACE\_INFO 構造体](../structure/find_replace_info) へのポインタを指定します。pBatchInfo が NULL でない場合、このパラメータは FIND\_REPLACE\_INFO 構造体の配列を指定します。

## 戻り値

文字列が見つかった場合は S\_OK を返します。見つからない場合は S\_FALSE を返します。エラーが発生すると、戻り値は負の数になります。負の値には、次の値が含まれます。ユーザーが検索を中止すると、E\_ABORT を返し、致命的なエラーが発生すると E\_FAIL を返します。

## バージョン

Version 15.7 以上で利用できます。

# EE\_JOIN

SQL においての JOIN 操作と同様な方法を使って、2個の CSV 文書を結合して新規文書を作成します。このメッセージを直接送るか、または
[Editor\_Join インライン関数](../macro/editor_join) を使うことができます。

EE\_JOIN

wParam = (WPARAM) (JOIN\_INFO\*) pJoinInfo;

lParam = 0;

## パラメータ

_pJoinInfo_

[JOIN\_INFO 構造体](../structure/join_info) へのポインタを指定します。

## 戻り値

戻り値は、出力文書の行数になります。エラーが発生すると戻り値は負の数になります。エラーが発生すると、戻り値は次のいずれかの値になることがあります。

|     |     |
| --- | --- |
| E\_DOCUMENT\_1\_NOT\_FOUND | 第1文書が見つかりません。 |
| E\_DOCUMENT\_2\_NOT\_FOUND | 第2文書が見つかりません。 |
| E\_COLUMN\_1\_NOT\_FOUND | 1列目が見つかりません。 |
| E\_COLUMN\_2\_NOT\_FOUND | 2列目が見つかりません。 |
| E\_SELECT\_SYNTAX | 選択文字列の中に構文エラーがあります。 |
| E\_SELECT\_DOCUMENT\_NOT\_FOUND | 選択文字列の中に指定した文書が見つかりません。 |
| E\_SELECT\_COLUMN\_NOT\_FOUND | 選択文字列の中に指定した列が見つかりません。 |
| E\_DIFFERENT\_CSV\_MODE | 異なる CSV モードです。 |
| E\_NOT\_MDI | タブが有効になっている必要があります。 |
| E\_WRITE\_TEMP\_FILE | 一時ファイルの書き込みエラー。 |
| E\_ABORT | ユーザーによって中止されました。 |
| E\_FAIL | 詳細不明のエラー。 |

## バージョン

Version 14.8 以上で利用できます。

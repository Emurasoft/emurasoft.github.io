# EE\_COMPARE

2個の文書を比較します。このメッセージを直接送るか、または
[Editor\_Compare インライン関数](../macro/editor_compare) を使うことができます。

EE\_COMPARE

wParam = (WPARAM) (COMPARE\_INFO\*) pCompareInfo;

lParam = 0;

## パラメータ

_pCompareInfo_

[COMPARE\_INFO 構造体](../structure/compare_info) へのポインタを指定します。

## 戻り値

戻り値は次のいずれかの値になることがあります。エラーが発生すると戻り値は負の数になります。

|     |     |
| --- | --- |
| E\_DOCUMENT\_1\_NOT\_FOUND | 第1文書が見つかりません。 |
| E\_DOCUMENT\_2\_NOT\_FOUND | 第2文書が見つかりません。 |
| E\_FAIL | 詳細不明のエラー。 |
| E\_NOT\_MDI | タブが有効になっている必要があります。 |
| S\_DIFF | 2個の文書は同じではありません。 |
| S\_MATCHED | 2個の文書は同じです。 |
| S\_MATCHED\_IGNORED | 2個の文書は無視した場所を除き同じです。 |

## バージョン

Version 17.7 以上で利用できます。

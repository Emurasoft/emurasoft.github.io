# EE\_EXTRACT\_FREQUENT

頻出文字列を抽出して新規文書を作成します。このメッセージを直接送るか、または [Editor\_ExtractFrequent インライン関数](../macro/editor_extractfrequent) 使うことができます。

EE\_EXTRACT\_FREQUENT

wParam = (WPARAM)(EXTRACT\_FREQUENT\_INFO\*)pInfo;

lParam = 0;

## パラメータ

_pInfo_

[EXTRACT\_FREQUENT\_INFO 構造体](../structure/extract_frequent_info) へのポインタを指定します。

## 戻り値

エラーが発生すると、負の値を返します。

## バージョン

Version 21.9 以上で利用できます。

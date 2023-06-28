# EE\_CONVERT\_CSV

現在の文書のCSV形式を変換します。このメッセージを直接送るか、または [Editor\_ConvertCsv インライン関数](../macro/editor_convertcsv) を使うことができます。

EE\_EDIT\_COLUMN

wParam = (WPARAM)(CONVERT\_CSV\_INFO\*)pInfo;

lParam = 0;

## パラメータ

_pInfo_

> [CONVERT\_CSV\_INFO 構造体](../structure/convert_csv_info) へのポインタを指定します。

## 戻り値

> 成功すると S\_OK を返します。

## バージョン

> EmEditor Professional Version 19.8 以上で利用できます。
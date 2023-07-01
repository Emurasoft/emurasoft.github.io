# EE\_INFO\_EX

実行中の EmEditor または指定するドキュメントに関する情報を取得または設定を行います。このメッセージを直接送るか、または [Editor\_DocInfoEx インライン関数](../macro/editor_docinfoex) 使うことができます。

EE\_INFO\_EX

wParam = (WPARAM)(INFO\_EX\_DATA\*)pInfo;

lParam = 0;

## パラメータ

_pInfo_

> [INFO\_EX\_DATA 構造体](../structure/info_ex_data) へのポインタを指定します。

## 戻り値

> 指定するパラメータに依存します。

## バージョン

> Version 21.8 以上で利用できます。

# EE\_CONVERT\_EX

文字変換を行います。このメッセージを直接送るか、または [Editor\_Convert インライン関数](../macro/editor_convert) を使うことができます。

EE\_CONVERT

wParam = (WPARAM) (CONVERT\_INFO\*)pInfo;

lParam = 0;

## パラメータ

_pInfo_

[CONVERT\_INFO 構造体](../structure/convert_info) へのポインタを指定します。

## 戻り値

成功すると 0 以外を返します。失敗すると 0 を返します。

# EE\_GET\_UNICODE\_NAME

指定された文字または文字列のUnicode名を取得します。このメッセージを直接送るか、または
[Editor\_GetUnicodeName インライン関数](../macro/editor_getunicodename) を使うことができます。

```
EE_GET_UNICODE_NAME
wParam = (WPARAM)(UNICODE_NAME_INFO*)pUNI;
lParam = 0;
```

## パラメータ

_pUNI_

[UNICODE\_NAME\_INFO 構造体](../structure/unicode_name_info) へのポインタを指定します。

## 戻り値

UNICODE\_NAME\_INFO 構造体の _cchBuf_ に 0 を指定した場合、バッファに必要なサイズを文字単位で返します。

## バージョン

Version 19.1 以上で利用できます。

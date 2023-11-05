# EE\_GET\_COLOR

指定する部分の文字色、背景色、スタイルを取得します。このメッセージを直接送るか、または [Editor\_GetColor インライン関数](../macro/editor_getcolor) を使うことができます。

```
EE_GET_COLOR
wParam = 0;
lParam = (LPARAM) (GET_COLOR_INFO*) pGetColorInfo;
```

## パラメータ

_pGetColorInfo_

GET\_COLOR\_INFO 構造体へのポインタを指定します。

## 戻り値

成功すると TRUE を、失敗すると FALSE を返します。

## バージョン

Version 14.4 以上で利用できます。

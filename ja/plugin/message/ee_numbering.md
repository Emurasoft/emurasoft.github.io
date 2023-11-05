# EE\_NUMBERING

カーソル位置または垂直選択に番号を挿入します。このメッセージを直接送るか、または
[Editor\_Numbering インライン関数](../macro/editor_numbering) を使うことができます。

```
EE_NUMBERING
wParam = (WPARAM)(NUMBERING_INFO*)pNI;
lParam = 0;
```

## パラメータ

_pUNI_

[NUMBERING\_INFO 構造体](../structure/numbering_info) へのポインタを指定します。

## 戻り値

成功すると 0 を返します。

## バージョン

Version 19.1 以上で利用できます。

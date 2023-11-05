# EE\_GET\_OUTLINE\_LEVEL

指定する論理行のアウトラインのレベルを取得します。このメッセージを直接送るか、または
[Editor\_GetOutlineLevel インライン関数](../macro/editor_getoutlinelevel) を使うことができます。

```
EE_GET_OUTLINE_LEVEL
wParam = (WPARAM) (INT_PTR) nLogicalLine;
lParam = 0;
```

## パラメータ

_nLogicalLine_

アウトラインのレベルを取得したい論理行を指定します。

## 戻り値

指定する論理行のアウトラインのレベルを返します。

## バージョン

EmEditor Professional Version 6.00 以上で利用できます。

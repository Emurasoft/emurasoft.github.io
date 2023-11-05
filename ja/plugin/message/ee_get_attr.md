# EE\_GET\_ATTR

構成を取得して、指定した位置に返します。このメッセージを直接送るか、または [Editor\_GetAttrインライン関数](../macro/editor_getattr) を使うことができます。

```
EE_GET_ATTR
wParam = 0;
lParam = (LPARAM) (ATTR_INFO) pAI;
```

## パラメータ

_pAI_

[ATTR\_INFO 構造体](../structure/attr_info) へのポインタを指定します。

## 戻り値

成功すると TRUE を返します。失敗すると FALSE を返します。

## バージョン

Version 9.00 以上で利用できます。

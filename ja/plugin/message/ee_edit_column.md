# EE\_EDIT\_COLUMN

現在の CSV 文書の指定された列を移動、コピー、削除、または結合します。このメッセージを直接送るか、または
[Editor\_EditColumn インライン関数](../macro/editor_editcolumn) を使うことができます。

```
EE_EDIT_COLUMN
wParam = (WPARAM)(EDIT_COLUMN_INFO*)pInfo;
lParam = 0;
```

## パラメータ

_pInfo_

[EDIT\_COLUMN\_INFO 構造体](../structure/edit_column_info) へのポインタを指定します。

## 戻り値

成功すると S\_OK を返します。

## バージョン

Version 19.7 以上で利用できます。

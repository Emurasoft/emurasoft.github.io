# EE\_SET\_OUTLINE\_ARRAY

指定する複数行のアウトラインのレベルを設定します。このメッセージを直接送るか、または
[Editor\_SetOutlineArray インライン関数](../macro/editor_setoutlinearray) を使うことができます。

```
EE_SET_OUTLINE_ARRAY
wParam = (WPARAM) 0;
lParam = (LPARAM) (OUTLINE_ARRAY_INFO*) pOutlineArrayInfo;
```

## パラメータ

_pOutlineArrayInfo_

[OUTLINE\_ARRAY\_INFO](../structure/outline_array_info) 構造体へのポインタを指定します。

## 戻り値

変更が無い場合には FALSE が返されます。それ以外では TRUE が返されます。

## バージョン

Version 13 以上で利用できます。

# EE\_GET\_MODIFIED

文書が更新されているかどうかのフラグを取得します。このメッセージを直接送るか、 [Editor\_DocGetModified インライン関数](../macro/editor_docgetmodified)、または
[Editor\_GetModified インライン関数](../macro/editor_getmodified) を使うことができます。

```
EE_GET_MODIFIED
wParam = (WPARAM) MAKEWPARAM(0, (iDoc)+1);
lParam = hDoc;
または
EE_GET_MODIFIED
wParam = 0;
lParam = 0;
```

## パラメータ

_iDoc_

対象となるドキュメントのインデックスを指定します。wParam の上位ワードには 1 を基底とするインデックスを指定します。wParam の上位ワードが 0 の場合、現在アクティブなドキュメントを対象とします。

_hDoc_

省略可能。対象となるドキュメントへのハンドルを指定します。このパラメータを指定する場合、iDoc は 0 である必要があります。

## 戻り値

更新されている場合は TRUE を、更新されていない場合は FALSE を返します。

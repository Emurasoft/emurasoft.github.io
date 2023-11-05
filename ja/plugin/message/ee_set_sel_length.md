# EE\_SET\_SEL\_LENGTH

選択テキストの長さを設定します。このメッセージを直接送るか、または [Editor\_SetSelLength インライン関数](../macro/editor_setsellength) を使うことができます。

```
EE_SET_SEL_LENGTH
wParam = (WPARAM) (UINT_PTR) nLen;
lParam = 0;
```

## パラメータ

_nLen_

選択テキストの長さを指定します。改行コードは、常に 2文字分 (CR+LF) となります。

## 戻り値

戻り値は利用されません。

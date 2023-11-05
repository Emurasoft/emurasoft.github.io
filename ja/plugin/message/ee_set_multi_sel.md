# EE\_SET\_MULTI\_SEL

複数選択が利用可能な場合、指定する選択の情報を設定します。このメッセージを直接送るか、または
[Editor\_SetMultiSel インライン関数](../macro/editor_setmultisel) を使うことができます。

```
EE_SET_MULTI_SEL
wParam = (WPARAM) (UINT_PTR) iSel;
lParam = (LPARAM) (const SEL_INFO*) pSelInfo;
```

## パラメータ

_iSel_

情報を設定する選択のインデックスを指定します。

_pSelInfo_

[SEL\_INFO 構造体](../structure/sel_info) へのポインタを指定します。

## 戻り値

指定した選択に関する情報を設定したら TRUE を返します。選択が複数選択モードでない場合、またはエラーが発生すると、FALSE を返します。

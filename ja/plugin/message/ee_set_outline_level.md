# EE\_SET\_OUTLINE\_LEVEL

指定する論理行のアウトラインのレベルを設定します。このメッセージを直接送るか、または
[Editor\_SetOutlineLevel インライン関数](../macro/editor_setoutlinelevel) を使うことができます。

```
EE_SET_OUTLINE_LEVEL
wParam = (WPARAM) (INT_PTR) nLogicalLine;
lParam = (LPARAM) (int) nLevel;
```

## パラメータ

_nLogicalLine_

アウトラインのレベルを設定したい論理行を指定します。

_nLevel_

アウトラインのレベルを指定します。

## 戻り値

戻り値は利用されません。

## バージョン

Version 6.00 以上で利用できます。

# EE\_SET\_STATUSA

ステータスメッセージにANSI文字列を設定します。このメッセージを直接送るか、または
[Editor\_SetStatusA インライン関数](../macro/editor_setstatusa) を使うことができます。

```
EE_SET_STATUSA
wParam = 0;
lParam = (LPARAM) (LPCSTR) szStatus;
```

## パラメータ

_szStatus_

ステータスバーに表示するメッセージ文字列を指定します。

## 戻り値

戻り値は利用されません。

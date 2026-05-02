# EE_GET_SEL_LENGTH

選択テキストの長さを取得します。このメッセージを直接送るか、または [Editor\_GetSelLength インライン関数](../macro/editor_getsellength) を使うことができます。

```
EE_GET_SEL_LENGTH
wParam = (WPARAM)0
lParam = (LPARAM)0
```

## Parameters

_nMaxLen_

最大の長さを指定します。長さがこの値を超える場合は、この値が返されます。

## 戻り値

戻り値は選択テキストの長さになります。

## バージョン

EmEditor Professional Version 26.1 以上で利用できます。

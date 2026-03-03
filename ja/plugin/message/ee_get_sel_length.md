# EE_GET_SEL_LENGTH

選択テキストの長さを取得します。このメッセージを直接送るか、または [Editor\_GetSelLength インライン関数](../macro/editor_getsellength) を使うことができます。

```
EE_GET_SEL_LENGTH
wParam = (WPARAM)0
lParam = (LPARAM)0
```

## 戻り値

戻り値は選択テキストの長さになります。ただし、長さが LONG_MAX を超える場合は、戻り値は LONG_MAX になります。

## バージョン

EmEditor Professional Version 26.1 以上で利用できます。

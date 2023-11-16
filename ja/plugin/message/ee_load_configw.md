# EE\_LOAD\_CONFIGW

Unicode文字列で指定する設定を読み直します。このメッセージを直接送るか、または [Editor\_LoadConfigW インライン関数](../macro/editor_loadconfigw) を使うことができます。

```
EE_LOAD_CONFIGW
wParam = 0;
lParam = (LPARAM) (LPCWSTR) szConfigName;
```

## パラメータ

_szConfigName_

設定の名前を指定します。

## 戻り値

戻り値は利用されません。

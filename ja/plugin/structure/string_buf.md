# STRING\_BUF

[EE\_INFO メッセージ](../message/ee_info) で使用します。

```
typedef struct _STRING_BUF {
	LPWSTR pBuf;
	UINT cchBuf;
} STRING_BUF;
```

## フィールド

_pBuf_

文字列を取得するバッファを指定します。

_cchBuf_

バッファのサイズを文字数で指定します。

## バージョン

Version 20.6 以上で利用できます。
